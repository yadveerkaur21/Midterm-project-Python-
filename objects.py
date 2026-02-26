from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class Player:
    first_name: str
    last_name: str
    position: str
    at_bats: int = 0
    hits: int = 0

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def average(self) -> float:
        # If at_bats is 0, avg must be 0.0 per specs
        if self.at_bats <= 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)


class Lineup:
    def __init__(self, players: List[Player] | None = None) -> None:
        self._players: List[Player] = players if players else []

    def __len__(self) -> int:
        return len(self._players)

    def __iter__(self) -> Iterator[Player]:
        # Iterator requirement for easy looping
        return iter(self._players)

    def get(self, index_1_based: int) -> Player:
        return self._players[index_1_based - 1]

    def add(self, player: Player) -> None:
        self._players.append(player)

    def remove(self, index_1_based: int) -> Player:
        return self._players.pop(index_1_based - 1)

    def move(self, from_index_1_based: int, to_index_1_based: int) -> None:
        player = self._players.pop(from_index_1_based - 1)
        self._players.insert(to_index_1_based - 1, player)

    def edit_position(self, index_1_based: int, new_position: str) -> None:
        self.get(index_1_based).position = new_position

    def edit_stats(self, index_1_based: int, at_bats: int, hits: int) -> None:
        p = self.get(index_1_based)
        p.at_bats = at_bats
        p.hits = hits