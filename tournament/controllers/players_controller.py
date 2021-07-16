from views.players_view import PlayersView
from models.players import Players
class PlayerController:

    @classmethod
    def list(cls):
        choice = PlayersView.players_view()

        if choice == "1":
            return "new_player"
        elif choice == "2":
            return "delete_player"
        elif choice == "3":
            return "edit_player"
        elif choice.lower() == "q":
            return "quit"

    @classmethod
    def new_player_view(cls, players):
        params = PlayersView.new_player()
        players.add(Players(params['nom'],params['prénom'],params['date de naissance'],params['sexe'],params['rang']))
        return "players" , players

