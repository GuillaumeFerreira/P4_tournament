from views.players_view import PlayersView
from models.players import Players
class PlayerController:

    @classmethod
    def list(cls,players):
        choice = PlayersView.players_view(players)

        if choice == "1":
            return "new_player",players
        elif choice == "2":
            return "delete_player",players
        elif choice == "3":
            return "edit_player",players
        elif choice == "4":
            return "homepage",players
        elif choice.lower() == "q":
            return "quit",players

    @classmethod
    def new_player_controller(cls, players):
        params = PlayersView.new_player()
        players.append(Players(params['nom'],params['prénom'],params['date de naissance'],params['sexe'],params['rang']))
        return "players", players

    @classmethod
    def del_player_controller(cls, players):
        index = PlayersView.del_player_view(players)
        players.pop(int(index) - 1)
        return "players", players