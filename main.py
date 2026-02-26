from objects import Lineup
import db
import ui


def add_player(lineup: Lineup) -> None:
    player = ui.prompt_new_player()
    lineup.add(player)
    print(f"{player.full_name} was added.")


def remove_player(lineup: Lineup) -> None:
    if len(lineup) == 0:
        print("Lineup is empty.")
        return
    num = ui.prompt_lineup_number(lineup, "Number")
    p = lineup.remove(num)
    print(f"{p.full_name} was deleted.")


def move_player(lineup: Lineup) -> None:
    if len(lineup) < 2:
        print("Need at least 2 players to move.")
        return
    current_num = ui.prompt_lineup_number(lineup, "Current lineup number")
    selected = lineup.get(current_num)
    print(f"{selected.full_name} was selected.")
    new_num = ui.prompt_int("New lineup number", min_value=1, max_value=len(lineup))
    lineup.move(current_num, new_num)
    print(f"{selected.full_name} was moved.")


def edit_position(lineup: Lineup) -> None:
    if len(lineup) == 0:
        print("Lineup is empty.")
        return
    num = ui.prompt_lineup_number(lineup, "Lineup number")
    p = lineup.get(num)
    print(f"You selected {p.full_name} POS={p.position}")
    new_pos = ui.prompt_position("Position")
    lineup.edit_position(num, new_pos)
    print(f"{p.full_name} was updated.")


def edit_stats(lineup: Lineup) -> None:
    if len(lineup) == 0:
        print("Lineup is empty.")
        return
    num = ui.prompt_lineup_number(lineup, "Lineup number")
    p = lineup.get(num)
    print(f"You selected {p.full_name} AB={p.at_bats} H={p.hits}")
    ab = ui.prompt_int("At bats", min_value=0)
    hits = ui.prompt_int("Hits", min_value=0, max_value=ab)
    lineup.edit_stats(num, ab, hits)
    print(f"{p.full_name} was updated.")


def main() -> None:
    ui.show_title()
    game_date = ui.prompt_game_date()
    ui.show_days_until_game(game_date)
    ui.show_positions()

    players = db.load_players()
    lineup = Lineup(players)

    while True:
        ui.show_menu()
        option = ui.prompt_menu_option()

        if option == 1:
            ui.display_lineup(lineup)
        elif option == 2:
            add_player(lineup)
            db.save_players(list(lineup))
        elif option == 3:
            remove_player(lineup)
            db.save_players(list(lineup))
        elif option == 4:
            move_player(lineup)
            db.save_players(list(lineup))
        elif option == 5:
            edit_position(lineup)
            db.save_players(list(lineup))
        elif option == 6:
            edit_stats(lineup)
            db.save_players(list(lineup))
        elif option == 7:
            print("Bye!")
            break


if __name__ == "__main__":
    main()