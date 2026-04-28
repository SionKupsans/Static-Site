import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node_one = LeafNode("b", "child_one")
        child_node_two = LeafNode("div", "child_two")
        child_node_three = LeafNode("p", "child_three")
        parent_node = ParentNode(
            "div", [child_node_one, child_node_two, child_node_three]
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child_one</b><div>child_two</div><p>child_three</p></div>",
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()

        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_values(self):
        parent_node = ParentNode("Div", None, None)
        self.assertEqual(
            parent_node.tag,
            "Div",
        )
        self.assertEqual(
            parent_node.children,
            None,
        )
        self.assertEqual(
            parent_node.props,
            None,
        )
