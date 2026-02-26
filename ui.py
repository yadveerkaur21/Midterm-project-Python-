from datetime import date, datetime
from objects import Lineup, Player

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
LINE_LEN = 64


def show_title() -> None:
    print("=" * LINE_LEN)
    print("Baseball Team Manager".center(LINE_LEN))
    print(f"CURRENT DATE: {date.today()}")
    print("=" * LINE_LEN)


def show_positions() -> None:
    print("POSITIONS")
    print(", ".join(POSITIONS))


def show_menu() -> None:
    print("\nMENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")


def prompt_menu_option() -> int:
    while True:
        raw = input("\nMenu option: ").strip()
        try:
            option = int(raw)
            if 1 <= option <= 7:
                return option
            print("Invalid menu option. Please try again.")
        except ValueError:
            print("Invalid integer. Please try again.")


def prompt_int(label: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        raw = input(f"{label}: ").strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid integer. Please try again.")
            continue

        if min_value is not None and val < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        if max_value is not None and val > max_value:
            print(f"Value must be at most {max_value}.")
            continue
        return val


def prompt_position(label: str = "Position") -> str:
    while True:
        pos = input(f"{label}: ").strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Please try again.")


def prompt_game_date() -> date | None:
    raw = input("GAME DATE (YYYY-MM-DD) or press Enter to skip: ").strip()
    if raw == "":
        return None
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Game date will be skipped.")
        return None


def show_days_until_game(game_date: date | None) -> None:
    if game_date is None:
        return
    today = date.today()
    if game_date > today:
        print(f"GAME DATE: {game_date}")
        print(f"DAYS UNTIL GAME: {(game_date - today).days}")
    else:
        print(f"GAME DATE: {game_date}")


def display_lineup(lineup: Lineup) -> None:
    print("\n" + "Player  POS   AB    H   AVG")
    print("-" * LINE_LEN)
    for i, p in enumerate(lineup, start=1):
        # avg must always show 3 decimals
        print(f"{i:<2} {p.full_name:<18} {p.position:<4} {p.at_bats:>5} {p.hits:>4} {p.average:>6.3f}")


def prompt_new_player() -> Player:
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    pos = prompt_position("Position")
    ab = prompt_int("At bats", min_value=0)
    hits = prompt_int("Hits", min_value=0, max_value=ab)  # hits cannot exceed at_bats
    return Player(first, last, pos, ab, hits)


def prompt_lineup_number(lineup: Lineup, label: str = "Lineup number") -> int:
    return prompt_int(label, min_value=1, max_value=len(lineup))