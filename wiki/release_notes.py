import os
import re
import markdown
import requests

github_token = os.environ["GITHUB_TOKEN"]
release_version = os.environ["RELEASE_VERSION"]

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
    <link rel="canonical" href="https://netatalk.sourceforge.io/{minor_version}/{file_name}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.sourceforge.io/css/site.css" />
    <link rel="icon" type="image/x-icon" href="https://netatalk.sourceforge.io/gfx/favicon.ico" />
</head>
"""

html = markdown.markdown(body["body"], extensions=['fenced_code', 'smarty', 'tables'])

pre_footer = f"""<hr />
<p>Release published on {published_at}</p>
<p>Generated from the original at <a href=\"https://github.com/Netatalk/netatalk/releases/tag/{github_tag}\">GitHub</a></p>
<hr />
</div>
"""

with open("templates/header.html", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("templates/navbar.html", "r", encoding="utf-8") as navbar_file:
    navbar = navbar_file.read()
with open("templates/footer.html", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()

with open(f"../{minor_version}/{file_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html_head)
    output_file.write(header)
    output_file.write(navbar)
    output_file.write(f"<div id=\"content\">\n<!-- content -->\n<h1>Netatalk {release_version}</h1><hr />\n")
    output_file.write(html)
    output_file.write(pre_footer)
    output_file.write(footer)
    
    print(f"Converted: {file_name}")

