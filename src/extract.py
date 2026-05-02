import re 
from markdown_to_blocks import markdown_to_blocks
from block_type import block_to_block_type , BlockType

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches 

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches 

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            count = 0
            for char in block:
                if char == "#":
                    count += 1
                else:
                    break

            if count == 1:
                title = block[count:].strip()
                return title 

    raise Exception("There is no title")