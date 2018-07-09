import json

def get(event, context):
    """Handle the GET request and return the full lambda request event"""

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
