from markdown_to_html_node import markdown_to_html_node 
from extract import extract_title
import os 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)

    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
       file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        # If it's a directory → recurse
        if os.path.isdir(content_path):
            generate_pages_recursive(content_path, template_path, dest_path)

        # If it's a markdown file → generate page
        elif entry.endswith(".md"):
            html_filename = entry.replace(".md", ".html")
            dest_file_path = os.path.join(dest_dir_path, html_filename)

            generate_page(content_path, template_path, dest_file_path)