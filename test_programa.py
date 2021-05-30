from programa import factorial
import pytest

l = [(0,1)]
for i in range(1, 171):
    n = l[i-1][1] * i
    l.append((i, n))

@pytest.mark.parametrize("z, y", l)

def test_factorial(z, y):
    assert factorial(z) == y