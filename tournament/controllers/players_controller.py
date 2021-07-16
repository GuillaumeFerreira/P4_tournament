from views.players_view import PlayersView

class PlayerController:

    @classmethod
    def list(cls):
        choice = PlayersView.players_view()

        if choice == "1":
            return "view_player"
        elif choice == "2":
            return "new_player"
        elif choice == "3":
            return "delete_player"
        elif choice.lower() == "q":
            return "quit"

