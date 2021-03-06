import vk
import getpass

APP_ID = 5978862  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return(input("Enter your VK login: "))


def get_user_password():
    return getpass.getpass("Enter your VK password: ")

def get_users(api,users_ids):
    return api.users.get(user_ids=','.join(map(str,users_ids)))

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    friends_online = api.friends.getOnline(online_mobile=1)
    return {"online": get_users(api,friends_online["online"]), "online_mobile": get_users(api,friends_online["online_mobile"])}

def output_friends_to_console(friends_online):
    print("\nList of friends who online in VK through PC\n")
    for friend in friends_online["online"]:
        print("%s %s is online" % (friend["first_name"], friend["last_name"]))
    print("\nList of friends who online in VK through mobile devices\n")    
    for friend in friends_online["online_mobile"]:
        print("%s %s is online mobile" % (friend["first_name"], friend["last_name"]))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
