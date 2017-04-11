import vk


APP_ID = 5978862  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return(input("Login: "))


def get_user_password():
    return(input("Password: "))


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends_online = []
    for friend in api.friends.get(fields='first_name,last_name,online'):
        if int(friend["online"]) == 1:        
            friends_online.append(friend)
    return friends_online

def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("%s %s is online" % (friend["first_name"], friend["last_name"]))
    #print(json.dumps(friends_online, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
