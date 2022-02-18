class usuario(object):
    __instance = None

    def __new__(cls):
        if usuario.__instance is None:
            print("Hola nueva instancia")
            usuario.__instance = object.__new__(cls)
        
        return usuario.__instance


if __name__ == '__main__':
    user1 = usuario()
    user2 = usuario()

    print(user1 is user2)