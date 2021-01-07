import sys
from typing import Callable, Tuple


def extended_gcd(a: int, b:int) -> Tuple[int, int, int]:
    x0, y0, x1, y1 = 1, 0, 0, 1  # type: int, int, int, int
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _mod_inverse(a: int, n: int) -> int:
    g, x, y = extended_gcd(a, n)
    if g != 1:
        raise ValueError("base is not invertible for the given modulus")
    else:
        return x % n


mod_inv: Callable[[int, int], int]

if sys.version_info.major == 3 and sys.version_info.minor >= 8:
    mod_inv = lambda x, n: pow(x, -1, n)
else:
    mod_inv = _mod_inverse