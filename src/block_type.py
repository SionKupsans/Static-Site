from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code" 
    QUOTE = "quote"
    UNORDERED = "unordered"
    ORDERED = "ordered"

def block_to_block_type(block):

    lines = block.split("\n")

    if lines[0].startswith("#"):
        count = 0 
        for char in lines[0]:
            if char == "#":
                count += 1 
            else:
                break
        if 1 <= count <= 6 and lines[0][count:].startswith(" "):
            return BlockType.HEADING
    

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if all(line.startswith(">") for line in lines):
       return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED
    
    is_ordered = True
    for i, line in enumerate(lines):
        expected = f"{i + 1}. "
        if not line.startswith(expected):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED 
    
    # Paragraph fallback 
    return BlockType.PARAGRAPH 

