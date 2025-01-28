VERSION = "4.1.1"
LOCALES = ["en", "ja"]

# Netatalk releases 2023 onward which have release notes on GitHub.
# Earlier versions have static release notes html pages.
RELEASENOTES = [
    "2.2.7",
    "2.2.8",
    "2.2.9",
    "2.2.10",
    "2.3.0",
    "2.3.1",
    "2.3.2",
    "2.4.0",
    "2.4.1",
    "2.4.2",
    "2.4.3",
    "2.4.4",
    "2.4.5",
    "2.4.6",
    "2.4.7",
    "2.4.8",
    "2.4.9",
    "2.4.10",
    "3.1.14",
    "3.1.15",
    "3.1.16",
    "3.1.17",
    "3.1.18",
    "3.1.19",
    "3.2.0",
    "3.2.1",
    "3.2.2",
    "3.2.3",
    "3.2.4",
    "3.2.5",
    "3.2.6",
    "3.2.7",
    "3.2.8",
    "3.2.9",
    "3.2.10",
    "4.0.0",
    "4.0.1",
    "4.0.2",
    "4.0.3",
    "4.0.4",
    "4.0.5",
    "4.0.6",
    "4.0.7",
    "4.0.8",
    "4.1.0",
    "4.1.1",
]

def html_head(title, path, lang="en"):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="Netatalk Wiki">
    <link rel="canonical" href="https://netatalk.io/{path}">
    <link rel="stylesheet" type="text/css" href="https://netatalk.io/css/site.css">
    <link rel="icon" type="image/x-icon" href="https://netatalk.io/gfx/favicon.ico">
</head>
"""

def html_foot(path):
    return f"""
<div class="footer">
    <a href="https://validator.nu/?doc=https://netatalk.io/{path}">
      <img style="border:0;width:88px;height:31px"
      src="https://raw.githubusercontent.com/bradleytaunt/html5-valid-badge/refs/heads/master/html5-validator-badge.svg"
      alt="Valid HTML5">
    </a>
    <a href="https://validator.nu/?doc=https://netatalk.io/{path}">
      <img style="border:0;width:88px;height:31px"
      src="https://www.w3.org/Icons/valid-css-v.svg" alt="Valid CSS">
    </a>
    <p>Netatalk and the Netatalk website are licensed under the <a href="/stable/htmldocs/gpl">GNU
    General Public License 2.0</a>.</p>
</div>
</body>
</html>
"""
