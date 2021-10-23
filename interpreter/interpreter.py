from nodes import AddNode, MinusNode, Node, NumberNode, PlusNode
from .values import Number


class Interpreter:
    __slots__ = "_tree"

    def visit(self, node: Node) -> Number:
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node: NumberNode) -> Number:
        return Number(node.value)

    def visit_AddNode(self, node: AddNode) -> Number:
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node: AddNode) -> Number:
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node: AddNode) -> Number:
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node: AddNode) -> Number:
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_PlusNode(self, node: PlusNode) -> Number:
        return self.visit(node.node)

    def visit_MinusNode(self, node: MinusNode) -> Number:
        return Number(-self.visit(node.node).value)

