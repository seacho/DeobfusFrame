"""Core abstractions for deobfuscation rules and registry management."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable, List, Optional


@dataclass
class DeobfuscationResult:
    """Represents a single deobfuscation attempt."""

    name: str
    score: float
    decoded: str
    metadata: dict = field(default_factory=dict)


class ObfuscationRule:
    """Base class for obfuscation detection and decoding."""

    name: str = ""
    description: str = ""

    def detect(self, text: str) -> float:
        """Return confidence score between 0.0 and 1.0."""

        raise NotImplementedError

    def decode(self, text: str) -> str:
        """Return decoded text (may raise ValueError for invalid input)."""

        raise NotImplementedError


class Registry:
    """Registry for deobfuscation rules."""

    def __init__(self) -> None:
        self._rules: List[ObfuscationRule] = []

    def register(self, rule: ObfuscationRule) -> None:
        self._rules.append(rule)

    def extend(self, rules: Iterable[ObfuscationRule]) -> None:
        for rule in rules:
            self.register(rule)

    def rules(self) -> List[ObfuscationRule]:
        return list(self._rules)

    def best_match(self, text: str) -> Optional[DeobfuscationResult]:
        best: Optional[DeobfuscationResult] = None
        for rule in self._rules:
            score = rule.detect(text)
            if score <= 0:
                continue
            decoded = rule.decode(text)
            result = DeobfuscationResult(
                name=rule.name,
                score=score,
                decoded=decoded,
                metadata={"description": rule.description},
            )
            if best is None or score > best.score:
                best = result
        return best
