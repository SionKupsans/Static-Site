import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes 


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node3 = TextNode("This is not a node", TextType.BOLD)
        node4 = TextNode("This is not a node", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

    def test_eq_url(self):
        node5 = TextNode("Test case", TextType.ITALIC, "www.boot.dev")
        node6 = TextNode("Test case", TextType.ITALIC, "www.boot.dev")
        self.assertEqual(node5, node6)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "some_url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "some_url"})

    def test_image(self):
        node = TextNode("alt text here", TextType.IMAGE, "some_image_url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "alt text here")
        self.assertEqual(
            html_node.props, {"src": "some_image_url", "alt": "alt text here"}
        )


    def test_text_to_textnode(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        nodes = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(len(nodes), len(expected))

        for i in range(len(nodes)):
            self.assertEqual(nodes[i].text, expected[i].text)
            self.assertEqual(nodes[i].text_type, expected[i].text_type)
            self.assertEqual(nodes[i].url, expected[i].url)

if __name__ == "__main__":
    unittest.main()
