#!/usr/bin/env python3
"""Generate all Fibonacci numbers less than or equal to a given limit."""

from __future__ import annotations

import sys
from collections.abc import Iterator

__all__ = ["fibonacci_up_to", "fibonacci_list"]


def _validate(n: object) -> int:
    """Return ``n`` if it is a non-negative ``int``, else raise.

    Raises:
        TypeError: If ``n`` is not an ``int`` (``bool`` is rejected too).
        ValueError: If ``n`` is negative.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"n must be an int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    return n


def _generate(limit: int) -> Iterator[int]:
    """Yield Fibonacci numbers in order while they are <= ``limit``."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def fibonacci_up_to(n: int) -> Iterator[int]:
    """Lazily yield every Fibonacci number <= ``n``, in ascending order.

    Arguments are validated immediately, when the function is called,
    rather than on the first ``next()``.

    Complexity:
        Time:  O(log n) iterations, since F(k) grows as phi**k. This is
               well within an O(n) bound. Big-int additions add a small
               extra cost for very large ``n``.
        Space: O(1) auxiliary space (two integers).

    Args:
        n: Inclusive upper bound. Must be a non-negative ``int``.

    Returns:
        An iterator of ints.

    Raises:
        TypeError: If ``n`` is not an ``int``.
        ValueError: If ``n`` is negative.

    Examples:
        >>> list(fibonacci_up_to(10))
        [0, 1, 1, 2, 3, 5, 8]
        >>> list(fibonacci_up_to(0))
        [0]
        >>> list(fibonacci_up_to(1))
        [0, 1, 1]
        >>> list(fibonacci_up_to(-1))
        Traceback (most recent call last):
            ...
        ValueError: n must be non-negative, got -1
        >>> list(fibonacci_up_to(2.5))
        Traceback (most recent call last):
            ...
        TypeError: n must be an int, got float
    """
    return _generate(_validate(n))


def fibonacci_list(n: int) -> list[int]:
    """Return every Fibonacci number <= ``n`` as a list.

    Complexity:
        Time:  O(log n).
        Space: O(log n) for the returned list.

    Raises:
        TypeError: If ``n`` is not an ``int``.
        ValueError: If ``n`` is negative.

    Examples:
        >>> fibonacci_list(50)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    return list(fibonacci_up_to(n))


def main() -> int:
    """Command-line entry point. Returns a process exit code."""
    try:
        raw = input("Enter n: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.", file=sys.stderr)
        return 130

    try:
        n = int(raw)
        print(*fibonacci_up_to(n))
    except ValueError as exc:
        # int() failures and negative-number errors both land here.
        msg = str(exc) if "n must" in str(exc) else f"{raw!r} is not a whole number"
        print(f"Error: {msg}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
