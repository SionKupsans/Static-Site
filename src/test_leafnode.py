import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_values(self):
        node = LeafNode("p", "I wish I could read")
        self.assertEqual(
            node.tag,
            "p",
        )
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = LeafNode("p", "Hello, world!", None)
        self.assertEqual(node.__repr__(), "LeafNode(p, Hello, world!, None)")


if __name__ == "__main__":
    unittest.main()
