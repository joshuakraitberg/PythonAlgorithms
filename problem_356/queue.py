from typing import Any


class QueueEmpty(IndexError):
    pass


class InvalidFixedLength(ValueError):
    pass


class Queue(object):

    """A queue (FIFO) using a set of fixed-length `arrays`.

    Supports `enqueue`, `dequeue`, and `get_size` operations.
    """

    def __init__(self, fixed_length: int):
        """
        :param fixed_length: Length of internal fixed-length arrays
        """

        try:
            fixed_length = int(fixed_length)
        except ValueError:
            raise InvalidFixedLength(f"Queue could not covert {fixed_length} to valid fixed-length")
        except TypeError:
            raise InvalidFixedLength(f"Queue does not accept {type(fixed_length)}")

        if fixed_length <= 0:
            raise InvalidFixedLength(f"Fixed-length must be greater than 0, got: {fixed_length}")

        self._arrays = []
        self._fixed_length = fixed_length

        # Index to enqueue on
        self._enqueue_idx = fixed_length

        # Index to dequeue from
        self._dequeue_idx = 0

        # Number of elements
        self._count = 0

    @property
    def fixed_length(self):
        """Fixed length used by arrays"""
        return self._fixed_length

    @property
    def n_arrays(self):
        """Number of fixed length arrays in-use"""
        return len(self._arrays)

    def enqueue(self, item: Any):
        """Puts an object onto end of queue"""

        # Allocate new array if needed
        if self._enqueue_idx >= self._fixed_length:
            self._enqueue_idx = 0
            self._arrays.append([None] * self._fixed_length)

        # Enqueue data
        self._arrays[-1][self._enqueue_idx] = item
        self._enqueue_idx += 1
        self._count += 1

    def dequeue(self) -> Any:
        """Pops the object from start of queue"""

        # Size guard
        if self._count <= 0:
            raise QueueEmpty("Cannot dequeue while empty")

        # Remove dequeue array if exhausted
        if self._dequeue_idx >= self._fixed_length:
            self._dequeue_idx = 0
            self._arrays = self._arrays[1:]

        # Get first item
        item = self._arrays[0][self._dequeue_idx]
        self._dequeue_idx += 1
        self._count -= 1

        # Reset original array if empty
        if self._count == 0:
            self._enqueue_idx = 0
            self._dequeue_idx = 0
            self._arrays = self._arrays[:1]

        return item

    def get_size(self) -> int:
        """Returns current size of queue"""
        return self._count
