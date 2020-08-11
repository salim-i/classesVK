import requests
import json

token = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
version = 5.21


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"https://vk.com/id{self.user_id}"

    def get_users(self):
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'user_id': self.user_id,
                'fields': 'friends',
                'access_token': token,
                'v': version
            }
        )
        return f"{response.json()['response'][0]['first_name']} {response.json()['response'][0]['last_name']} " \
               f"(id {response.json()['response'][0]['id']})"

    def get_friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': token,
                'v': version,
                'user_id': self.user_id,
                'fields': 'friends',
            }
        )
        return [user_id['id'] for user_id in json.loads(response.text)['response']['items']]


user1 = User(32707600)
user2 = User(39377403)
user_friends1 = set(user1.get_friends())
user_friends2 = set(user2.get_friends())
common_friends = user_friends1 & user_friends2
print(f"Пользователь {user1.get_users()} {user1} имеет {len(user1.get_friends())} друзей, "
      f"а пользователь {user2.get_users()} {user2} имеет {len(user2.get_friends())} друзей ")
print(f"У них {len(common_friends)} общих друзей ")
