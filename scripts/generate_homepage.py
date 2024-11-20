import os
import re
import requests

url = "https://raw.githubusercontent.com/Netatalk/netatalk/refs/heads/main/NEWS"

try:
    response = requests.get(url)
    response.raise_for_status()

    file_contents = """
<div id="content">
<h1>Netatalk NEWS</h1>
<pre>
""" + response.text + """
</pre>

</div>
"""

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

output_file = "./news.html.in"

try:
    with open(output_file, "w") as file:
        file.write(file_contents)
    
    print(f"File '{output_file}' created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

url = "https://raw.githubusercontent.com/Netatalk/netatalk/refs/heads/main/CONTRIBUTORS"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    file_contents = re.sub(r"\s<[^<>]+@[a-zA-Z0-9._-]+>", "", response.text)

    file_contents = """
<div id="content">
<h1>Netatalk CONTRIBUTORS</h1>
<pre>
""" + file_contents + """
</pre>

</div>
"""

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

output_file = "./contributors.html.in"

try:
    with open(output_file, "w") as file:
        file.write(file_contents)
    
    print(f"File '{output_file}' created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

files = []

for file in os.listdir("./"):
    if file.endswith(".in"):
        files.append(f"{file}")
with open("./templates/header.html", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("./templates/navbar.html", "r", encoding="utf-8") as navbar_file:
    navbar = navbar_file.read()
with open("./templates/footer.html", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()
for file in files:
    with open(f"./{file}", "r", encoding="utf-8") as input_file:
        html = input_file.read()
    new_name = file.replace('.html.in', '.html')
    page_title = new_name.replace('.html', '')
    if new_name[0:3] == "CVE":
        new_name = new_name.replace("CVE", "security/CVE")
    if page_title == "index":
        page_title = "Networking Apple Macintosh through Open Source"

    html_head = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="description" content="Netatalk - Networking Apple Macintosh through Open Source" />
<meta
  name="keywords"
  content="Netatalk, AFP, AFP Server, AppleShare, File Server, PAP, Print Server, AppleTalk, Macintosh, Mac, OSX, OS X, OS9, OS 9, macOS, Apple II, IIGS, GS/OS, IIe" />
<meta name="language" content="EN" />
<meta name="publisher" content="netatalk.io" />
<meta name="robots" content="index,follow" />
<meta name="audience" content="all" />

<link rel="stylesheet" type="text/css" href="/css/site.css" />
<link rel="stylesheet" type="text/css" href="/css/printer.css" media="print" />
<link rel="alternate stylesheet" type="text/css" href="/css/printer.css" title="Printer" />
<link
  rel="copyright"
  title="GNU General Public License, version 2"
  href="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html" />
<link rel="author" title="The Netatalk Development Team" href="http://netatalk.io" />
<link rel="help" href="/stable/htmldocs/" title="Documentation" />
<link rel="home" href="index.html" title="Netatalk Home" />
<link rel="home" href="https://github.com/Netatalk/netatalk" title="Netatalk GitHub" />
<link rel="bookmark" href="/stable/htmldocs/" title="Netatalk Documentation" />
<link rel="bookmark" href="https://github.com/Netatalk/netatalk/wiki" title="wiki" />
<link rel="bookmark" href="https://sourceforge.net/projects/netatalk/files/" title="Downloads" />
<link rel="icon" type="image/x-icon" href="/gfx/favicon.ico" />

<title>Netatalk - {page_title}</title>
</head>
"""

    with open(f"./public/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html_head)
        output_file.write(header)
        output_file.write(navbar)
        output_file.write(html)
        output_file.write(footer)

    print(f"Converted: {file}")
