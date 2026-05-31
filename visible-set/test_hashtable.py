import pytest
from hashtable import HashTable, EMPTY_HASH, NULL


def test_default_size():
    ht = HashTable()
    assert len(ht._table) == 8


def test_custom_size():
    ht = HashTable(size=16)
    assert len(ht._table) == 16


def test_add_and_len():
    ht = HashTable()
    ht.add('a')
    ht.add('b')
    ht.add('c')
    assert len(ht) == 3


def test_add_duplicate_ignored():
    ht = HashTable()
    ht.add('x')
    ht.add('x')
    assert len(ht) == 1


def test_contains_true():
    ht = HashTable()
    ht.add(42)
    assert 42 in ht


def test_contains_false():
    ht = HashTable()
    ht.add(42)
    assert 99 not in ht


def test_contains_empty():
    ht = HashTable()
    assert 'anything' not in ht


def test_grow_doubles_capacity():
    ht = HashTable()
    old_capacity = len(ht._table)
    ht._grow()
    assert len(ht._table) == old_capacity * 2


def test_grow_preserves_items():
    ht = HashTable()
    items = ['a', 'b', 'c']
    for item in items:
        ht.add(item)
    ht._grow()
    assert len(ht) == len(items)
    assert set(ht) == set(items)


def test_add_triggers_grow():
    ht = HashTable()
    for i in range(5):  # 5/8 = 62.5%, just under 2/3
        ht.add(i)
    assert len(ht._table) == 8
    ht.add(5)  # 6/8 = 75% > 2/3, triggers grow
    assert len(ht._table) == 16
    assert set(ht) == set(range(6))


def test_find_returns_hash_and_slot_for_present_item():
    ht = HashTable()
    ht.add('hello')
    h, idx = ht._find('hello')
    assert h is not EMPTY_HASH
    assert ht._table['value'][idx] == 'hello'


def test_find_returns_no_hash_and_empty_slot_for_absent_item():
    ht = HashTable()
    ht.add('hello')
    h, idx = ht._find('world')
    assert h is EMPTY_HASH
    assert ht._table['value'][idx] is NULL


def test_find_on_empty_table():
    ht = HashTable()
    h, idx = ht._find(42)
    assert h is EMPTY_HASH
    assert idx == hash(42) % len(ht._table)


def test_find_idx_is_insertion_point_when_not_found():
    ht = HashTable()
    item = 'new'
    h, idx = ht._find(item)
    assert h is EMPTY_HASH
    ht.add(item)
    h2, idx2 = ht._find(item)
    assert h2 is not EMPTY_HASH
    assert idx == idx2  # same slot used for insertion
    assert h2 == hash(item)
