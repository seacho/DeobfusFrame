"""Engine for iterative deobfuscation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .core import DeobfuscationResult, Registry


@dataclass
class DeobfuscationStep:
    result: DeobfuscationResult


@dataclass
class DeobfuscationReport:
    original: str
    final: str
    steps: List[DeobfuscationStep] = field(default_factory=list)


class DeobfuscatorEngine:
    def __init__(self, registry: Registry) -> None:
        self._registry = registry

    def deobfuscate(
        self,
        text: str,
        *,
        max_rounds: int = 3,
        min_score: float = 0.5,
    ) -> DeobfuscationReport:
        current = text
        steps: List[DeobfuscationStep] = []

        for _ in range(max_rounds):
            match = self._registry.best_match(current)
            if match is None or match.score < min_score:
                break
            steps.append(DeobfuscationStep(result=match))
            current = match.decoded

        return DeobfuscationReport(original=text, final=current, steps=steps)
