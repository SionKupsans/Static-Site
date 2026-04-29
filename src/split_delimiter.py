from textnode import TextType , TextNode
from extract_links import extract_markdown_images, extract_markdown_links 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        # If not plain text, keep as is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node) 
            continue 

        text = node.text

        # Validation - must have matching delimiters
        if text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown: missing closing delimiter")
       
        # Split text
        parts = text.split(delimiter)

        # Rebuild notes
        for idx, part in enumerate(parts):
            if idx % 2 == 0:
                text_node = TextNode(part, TextType.TEXT)
                new_nodes.append(text_node)
            else: 
                text_node = TextNode(part, text_type)
                new_nodes.append(text_node)

    return new_nodes 

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # If not plain text, keep as is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node) 
            continue 

        text = node.text 

        if text == "":
            continue 

        images = extract_markdown_images(text)

        # No images → keep original
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = text 

        for alt, url in images:
            pattern = f"![{alt}]({url})"
            parts = remaining_text.split(pattern, 1)

            # text before image
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            remaining_text = parts[1]

        # leftover text
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))


    return new_nodes 

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # If not plain text, keep as is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node) 
            continue 

        text = node.text 

        if text == "":
            continue 

        links = extract_markdown_links(text)

        # No links → keep original
        if not links:
            new_nodes.append(node)
            continue

        remaining_text = text 

        for alt, url in links:
            pattern = f"[{alt}]({url})"
            parts = remaining_text.split(pattern, 1)

            # text before image
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # link node
            new_nodes.append(TextNode(alt, TextType.LINK, url))

            remaining_text = parts[1]

        # leftover text
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))


    return new_nodes 