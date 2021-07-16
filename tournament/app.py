from controllers.home_controller import HomePageController
from controllers.players_controller import PlayerController
from controllers.tournament_controller import TournamentController
import os

class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "players": PlayerController.list,
        "new_tournament": TournamentController.new_tournament,
        "new_player" : PlayerController.new_player_controller,
        "delete_player" : PlayerController.del_player_controller,

    }
    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.players =[]

    def run(self):
        while not self.exit:
            #On efface la console pour avoir une interface propre
            os.system('cls')

            #On execute la route pour aller sur les bonnes propositions

            controller_method = self.routes[self.route]
            next_route,players = controller_method(self.players)


            self.route = next_route
            self.players = players

            if next_route == "quit":
                self.exit = True