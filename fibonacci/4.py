#!/usr/bin/env python3
"""Print all Fibonacci numbers less than or equal to a user-supplied n."""

from collections.abc import Iterator


def fibonacci_up_to(limit: int) -> Iterator[int]:
    """Yield Fibonacci numbers in order while they are <= limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def read_non_negative_int(prompt: str) -> int:
    """Prompt until the user enters a non-negative integer."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print(f"'{raw}' is not a whole number. Try again.")
            continue
        if value < 0:
            print("Number must be 0 or greater. Try again.")
            continue
        return value


def main() -> int:
    try:
        n = read_non_negative_int("Enter n: ")
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return 1

    print(" ".join(map(str, fibonacci_up_to(n))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
