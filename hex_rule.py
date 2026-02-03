"""Hex deobfuscation rule."""

from __future__ import annotations

import re

from ..core import ObfuscationRule

_HEX_RE = re.compile(r"^[0-9a-fA-F]+$")


class HexRule(ObfuscationRule):
    name = "hex"
    description = "Hex encoded bytes"

    def detect(self, text: str) -> float:
        stripped = "".join(text.split())
        if len(stripped) < 4 or len(stripped) % 2 != 0:
            return 0.0
        if not _HEX_RE.match(stripped):
            return 0.0
        return 0.7

    def decode(self, text: str) -> str:
        stripped = "".join(text.split())
        decoded = bytes.fromhex(stripped)
        return decoded.decode("utf-8", errors="replace")
