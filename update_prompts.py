import glob
import re

prompt_new = "c1134czi5625@c5r4s7 ~ % "

for filepath in glob.glob("Log_4-*.md"):
    with open(filepath, "r") as f:
        content = f.read()
    
    # Replace "$ " at the beginning of any line
    new_content = re.sub(r'(?m)^\$ ', prompt_new, content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Updated {filepath}")

html_path = "app/index.html"
if glob.glob(html_path):
    with open(html_path, "r") as f:
        content = f.read()
    new_content = content.replace("dev@macbook ~ %", "c1134czi5625@c5r4s7 ~ %")
    if new_content != content:
        with open(html_path, "w") as f:
            f.write(new_content)
        print(f"Updated {html_path}")
