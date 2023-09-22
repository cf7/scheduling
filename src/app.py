import json
from controller.Controller import Controller
from endpoints.Endpoint import factory as endpoint_factory

def lambda_handler(event, context):
    

    
    print("lambda_handler")

    print("event: ", event)

    print("Controller: ", Controller)
    
    Controller.get_instance(endpoint_factory)
    
    
    return {
        "statusCode": 200
    }