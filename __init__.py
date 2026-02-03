"""DeobfusFrame package."""

from __future__ import annotations

from .core import Registry
from .engine import DeobfuscatorEngine
from .obfuscations.base64_rule import Base64Rule
from .obfuscations.hex_rule import HexRule
from .obfuscations.reverse_rule import ReverseRule
from .obfuscations.xor_rule import XorRule


def default_registry() -> Registry:
    registry = Registry()
    registry.extend([Base64Rule(), HexRule(), ReverseRule(), XorRule()])
    return registry


def default_engine() -> DeobfuscatorEngine:
    return DeobfuscatorEngine(default_registry())


__all__ = ["DeobfuscatorEngine", "Registry", "default_engine", "default_registry"]
