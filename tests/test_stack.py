"""Здесь надо написать тесты с использованием unittest для модуля stack."""

from src.stack import Stack, Node


def test_node():
    n1 = Node(5, None)
    n2 = Node('a', n1)
    assert n1.data == 5
    assert n2.data == 'a'
    assert n1.next_node is None
    assert n2.next_node == n1


def test_stack():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'
    assert stack.top.next_node.next_node.data == 'data1'
    assert stack.top.next_node.next_node.next_node is None
    stack.pop()
    assert stack.top.data == 'data2'
    stack.pop()
    assert stack.top.data == 'data1'
    stack.pop()
    assert stack.top.data is None
