class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # CASE 1: No tag (just raw text node)
        if self.tag is None:
            return self.value or ""

        # CASE 2: Leaf node (no children)
        if not self.children:
            if self.tag == "img":
                alt = self.props.get("alt", "")
                src = self.props.get("src", "")
                return f'<img src="{src}" alt="{alt}">'
        
            if self.tag == "a":
                href = self.props.get("href", "")
                return f'<a href="{href}">{self.value or ""}</a>'

            return f"<{self.tag}>{self.value or ''}</{self.tag}>"

        # CASE 3: Parent node (has children)
        inner_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}>{inner_html}</{self.tag}>"

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
