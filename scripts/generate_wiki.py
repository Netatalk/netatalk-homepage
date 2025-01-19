import os
import re

import markdown
import datetime
from markdown.extensions.wikilinks import WikiLinkExtension
from git import Repo
import urllib.parse

now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d")
files = []
navbar = ""


def html_head(name):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Netatalk Wiki - {name.replace('-', ' ')}</title>
    <meta name="description" content="Netatalk Wiki">
    <link rel="canonical" href="https://netatalk.io/docs/{name}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css" />
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico" />
</head>
"""

def pre_footer(name):
    return f"""<hr />
    <p>
        This is a mirror of the Netatalk GitHub Wiki.
        Please <a href="https://github.com/Netatalk/netatalk/wiki/{name}">visit the original page</a>
        if you want to correct an error or contribute new contents.
    </p>
    <p>Last updated {date_time}</p>
    <hr />
    </div>
"""

def build_url(label, base, end):
    """ Build a URL from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '-', label)
    return '{}{}{}'.format(base, clean_label, end)

def site_map():
    repo = Repo("wiki/")
    tree = repo.tree()

    with open("./public/docs/sitemap.xml", "w", encoding="utf-8", errors="xmlcharrefreplace") as site_map_xml:
        site_map_xml.write("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
""")
        for blob in tree:
            commit = next(repo.iter_commits(paths=blob.path, max_count=1))
            datetime_obj = datetime.datetime.fromtimestamp(commit.committed_date)
            site_map_xml.write(f"""<url>
    <loc>https://netatalk.io/docs/{urllib.parse.quote(blob.path.replace('.md', '.html'))}</loc>
    <lastmod>{datetime_obj.strftime("%Y-%m-%d")}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
</url>
""")
        site_map_xml.write('</urlset>')


with open("./wiki/_Sidebar.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
    html = markdown.markdown(text, extensions=['fenced_code', 'smarty', 'tables', WikiLinkExtension(base_url="/docs/", end_url=".html", build_url=build_url)])
    navbar = f"""<div id="navbars">
<div class="navbar">
<h2>Table of contents</h2>
{html}
</div></div>
"""

for file in os.listdir("./wiki/"):
    if file.endswith(".md"):
        files.append(f"{file}")
with open("./templates/header.html", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()
for file in files:
    if file == "_Sidebar.md":
        continue
    with open(f"./wiki/{file}", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(text, extensions=['fenced_code', 'smarty', 'tables', WikiLinkExtension(base_url="/docs/", end_url=".html", build_url=build_url)])
    page_title = file.replace('.md', '')
    new_name = file.replace('.md', '.html')
    if new_name == "Home.html":
        new_name = "index.html"

    with open(f"./public/docs/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html_head(page_title))
        output_file.write(header)
        output_file.write(navbar)
        output_file.write(f"<div id=\"content\">\n<h1 id=\"{file.split('.')[0]}\">{file.split('.')[0].replace('-', ' ')}</h1>\n")
        output_file.write(html)
        output_file.write(pre_footer(page_title))
        output_file.write(footer)

    print(f"Converted: {file}")

site_map()
