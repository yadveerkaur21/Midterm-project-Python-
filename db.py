import csv
from pathlib import Path
from typing import List
from objects import Player


FILENAME = "players.csv"


def load_players(filename: str = FILENAME) -> List[Player]:
    path = Path(filename)
    if not path.exists():
        # Missing file must be handled (start with empty lineup)
        return []

    players: List[Player] = []
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            players.append(
                Player(
                    first_name=row["first_name"].strip(),
                    last_name=row["last_name"].strip(),
                    position=row["position"].strip(),
                    at_bats=int(row["at_bats"]),
                    hits=int(row["hits"]),
                )
            )
    return players


def save_players(players: List[Player], filename: str = FILENAME) -> None:
    path = Path(filename)
    with path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = ["first_name", "last_name", "position", "at_bats", "hits"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in players:
            writer.writerow(
                {
                    "first_name": p.first_name,
                    "last_name": p.last_name,
                    "position": p.position,
                    "at_bats": p.at_bats,
                    "hits": p.hits,
                }
            )