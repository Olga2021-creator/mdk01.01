import requests


def check_login(login: str, password: str):
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    r = requests.get('http://127.0.0.1:8000/users/login', data=data)
    answer = r.json()
    code = answer["code"]
    message = answer["message"]

    if code != 200:
        print(f"Server error: {message}")
    if answer["post_id"] is not None:
        return answer["post_id"][0]
