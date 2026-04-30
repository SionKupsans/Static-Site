import unittest
from block_type import BlockType, block_to_block_type 

class TestBlockType(unittest.TestCase):
    def test_headings(self):
        block = "# Heading"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.HEADING)

    def test_code_blocks(self):
        block = "```\n variable = 6 ```"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.CODE)

    def test_quote_blocks(self):
        block = ">This is a quote\n>block"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Bulletpoint 1\n- Bulletpoint 2\n- Bulletpoint 3"

        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED)

    def test_ordered_lists(self):
        block = "1. This is\n2. An\n3. Ordered list"

        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED)

    def test_paragraph(self):
        block = "This is a paragraph"
        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()