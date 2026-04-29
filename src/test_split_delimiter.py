import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitDelimiter(unittest.TestCase):
    
    def test_delimiter(self):
        node = TextNode("This is `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

        self.assertEqual(result[2].text, " here")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_bold_text(self):
        node = TextNode("Hello **world** today", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual([n.text for n in result], ["Hello ", "world", " today"])
        self.assertEqual([n.text_type for n in result], [TextType.TEXT, TextType.BOLD, TextType.TEXT])

    def test_missing_dilimiter_error(self):
        node = TextNode("This is `broken text", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertIn("Invalid Markdown", str(context.exception))

    def test_no_delimiter(self):
        node = TextNode("just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "just plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com)", 
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com")
            ],
            new_nodes,
        )

    def test_no_image(self):
        node = TextNode(
            "This is text without an image", 
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text without an image", TextType.TEXT)
            ],
            new_nodes, 
        )

    def test_no_link(self):
        node = TextNode(
            "This is text without a link", 
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text without a link", TextType.TEXT)
            ],
            new_nodes, 
        )


if __name__ == "__main__":
    unittest.main()