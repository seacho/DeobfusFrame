"""Base64 deobfuscation rule."""

from __future__ import annotations

import base64
import binascii
import re

from ..core import ObfuscationRule

_BASE64_RE = re.compile(r"^[A-Za-z0-9+/=\n\r]+$")


class Base64Rule(ObfuscationRule):
    name = "base64"
    description = "Base64 encoded string"

    def detect(self, text: str) -> float:
        stripped = "".join(text.split())
        if len(stripped) < 8 or len(stripped) % 4 != 0:
            return 0.0
        if not _BASE64_RE.match(stripped):
            return 0.0
        try:
            base64.b64decode(stripped, validate=True)
        except (ValueError, binascii.Error):
            return 0.0
        return 0.8

    def decode(self, text: str) -> str:
        stripped = "".join(text.split())
        decoded = base64.b64decode(stripped)
        return decoded.decode("utf-8", errors="replace")
