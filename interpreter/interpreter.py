from nodes import (
    AddNode,
    AssignmentNode,
    MinusNode,
    Node,
    NumberNode,
    PlusNode,
    PowerNode,
    ValueAccessNode,
)

from .symbol_table import SymbolTable
from .values import Number


class Interpreter:
    __slots__ = "_symbol_table"

    def __init__(self) -> None:
        self._symbol_table = SymbolTable()

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
        except ZeroDivisionError:
            raise Exception("Runtime math error")

    def visit_ModuloNode(self, node: AddNode) -> Number:
        try:
            return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
        except ZeroDivisionError:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node: PowerNode) -> Number:
        value = self.visit(node.node).value
        if value < 0:
            raise Exception("Division by zero error")
        power = self.visit(node.power).value
        return Number(value ** power)

    def visit_PlusNode(self, node: PlusNode) -> Number:
        return self.visit(node.node)

    def visit_MinusNode(self, node: MinusNode) -> Number:
        return Number(-self.visit(node.node).value)

    def visit_ValueAccessNode(self, node: ValueAccessNode) -> Number:
        name = node.name
        value = self._symbol_table.get(name)
        if value is None:
            raise Exception(f"'{name}' is not defined")
        return value

    def visit_AssignmentNode(self, node: AssignmentNode) -> None:
        name = node.name
        value = self.visit(node.value)
        if self._symbol_table.get(name) is not None:
            raise Exception(f"'{name}' is already defined")
        self._symbol_table.set(name, value)
