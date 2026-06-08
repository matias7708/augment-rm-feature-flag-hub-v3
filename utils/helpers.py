# Shared helpers
from typing import Iterable

def take(it: Iterable, n: int) -> list:
    out = []
    for i, x in enumerate(it):
        if i >= n:
            break
        out.append(x)
    return out
