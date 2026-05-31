import numpy as np

DEFAULT_SIZE = 8
EMPTY_HASH = -1  # -1 is never returned by hash() in CPython
NULL = object()  # sentinel representing an empty slot


class HashTable:
    """Hash table backed by a numpy structured array of (hash: int64, value: object) rows.

    Uses linear probing on collision. Empty slots hold hash=-1 and value=NULL.
    Doubles in size when adding item, if occupancy would exceed 2/3.
    """

    def __init__(self, size=DEFAULT_SIZE):
        self._item_count = 0
        self._table = self._make_table(size)

    def _make_table(self, size):
        table = np.empty(size, dtype=[('hash', np.int64), ('value', object)])
        table['hash'][:] = EMPTY_HASH
        table['value'][:] = NULL
        return table
    
    def size(self):
        return len(self._table)

    def add(self, item, grow=True):
        h, offset = self._find(item)
        if h is EMPTY_HASH:
            if grow and self._needs_space():
                self._grow()
                h2, offset = self._find(item)
                assert h2 is EMPTY_HASH
            self._table['hash'][offset] = hash(item)
            self._table['value'][offset] = item
            self._item_count += 1

    def _needs_space(self):
        """Return True if adding one item would push occupancy above 2/3."""
        return (self._item_count + 1) / len(self._table) > 2 / 3

    def _grow(self):
        """Double the table size and re-insert all existing items."""
        current = self._table
        self._table = self._make_table(len(current) * 2)
        self._item_count = 0
        for row in current:
            if row['value'] is not NULL:
                self.add(row['value'], grow=False)

    def _find(self, item):
        """Linear probe for item; return (hash, offset).

        If found, hash is item's hash and offset is its row.
        If not found, hash is EMPTY_HASH and offset is the first empty row.
        """
        h = hash(item)
        offset = h % len(self._table)
        while self._table['value'][offset] is not NULL:
            if self._table['value'][offset] == item:
                return h, offset
            offset = (offset + 1) % len(self._table)
        return EMPTY_HASH, offset

    def __contains__(self, item):
        h, _ = self._find(item)
        return h is not EMPTY_HASH


    def __len__(self):
        return self._item_count

    def __iter__(self):
        for row in self._table:
            if row['value'] is not NULL:
                yield row['value']
