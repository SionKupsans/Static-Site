from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode Value is empty")

        if self.tag is None:
            return self.value

        props_str = ""
        if self.props:
            props_str = " " + " ".join(
                f'{key}="{value}"' for key, value in self.props.items()
            )

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
