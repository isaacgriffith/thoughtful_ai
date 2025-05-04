import pytest
from thoughtful_sort.sort import sort

def test_standard_package():
    # Test a standard package (not bulky or heavy)
    assert sort(10, 10, 10, 10) == "STANDARD"
    assert sort(100, 100, 10, 10) == "STANDARD"

def test_special_bulky_volume():
    # Test a bulky package (volume > 1,000,000)
    assert sort(100, 100, 100, 10) == "SPECIAL"  # 1,000,000 volume
    assert sort(100, 100, 101, 10) == "SPECIAL"  # 1,010,000 volume

def test_special_bulky_dimension():
    # Test a bulky package (any dimension > 150)
    assert sort(151, 10, 10, 10) == "SPECIAL"
    assert sort(10, 151, 10, 10) == "SPECIAL"
    assert sort(10, 10, 151, 10) == "SPECIAL"

def test_special_heavy():
    # Test a heavy package (mass > 20)
    assert sort(10, 10, 10, 21) == "SPECIAL"
    assert sort(10, 10, 10, 30) == "SPECIAL"

def test_rejected_volume_and_heavy():
    # Test a package that is both bulky (volume) and heavy
    assert sort(100, 100, 100, 21) == "REJECTED"
    assert sort(200, 200, 200, 30) == "REJECTED"

def test_rejected_dimension_and_heavy():
    # Test a package that is both bulky (dimension) and heavy
    assert sort(151, 10, 10, 21) == "REJECTED"
    assert sort(10, 151, 10, 21) == "REJECTED"
    assert sort(10, 10, 151, 21) == "REJECTED"

def test_invalid_dimensions():
    # Test negative dimensions
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 10)
    with pytest.raises(ValueError):
        sort(10, -1, 10, 10)
    with pytest.raises(ValueError):
        sort(10, 10, -1, 10)
    with pytest.raises(ValueError):
        sort(10, 10, 10, -1) 