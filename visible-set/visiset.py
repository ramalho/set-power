import numpy as np

EMPTY_BUCKET = -1  # -1 is never returned by hash() in CPython
NULL = object()  # sentinel representing a null pointer


class VisiSet:
    """Set backed by a numpy structured array of (hash: int64, value: object) rows.

    Emulates CPython's set hash table: 8 initial slots, linear probing on collision.
    Empty slots hold hash=-1 and value=NULL.
    """

    _dtype = np.dtype([('hash', np.int64), ('value', object)])
    _INIT_SIZE = 8

    def __init__(self, iterable=()):
        self._data = np.empty(self._INIT_SIZE, dtype=self._dtype)
        self._data['hash'][:] = EMPTY_BUCKET
        self._data['value'][:] = NULL
        self._len = 0
        for item in iterable:
            self.add(item)

    # ---- set interface -------------------------------------------------------

    def add(self, item):
        if item in self:
            return
        h = hash(item)
        idx = int(h % len(self._data))
        while self._data['value'][idx] is not NULL:
            idx = (idx + 1) % len(self._data)
        self._data['hash'][idx] = h
        self._data['value'][idx] = item
        self._len += 1

    def __contains__(self, item):
        idx = int(hash(item) % len(self._data))
        while self._data['value'][idx] is not NULL:
            if self._data['value'][idx] == item:
                return True
            idx = (idx + 1) % len(self._data)
        return False

    def __len__(self):
        return self._len

    def __iter__(self):
        for row in self._data:
            if row['value'] is not NULL:
                yield row['value']

    # ---- display -------------------------------------------------------------

    def __repr__(self):
        items = ', '.join(repr(v) for v in self)
        return f'VisiSet({{{items}}})'

    _CSS = """
    <style>
    .vs-wrap { font-family: monospace; font-size: 13px; }
    .vs-table {
        border-collapse: collapse;
        font-family: monospace;
        font-size: 13px;
    }
    .vs-table th {
        background: #2b2b2b;
        color: #ddd;
        padding: 3px 14px 3px 6px;
        text-align: right;
        font-weight: normal;
        border: 1px solid #444;
    }
    .vs-table td {
        padding: 2px 14px 2px 6px;
        text-align: right;
        border: 1px solid #ccc;
    }
    .vs-table tr:nth-child(odd) td { background: #f9f9f9; }
    .vs-table tr.vs-empty td { color: #bbb; background: #fafafa; }
    </style>
    """

    def _repr_html_(self):
        rows = []
        n = len(self._data)
        for row in self._data:
            h = int(row['hash'])
            if row['value'] is NULL:
                rows.append(
                    f"<tr class='vs-empty'><td>{h}</td><td></td><td>NULL</td></tr>"
                )
            else:
                slot = int(row['hash']) % n
                v = repr(row['value'])
                rows.append(f"<tr><td>{h}</td><td>{slot}</td><td>{v}</td></tr>")
        return (
            self._CSS
            + "<div class='vs-wrap'>"
            + "<table class='vs-table'>"
            + "<thead><tr><th>hash</th><th>%</th><th>value</th></tr></thead>"
            + "<tbody>" + "".join(rows) + "</tbody>"
            + "</table>"
            + "</div>"
        )
