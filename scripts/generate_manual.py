import os
import re
import markdown
from markdown.extensions.toc import TocExtension

navbar = ""
locales = ["en", "ja"]
END_URL = ".html"


def html_head(page_title, new_name):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Netatalk Manual - {page_title}</title>
    <meta name="description" content="Netatalk Manual">
    <link rel="canonical" href="https://netatalk.io/{new_name}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css" />
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico" />
</head>
"""

with open("./templates/header.html", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()

# Generate manual

for lang in locales:
    files = []
    base_url = f"/manual/{lang}/"
    with open(f"./manual/{lang}/_Sidebar.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
            ],
        )

        navbar = f"""<div id="navbars">
    <div class="navbar">
    <h2>Table of contents</h2>
    {html}
    </div></div>
    """

    for file in os.listdir(f"./manual/{lang}/"):
        if file.endswith(".md"):
            files.append(f"{file}")
    for file in files:
        if file == "_Sidebar.md":
            continue
        with open(f"./manual/{lang}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text = "[TOC]\n\n" + text
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                    TocExtension(
                        anchorlink=True,
                    ),
                ],
            )
        page_title = file.replace('.md', '')
        new_name = file.replace('.md', '.html')

        with open(f"./public/manual/{lang}/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(page_title, "manual/" + lang + "/" + new_name))
            output_file.write(header)
            output_file.write(navbar)
            output_file.write("<div id=\"content\">")
            output_file.write(html)
            output_file.write("</div>")
            output_file.write(footer)

        print(f"Converted: {lang}/{file}")


# Generate READMEs

files = []

for file in os.listdir("./manual/"):
    if file.endswith(".md"):
        files.append(f"{file}")
with open("./templates/navbar.html", "r", encoding="utf-8") as navbar_file:
    navbar = navbar_file.read()
for file in files:
    with open(f"./manual/{file}", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text = re.sub(r"\s<[^<>]+@[a-zA-Z0-9._-]+>", "", text)
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
            ],
        )
    page_title = file.replace('index', 'Index').replace('.md', '')
    new_name = file.replace('.md', '.html').lower()

    with open(f"./public/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html_head(page_title.capitalize(), new_name))
        output_file.write(header)
        output_file.write(navbar)
        output_file.write("<div id=\"content\">")
        output_file.write(html)
        output_file.write("</div>")
        output_file.write(footer)

    print(f"Converted: {new_name}")
