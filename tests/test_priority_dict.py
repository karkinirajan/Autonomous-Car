import pytest
from priority_dict import priority_dict


def test_smallest_and_pop_order():
    pd = priority_dict({"a": 3, "b": 1, "c": 2})
    assert pd.smallest() == ("b", 1)
    assert [pd.pop_smallest()[0] for _ in range(3)] == ["b", "c", "a"]


def test_priority_update():
    pd = priority_dict({"a": 3, "b": 1})
    pd["a"] = 0
    assert pd.smallest() == ("a", 0)


def test_empty_raises():
    with pytest.raises(IndexError):
        priority_dict().smallest()


def test_sorted_iter_drains():
    pd = priority_dict({"x": 2, "y": 1})
    assert list(pd.sorted_iter()) == [("y", 1), ("x", 2)]
    assert len(pd) == 0
