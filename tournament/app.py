from controllers.home_controller import HomePageController
from controllers.players_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController
from models.store import Store

import os


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "detail_tournament": TournamentController.detail_tournament,
        "players": PlayerController.list,
        "new_tournament": TournamentController.new_tournament,
        "new_player": PlayerController.new_player_controller,
        "delete_player": PlayerController.del_player_controller,
        "list_tournament": TournamentController.tournament_params_edit,
        "edit_player": PlayerController.edit_player_controller,
        "add_player_tournament": TournamentController.add_player_tournament,
        "first_round": RoundController.first_round,
        "next_round": RoundController.next_round,
        "end_page": RoundController.end_match,
        "save_tournament": TournamentController.save_json,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        new_store = Store()
        new_store.store_test()
        # new_store.read_json()
        self.store = new_store.data

    def run(self):
        while not self.exit:

            # On efface la console pour avoir une interface propre
            os.system("cls")

            # On execute la route pour aller sur les bonnes propositions

            controller_method = self.routes[self.route]
            next_route, next_params = controller_method(self.store, self.route_params)

            self.route = next_route
            self.route_params = next_params

            if next_route == "quit":
                self.exit = True
