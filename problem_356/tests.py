import operator
from math import ceil
from typing import Any, Iterator

import pytest

from queue import Queue, QueueEmpty, InvalidFixedLength

REPEAT = 100


class QueueTester(object):
    RANGE_MULTIPLIER = 10

    def __init__(self, queue: Queue):
        self.queue: Queue = queue

    def get_sample_space(self, start=1, modifier=RANGE_MULTIPLIER):
        return range(start, self.queue.fixed_length * modifier + start)

    def assert_n_array(self, val=0):
        assert (
                self.queue.n_arrays == val and 0 <= val <= 1 or
                self.queue.n_arrays == ceil(self.queue.get_size() / self.queue.fixed_length) or
                self.queue.get_size() % self.queue.fixed_length == 0 and
                self.queue.n_arrays - 1 == ceil(self.queue.get_size() / self.queue.fixed_length)
        )

    def assert_get_size(self, func=operator.eq, val=0):
        assert func(self.queue.get_size(), val)

    def _assert_enqueue(self, item):
        self.queue.enqueue(item)

    def assert_enqueue(self, item=None):
        size = self.queue.get_size() + 1
        self._assert_enqueue(item)
        assert self.queue.get_size() == size
        self.assert_n_array()

    def _assert_dequeue(self, item):
        assert self.queue.dequeue() == item

    def assert_dequeue(self, item=None):
        size = self.queue.get_size() - 1
        self._assert_dequeue(item)
        assert self.queue.get_size() == size
        self.assert_n_array()

    def assert_failed_dequeue(self):
        with pytest.raises(QueueEmpty):
            self.queue.dequeue()

    def assert_many_enqueues(self, items: Iterator[Any] = ()):
        for item in items:
            self.assert_enqueue(item)

    def assert_many_dequeues(self, items: Iterator[Any] = ()):
        for item in items:
            self.assert_dequeue(item)


@pytest.fixture(scope="function", params=[1, 10, 114.6, "1421"])
def queue(request):
    queue = Queue(request.param)
    assert queue.fixed_length == int(request.param)
    return queue


@pytest.fixture(scope="function")
def tester(queue):
    tester = QueueTester(queue)
    tester.assert_n_array()
    tester.assert_get_size()
    tester.assert_failed_dequeue()
    yield tester


@pytest.mark.parametrize(
    "fixed_length",
    (-1, 0, 0.9999, -14.0, "-142", pytest.param(10j, id="10j"), "beef", pytest)
)
def test_fixed_length_value_errors(fixed_length: Any):
    with pytest.raises(InvalidFixedLength):
        _ = Queue(fixed_length)


def test_enqueue(tester: QueueTester):
    tester.assert_enqueue()


def test_dequeue(tester: QueueTester):
    tester.assert_enqueue()
    tester.assert_dequeue()
    tester.assert_failed_dequeue()


def test_many_enqueues(tester: QueueTester):
    items = tester.get_sample_space()
    tester.assert_many_enqueues(items)


def test_many_dequeues(tester: QueueTester):
    items = tester.get_sample_space()
    tester.assert_many_enqueues(items)
    tester.assert_many_dequeues(items)
    tester.assert_failed_dequeue()


def test_one_on_one_off(tester: QueueTester):
    for item in tester.get_sample_space():
        tester.assert_enqueue(item)
        tester.assert_dequeue(item)
    tester.assert_failed_dequeue()
