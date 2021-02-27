from dataclasses import dataclass
from collections import deque


class ParseError(ValueError):
    pass


@dataclass
class ParseResult:
    pass


def get(inp: deque, amt: int) -> bytes:
    r = []
    for _ in range(amt):
        r.append(inp.popleft())
    return bytes(r)


def parse(input_bytes: bytes) -> None:
    inp = deque(input_bytes)
    if get(inp, 4) != b"\0ASM":
        raise ParseError("Missing WASM header")
    return ParseResult()
