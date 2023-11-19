"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue


class Testqueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        self.assertEqual(str(Queue()), "")
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(str(queue), "data1\ndata2\ndata3")

