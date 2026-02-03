"""Reverse-string deobfuscation rule."""

from __future__ import annotations

from ..core import ObfuscationRule


class ReverseRule(ObfuscationRule):
    name = "reverse"
    description = "String reversed with prefix 'rev:'"

    def detect(self, text: str) -> float:
        if text.startswith("rev:") and len(text) > 4:
            return 0.6
        return 0.0

    def decode(self, text: str) -> str:
        payload = text[4:]
        return payload[::-1]
