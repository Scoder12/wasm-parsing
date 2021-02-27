import pytest

from wasm_parser import parse, ParseError, ParseResult


def test_parses_header():
    assert parse(b"\0ASM") == ParseResult()

    with pytest.raises(ParseError):
        parse(b"nonsense")
