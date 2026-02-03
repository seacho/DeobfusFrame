"""XOR deobfuscation rule for 'xor:<key>:<hex>' strings."""

from __future__ import annotations

import re

from ..core import ObfuscationRule

_XOR_RE = re.compile(r"^xor:(?P<key>\d{1,3}):(?P<data>[0-9a-fA-F]+)$")


class XorRule(ObfuscationRule):
    name = "xor"
    description = "XOR with byte key using format xor:<key>:<hex>"

    def detect(self, text: str) -> float:
        match = _XOR_RE.match(text.strip())
        if not match:
            return 0.0
        key = int(match.group("key"))
        if key < 0 or key > 255:
            return 0.0
        data = match.group("data")
        if len(data) % 2 != 0:
            return 0.0
        return 0.65

    def decode(self, text: str) -> str:
        match = _XOR_RE.match(text.strip())
        if not match:
            raise ValueError("invalid xor format")
        key = int(match.group("key"))
        data = bytes.fromhex(match.group("data"))
        decoded = bytes(b ^ key for b in data)
        return decoded.decode("utf-8", errors="replace")
