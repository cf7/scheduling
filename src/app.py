import json

def lambda_handler(event, context):
    
    print("lambda_handler")

    print("event: ", event)

    return {
        "status": 200
    }