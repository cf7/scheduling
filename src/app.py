import json
import pydantic
from api.API import API
from api.routes.Routes import route_factory


def lambda_handler(event, context):
    try:
        print("lambda_handler")

        print("event: ", event)

        api = API.get_instance(route_factory)

        return api.api_action(event)
    except Exception as e:
        print(e)
        return None


"""
API Architecture Overview:

app.lambda_handler
    --> API layer
        --> Business logic layer (service or Use Cases: depending on architecture)
            --> Repository layer (Entity manipulation logic)
                --> Entity layer (domain specific models)
                    --> persistence layer (DAO or ORM: depending on architecture)
"""

"""
Notes:

requirements.txt must be at top-level of /src
for sam-cli and docker to resolve dependencies properly

"""
