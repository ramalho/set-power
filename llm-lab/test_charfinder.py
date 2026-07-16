#!/usr/bin/env python3
"""Tests for charfinder."""

import subprocess
import sys
from pathlib import Path

from charfinder import find_chars, format_codepoint, main, tokenize


def codepoints(*args):
    """Codepoints found for the given CLI arguments."""
    return [cp for cp, _char, _name in find_chars(args)]


# ---------- tokenize ----------

def test_tokenize_single_word():
    assert tokenize('cat') == {'CAT'}


def test_tokenize_uppercases():
    assert tokenize('Cat FaCe') == {'CAT', 'FACE'}


def test_tokenize_splits_hyphenated_word():
    assert tokenize('hyphen-minus') == {'HYPHEN', 'MINUS'}


def test_tokenize_splits_on_whitespace_and_hyphens():
    assert tokenize('cat-face smiling') == {'CAT', 'FACE', 'SMILING'}


def test_tokenize_empty_string():
    assert tokenize('') == set()


# ---------- format_codepoint ----------

def test_format_codepoint_pads_to_four_digits():
    assert format_codepoint(0x41) == 'U+0041'


def test_format_codepoint_exactly_four_digits():
    assert format_codepoint(0x2013) == 'U+2013'


def test_format_codepoint_five_digits_not_padded_to_six():
    assert format_codepoint(0x1F431) == 'U+1F431'


def test_format_codepoint_six_digits():
    assert format_codepoint(0x10FFFF) == 'U+10FFFF'


def test_format_codepoint_hex_is_uppercase():
    assert format_codepoint(0x1F4A9) == 'U+1F4A9'


# ---------- find_chars: whole-word matching ----------

def test_find_matches_whole_name():
    assert 0x1F408 in codepoints('cat')  # CAT


def test_find_matches_word_within_name():
    assert 0x1F431 in codepoints('cat')  # CAT FACE


def test_find_does_not_match_substring_of_a_word():
    # MULTIPLICATION SIGN contains 'cat' as a substring, but not as a word.
    assert 0x00D7 not in codepoints('cat')


def test_find_requires_every_query_word():
    found = codepoints('cat', 'face')
    assert 0x1F431 in found      # CAT FACE
    assert 0x1F408 not in found  # CAT -- has no FACE


def test_find_word_order_does_not_matter():
    assert codepoints('face', 'cat') == codepoints('cat', 'face')


def test_find_is_case_insensitive():
    assert codepoints('CAT', 'FaCe') == codepoints('cat', 'face')


def test_find_no_match_returns_nothing():
    assert codepoints('zzzznotaword') == []


# ---------- find_chars: hyphens ----------

def test_find_splits_hyphen_in_the_name():
    # U+002D is named HYPHEN-MINUS, so 'minus' alone must find it.
    assert 0x002D in codepoints('minus')


def test_find_bare_word_matches_both_sides_of_a_hyphenated_name():
    found = codepoints('hyphen')
    assert 0x2010 in found  # HYPHEN
    assert 0x002D in found  # HYPHEN-MINUS


def test_find_splits_hyphenated_query_into_two_words():
    found = codepoints('hyphen-minus')
    assert 0x002D in found      # HYPHEN-MINUS
    assert 0x2010 not in found  # HYPHEN -- has no MINUS


def test_find_hyphenated_query_equals_two_separate_args():
    assert codepoints('hyphen-minus') == codepoints('hyphen', 'minus')


# ---------- find_chars: results ----------

def test_find_yields_codepoint_char_and_name():
    assert (0x002D, '-', 'HYPHEN-MINUS') in list(find_chars(['hyphen-minus']))


def test_find_results_ascend_by_codepoint():
    found = codepoints('cat', 'face')
    assert found == sorted(found)


def test_find_finds_astral_characters():
    assert 0x101EC in codepoints('phaistos', 'disc', 'sign', 'cat')


# ---------- main: output format ----------

def test_main_line_is_tab_delimited(capsys):
    main(['registered', 'sign'])
    first_line = capsys.readouterr().out.splitlines()[0]
    assert first_line == 'U+00AE\t®\tREGISTERED SIGN'


def test_main_singular_count_message(capsys):
    main(['registered', 'sign'])
    assert capsys.readouterr().out.splitlines()[-1] == '(1 character found)'


def test_main_count_matches_number_of_lines(capsys):
    main(['cat', 'face'])
    lines = capsys.readouterr().out.splitlines()
    assert lines[-1] == f'({len(lines) - 1} characters found)'


def test_main_zero_matches_prints_only_the_count(capsys):
    main(['zzzznotaword'])
    assert capsys.readouterr().out == '(0 characters found)\n'


def test_main_returns_zero_on_success():
    assert main(['cat']) == 0


def test_main_without_args_shows_usage(capsys):
    status = main([])
    assert status == 1
    assert 'Usage' in capsys.readouterr().err


# ---------- end to end ----------

def test_cli_end_to_end():
    script = Path(__file__).parent / 'charfinder.py'
    proc = subprocess.run(
        [sys.executable, str(script), 'registered', 'sign'],
        capture_output=True, text=True, encoding='utf-8',
    )
    assert proc.returncode == 0
    assert proc.stdout == 'U+00AE\t®\tREGISTERED SIGN\n(1 character found)\n'
