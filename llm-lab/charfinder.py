#!/usr/bin/env python3
"""Search Unicode characters by the words in their names.

A character matches when every word of the query appears as a whole word
in its name. Hyphens separate words on both sides, so the name
HYPHEN-MINUS is the word set {HYPHEN, MINUS} and is found by 'minus',
by 'hyphen', and by 'hyphen-minus' -- but not by 'hyp'.
"""

import sys
import unicodedata
from collections.abc import Iterator, Sequence

FIRST, LAST = 32, sys.maxunicode  # start at 32 to skip the control characters


def tokenize(text: str) -> set[str]:
    """The set of uppercase words in text, splitting on spaces and hyphens."""
    return set(text.upper().replace('-', ' ').split())


def format_codepoint(codepoint: int) -> str:
    """Codepoint in U+XXXX notation: uppercase hex, at least 4 digits."""
    return f'U+{codepoint:04X}'


def find_chars(args: Sequence[str]) -> Iterator[tuple[int, str, str]]:
    """Yield (codepoint, char, name) for each match, in codepoint order."""
    query = tokenize(' '.join(args))
    for codepoint in range(FIRST, LAST + 1):
        char = chr(codepoint)
        name = unicodedata.name(char, '')
        if name and query <= tokenize(name):
            yield codepoint, char, name


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(f'Usage: {sys.argv[0]} WORD [WORD ...]', file=sys.stderr)
        return 1
    count = 0
    for codepoint, char, name in find_chars(args):
        print(f'{format_codepoint(codepoint)}\t{char}\t{name}')
        count += 1
    noun = 'character' if count == 1 else 'characters'
    print(f'({count} {noun} found)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
