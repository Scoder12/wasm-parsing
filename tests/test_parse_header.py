import pytest

from parser import parse, ParserError, ParseResult


def test_parses_header():
    assert parse(b"\0ASM") == ParseResult()

    with pytest.raises(ParserError):
        parse(b"nonsense")
