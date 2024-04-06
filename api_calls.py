import requests

def get_current_user():
    url = "http://192.168.192.194:2003/symfony/web/index.php/api/v1/user"

    payload = {}
    headers = {
    'Authorization': 'Bearer 0355369cd058ad4f2796a07018cb878237ee0b75',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

