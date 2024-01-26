import os

files = []

for file in os.listdir("./"):
    if file.endswith(".in"):
        files.append(f"{file}")
with open("./header.html.tmpl", "r", encoding="utf-8") as header_file:
    header = header_file.read()
with open("./footer.html.tmpl", "r", encoding="utf-8") as footer_file:
    footer = footer_file.read()
for file in files:
    with open(f"./{file}", "r", encoding="utf-8") as input_file:
        html = input_file.read()
    new_name = file.replace('.html.in', '.html')

    with open(f"./public/{new_name}", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(header)
        output_file.write(html)
        output_file.write(footer)

    print(f"Converted: {file}")

