import os
import re
import markdown

END_URL = ".html"

subdirs = [
    '.',
    'blog',
    'security',
# Historical release notes; later ones are built in generate_releasenotes.py
    '1.5',
    '1.6',
    '2.0',
    '2.1',
    '2.2',
    '3.0',
    '3.1',
]

def html_head(page_title, new_path):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Netatalk - {page_title}</title>
    <meta name="description" content="Netatalk Homepage">
    <link rel="canonical" href="https://netatalk.io/{new_path}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css">
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico">
</head>
"""

with open("./templates/header.html", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("./templates/navbar.html", "r", encoding="utf-8") as navbar_file:
    navbar = navbar_file.read()
with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()

for dir in subdirs:
    files = []

    for file in os.listdir(dir):
        if file.endswith(".md"):
            files.append(f"{file}")
    for file in files:
        path = f"{dir}/{file}"
        with open(f"./{dir}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                ],
            )
        page_title = file.replace('.md', '')
        new_name = file.replace('.md', '.html')
        if page_title == "index":
            page_title = "Networking Apple Macintosh through Open Source"
        else:
            page_title.capitalize()

        new_path = f"{dir}/{new_name}"
        if dir == ".":
            new_path = new_name
        with open(f"./public/{new_path}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(page_title, new_path))
            output_file.write(header)
            output_file.write(navbar)
            output_file.write("<div id=\"content\">")
            output_file.write(html)
            output_file.write("</div>")
            output_file.write(footer)

        print(f"Converted: {file}")
