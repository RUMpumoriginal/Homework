import pytest
from shop import discount


def test_discount_10_percent():
    assert discount(100, 10) == 90
    assert discount(100, 0) == 100

with pytest.raises(ValueError):
        discount(100, 150)

test_discount_10_percent()
