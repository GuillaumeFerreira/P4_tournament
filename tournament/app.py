from controllers.home_controller import HomePageController
from controllers.players_controller import PlayerController
import os

class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "players": PlayerController.list,

    }
    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False

    def run(self):
        while not self.exit:
            #On efface la console pour avoir une interface propre
            os.system('cls')

            #On lance le programme
            controller_method = self.routes[self.route]
            next_route = controller_method()

            #result = HomePageController.dispatch()
            #print(result)
            self.route = next_route

            if next_route == "quit":
                self.exit = True