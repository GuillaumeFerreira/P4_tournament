from views.players_view import PlayersView
from models.players import Players
class PlayerController:

    @classmethod
    def list(cls,store, route_params):
        choice = PlayersView.players_view(store['players'])

        if choice == "1":
            return "new_player",None
        elif choice == "2":
            return "delete_player",None
        elif choice == "3":
            return "edit_player",None
        elif choice == "4":
            return "homepage",None
        elif choice.lower() == "q":
            return "quit",None

    @classmethod
    def new_player_controller(cls, store, route_params):
        params = PlayersView.new_player()
        store['players'].append(Players(params['nom'],params['prénom'],params['date de naissance'],params['sexe'],params['rang']))
        return "players", store

    @classmethod
    def del_player_controller(cls, store, route_params):
        index = PlayersView.del_player_view(store['players'])
        store['players'].pop(int(index) - 1)
        return "players", store