import numpy as np

EMPTY_BUCKET = -1  # -1 is never returned by hash() in CPython
NULL = object()    # sentinel representing an empty slot


class HashTable:
    """Hash table backed by a numpy structured array of (hash: int64, value: object) rows.

    Uses linear probing on collision. Empty slots hold hash=-1 and value=NULL.
    Grows (doubles in size) when occupancy would exceed 2/3.
    """

    def __init__(self, size=8):
        self._len = 0
        self._table = self._make_table(size)

    def _make_table(self, size):
        table = np.empty(size, dtype=[('hash', np.int64), ('value', object)])
        table['hash'][:] = EMPTY_BUCKET
        table['value'][:] = NULL
        return table

    def _needs_space(self):
        """Return True if adding one item would push occupancy above 2/3."""
        return (self._len + 1) / len(self._table) > 2 / 3

    def add(self, item, grow=True):
        if item in self:
            return
        if grow and self._needs_space():
            self._grow()
        h = hash(item)
        idx = int(h % len(self._table))
        while self._table['value'][idx] is not NULL:
            idx = (idx + 1) % len(self._table)
        self._table['hash'][idx] = h
        self._table['value'][idx] = item
        self._len += 1

    def _grow(self):
        """Double the table size and re-insert all existing items."""
        current = self._table
        self._table = self._make_table(len(current) * 2)
        self._len = 0
        for row in current:
            if row['value'] is not NULL:
                self.add(row['value'], grow=False)

    def __contains__(self, item):
        idx = int(hash(item) % len(self._table))
        while self._table['value'][idx] is not NULL:
            if self._table['value'][idx] == item:
                return True
            idx = (idx + 1) % len(self._table)
        return False

    def __len__(self):
        return self._len

    def __iter__(self):
        for row in self._table:
            if row['value'] is not NULL:
                yield row['value']
