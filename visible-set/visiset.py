import numpy as np


class VisiSet:
    """Set backed by a numpy structured array of (hash: uint64, value: object) rows."""

    _dtype = np.dtype([('hash', np.uint64), ('value', object)])

    def __init__(self, iterable=()):
        self._data = np.empty(0, dtype=self._dtype)
        for item in iterable:
            self.add(item)

    # ---- set interface -------------------------------------------------------

    def add(self, item):
        if item in self:
            return
        h = hash(item) & 0xFFFF_FFFF_FFFF_FFFF
        row = np.array([(h, item)], dtype=self._dtype)
        self._data = np.append(self._data, row)

    def __contains__(self, item):
        return bool(np.any(self._data['value'] == item))

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data['value'])

    # ---- display -------------------------------------------------------------

    def __repr__(self):
        items = ', '.join(repr(v) for v in self._data['value'])
        return f'VisiSet({{{items}}})'

    _CSS = """
    <style>
    .vs-wrap { font-family: monospace; font-size: 13px; }
    .vs-wrap .vs-title { color: #555; margin-bottom: 2px; }
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
    .vs-dtype { color: #888; margin-top: 3px; }
    </style>
    """

    def _repr_html_(self):
        rows = []
        for row in self._data:
            h = f"{int(row['hash']):016x}"
            v = repr(row['value'])
            rows.append(f"<tr><td>{h}</td><td>─→&nbsp;{v}</td></tr>")
        dtype_str = "dtype=[('hash', '&lt;u8'), ('value', 'O')]"
        return (
            self._CSS
            + "<div class='vs-wrap'>"
            + "<table class='vs-table'>"
            + "<thead><tr><th>hash</th><th>value</th></tr></thead>"
            + "<tbody>" + "".join(rows) + "</tbody>"
            + "</table>"
            + "</div>"
        )
