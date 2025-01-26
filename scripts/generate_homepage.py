import os
import re
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

END_URL = ".html"

subdirs = [
    './',
    './blog/',
    './security/',
# Historical release notes; later ones are built in generate_releasenotes.py
    './1.5/',
    './1.6/',
    './2.0/',
    './2.1/',
    './2.2/',
    './3.0/',
    './3.1/',
]

def html_head(name):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Netatalk - {name.replace('index', 'Index').replace('-', ' ')}</title>
    <meta name="description" content="Netatalk Homepage">
    <link rel="canonical" href="https://netatalk.io/{name}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css" />
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico" />
</head>
"""

with open("./templates/header.html", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("./templates/navbar.html", "r", encoding="utf-8") as navbar_file:
    navbar = navbar_file.read()
with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()

def build_url(label, base, end):
    """ Build a URL from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|([_][ ]+)|([ ]+)', '-', label)
    return '{}{}{}'.format(base, clean_label, end)

for dir in subdirs:
    files = []

    for file in os.listdir(dir):
        if file.endswith(".md"):
            files.append(f"{file}")
    for file in files:
        with open(f"./{dir}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                    WikiLinkExtension(
                        base_url=dir,
                        end_url=END_URL,
                        build_url=build_url,
                        html_class='',
                    ),
                ],
            )
        page_title = file.replace('.md', '')
        new_name = file.replace('.md', '.html')
        if page_title == "index":
            page_title = "Networking Apple Macintosh through Open Source"

        with open(f"./public/{dir}/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(page_title))
            output_file.write(header)
            output_file.write(navbar)
            output_file.write("<div id=\"content\">")
            output_file.write(html)
            output_file.write("</div>")
            output_file.write(footer)

        print(f"Converted: {file}")
