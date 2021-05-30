from programa import factorial
import pytest

l = [(0,1)]
for i in range(1, 171):
    n = 1
    for j in range(1, i+1):
        n *= j
    m = (i,n)
    l.append(m)

@pytest.mark.parametrize("z, y", l)

def test_factorial(z, y):
    assert factorial(z) == y