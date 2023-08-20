import json

def get_value_from_event(event: dict, key):

    body: dict = event.get("body", None)
    value = None
    if body is not None:
        if type(body) is str:
            body = convert_string_to_json(body)
            
    
    if type(body) is dict:
        value = body.get(key, None) 
    else:
        value = event.get(key, None)   
    
    return value


def convert_string_to_json(string, retry=True):
    """
    Converts a string to a JSON object
    :param string: string to convert
    :return: JSON object
    """
    try:
        return json.loads(string)
    except Exception as e:
        print(e)
        if "Expecting property name enclosed in double quotes" in str(e) and retry:
            string = str(string).replace("'", "\"")
            return convert_string_to_json(string ,False)
        else:
            raise e
