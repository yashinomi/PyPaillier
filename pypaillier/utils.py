import math
import sys
import secrets
from typing import Callable, Dict, Tuple


def lcm(x: int, y: int) -> int:
    return x * y // math.gcd(x, y)


def _extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Calculates extended gcd. Only used to calculate the modulo inverse.

    Parameters
    ----------
    a : int
    b : int
    """
    x0, y0, x1, y1 = 1, 0, 0, 1  # type: int, int, int, int
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _mod_inverse(a: int, n: int) -> int:
    """
    A fallback to calculate the modulo inverse when the version of python is less than 3.8.

    Parameters
    ----------
    a : int
        The number you want the inverse for.
    n : int
        modulo

    Returns
    -------
    int
        The modulo inverse.
    """
    g, x, y = _extended_gcd(a, n)
    if g != 1:
        raise ValueError("base is not invertible for the given modulus")
    else:
        return x % n


def safe_random_below(upper_bound: int, num_safe_for: int = -1) -> int:
    """
    Picks a random number `r` from [0, `upper_bound`) that satisfies `gcd(r, num_safe_for) == 1`
    and is cryptographically secure.

    Parameters
    ----------
    upper_bound :  int
        An upper_bound to choose the random number from.

    num_safe_for : int, optional
        Uses to calculate gcd.

    Returns
    -------
    r : int
        A cryptographically secure pseudo random number.
    """
    if num_safe_for < 0:
        num_safe_for = upper_bound
    r: int = secrets.randbelow(upper_bound)
    while math.gcd(r, num_safe_for) != 1:
        r: int = secrets.randbelow(upper_bound)

    return r


if sys.version_info.major == 3 and sys.version_info.minor >= 8:
    mod_inv: Callable[[int, int], int] = lambda a, n: pow(a, -1, n)
else:
    mod_inv: Callable[[int, int], int] = _mod_inverse
