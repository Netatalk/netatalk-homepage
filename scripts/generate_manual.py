import os
import re
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

files = []
navbar = ""
locales = ["en", "ja"]


def html_head(name):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Netatalk Manual - {name.replace('-', ' ')}</title>
    <meta name="description" content="Netatalk Manual">
    <link rel="canonical" href="https://netatalk.io/manual/{name}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css" />
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico" />
</head>
"""

def build_url(label, base, end):
    """ Build a URL from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|([_][ ]+)|([ ]+)', '-', label)
    return '{}{}{}'.format(base, clean_label, end)

for lang in locales:
    base_url = f"/manual/{lang}/"
    end_url = ".html"
    with open(f"./manual/{lang}/_Sidebar.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(
            text,
            extensions=[
                'fenced_code',
                'smarty',
                'tables',
                WikiLinkExtension(
                    base_url=base_url,
                    end_url=end_url,
                    build_url=build_url,
                    html_class='',
                ),
            ],
        )

        replacements = [
            # FIXME: A more scalable approach to create intra-linguistic navbar links.
            (fr"/{re.escape(lang)}/en.html", r'/en/index.html'),
            (fr"/{re.escape(lang)}/ja.html", r'/ja/index.html'),
            # FIXME: Workaround for https://github.com/Python-Markdown/markdown/pull/1504
            (r"\[\[afp\.conf\]\]", fr'<a href="{base_url}afp.conf.{end_url}">afp.conf</a>'),
            (r"\[\[afp_signature\.conf\]\]", fr'<a href="{base_url}afp_signature.conf.{end_url}">afp_signature.conf</a>'),
            (r"\[\[afp_voluuid\.conf\]\]", fr'<a href="{base_url}afp_voluuid.conf.{end_url}">afp_voluuid.conf</a>'),
            (r"\[\[afp\.conf\]\]", fr'<a href="{base_url}afp.conf.{end_url}">afp.conf</a>'),
            (r"\[\[atalkd\.conf\]\]", fr'<a href="{base_url}atalkd.conf.{end_url}">atalkd.conf</a>'),
            (r"\[\[extmap\.conf\]\]", fr'<a href="{base_url}extmap.conf.{end_url}">extmap.conf</a>'),
            (r"\[\[papd\.conf\]\]", fr'<a href="{base_url}papd.conf.{end_url}">papd.conf</a>')
        ]

        for pattern, replacement in replacements:
            html = re.sub(pattern, replacement, html)

        navbar = f"""<div id="navbars">
    <div class="navbar">
    <h2>Table of contents</h2>
    {html}
    </div></div>
    """

    for file in os.listdir(f"./manual/{lang}/"):
        if file.endswith(".md"):
            files.append(f"{file}")
    with open("./templates/header.html", "r", encoding="utf-8") as header_file:
        header = header_file.read()
    with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
        footer = footer_file.read()
    for file in files:
        if file == "_Sidebar.md":
            continue
        with open(f"./manual/{lang}/{file}", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            html = markdown.markdown(
                text,
                extensions=[
                    'fenced_code',
                    'smarty',
                    'tables',
                    WikiLinkExtension(
                        base_url="/manual/{lang}/",
                        end_url=".html",
                        build_url=build_url,
                        html_class=''
                    )
                ]
            )
        page_title = file.replace('.md', '')
        new_name = file.replace('.md', '.html')

        with open(f"./public/manual/{lang}/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html_head(page_title))
            output_file.write(header)
            output_file.write(navbar)
            output_file.write("<div id=\"content\">")
            output_file.write(html)
            output_file.write("</div>")
            output_file.write(footer)

        print(f"Converted: {lang}/{file}")
