from common.event_utilities import get_value_from_event

def lambda_handler(event, context):
    print(f'event: {event}')
    print(f'context: {context}')

    user_name = get_value_from_event(event, "user_name")
    password = get_value_from_event(event, "password")

    response = {
        'statusCode:': 200,
        'body': f'hello {user_name} from lambda'
    }

    return response
    


if __name__ == "__main__":
    lambda_handler(None, None)