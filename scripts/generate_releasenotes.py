import os
import re
import markdown
import requests

# Netatalk releases 2023 onward which have release notes on GitHub.
# Earlier versions have static release notes html pages.
versions = [
    "2.2.7",
    "2.2.8",
    "2.2.9",
    "2.2.10",
    "2.3.0",
    "2.3.1",
    "3.1.14",
    "3.1.15",
    "3.1.16",
    "3.1.17",
    "3.1.18",
]

url_pattern = re.compile(r'((?:^|\s)(https?://\S+)(?=<))')
github_pattern = re.compile(r'(GitHub #)(\d+)')

github_token = os.environ["GITHUB_TOKEN"]

for release_version in versions:
    github_tag = "netatalk-" + release_version.replace(".", "-")
    minor_version = re.search(r"^(\d+\.\d+)", release_version).group()
    file_name = "ReleaseNotes" + release_version + ".html"
    url = f"https://api.github.com/repos/Netatalk/netatalk/releases/tags/{github_tag}"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + github_token,
        "X-GitHub-Api-Version": "2022-11-28",
    }

    response = requests.get(url, headers=headers)
    body = response.json()
    published_at = re.search(r"^(\d{4}-\d{2}-\d{2})", body["published_at"]).group()

    html_head = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Netatalk Release Notes - {release_version}</title>
    <meta name="description" content="Netatalk Release Notes">
    <link rel="canonical" href="https://netatalk.io/{minor_version}/{file_name}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css" />
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico" />
</head>
"""

    html = markdown.markdown(body["body"], extensions=['fenced_code', 'smarty', 'tables'])

    html = url_pattern.sub(r" <a href='\2'>\2</a>", html)
    html = github_pattern.sub(r"<a href='https://github.com/Netatalk/netatalk/issues/\2'>\1\2</a>", html)

    pre_footer = f"""<hr />
<p>Release published on {published_at}</p>
<p>Generated from the original at <a href=\"https://github.com/Netatalk/netatalk/releases/tag/{github_tag}\">GitHub</a></p>
<hr />
</div>
"""

    with open("./templates/header.html", "r", encoding="utf-8") as header_file:
        header = header_file.read()
    with open("./templates/navbar.html", "r", encoding="utf-8") as navbar_file:
        navbar = navbar_file.read()
    with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
        footer = footer_file.read()

    with open(f"./public/{minor_version}/{file_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html_head)
        output_file.write(header)
        output_file.write(navbar)
        output_file.write(f"<div id=\"content\">\n<h1>Netatalk {release_version}</h1><hr />\n")
        output_file.write(html)
        output_file.write(pre_footer)
        output_file.write(footer)

        print(f"Converted: {file_name}")
