username = input(" Username : ")
password = input(" Password : ")

if username == "stang" and password == "123456":
    print("Welcome Guy")
    print("----- Stang ShoppingMall-----")
    print("1. PS5")

    select = int(input("Choose to buy : "))
    if select == 1:
        print("1. PS5 = 12900")
        print("2. PS5 pro = 17900")

        PS5 = int(input("Choose Version : "))
        if PS5 == 1:
            PS5 = "PS5"
            price = 12900
            print("PS5")
        elif PS5 == 2:
            PS5 = "PS5 pro"
            price = 17900
            print("PS5")
        else:
            print("Invalid PS5 version selected.")
            exit()

        howmany = int(input("How Many PS5 : "))
        print(f"{PS5} x{howmany} Price = {price * howmany} THB")

else:
    print("Incorrect username or password")