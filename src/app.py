import json
import pydantic
from controller.Controller import Controller
from routes.Routes import route_factory


def lambda_handler(event, context):
    print("lambda_handler")

    print("event: ", event)

    print("Controller: ", Controller)

    controller = Controller.get_instance(route_factory)

    return controller.controller_action(event)


"""
API Architecture Overview:

app.lambda_handler
    --> Controller (API layer)
        --> Domain Service layer (Business logic)
            --> Repository layer (Entity logic)
                --> DAO layer (access DB)
                    --> persistance layer (DB)
"""

"""
Notes:

requirements.txt must be at top-level of /src
for sam-cli and docker to resolve dependencies properly

"""
