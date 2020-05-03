def confirmLogin(system):
    global username, password
    username = input("Enter your {} Username: ".format(system))
    password = input("Enter your {} Password: ".format(system))

    entered_correctly = input("Was your information entered correctly (type 'no' if not or hit enter to continue)? ")
    print("\n")
    # if the info was incorrectly entered
    while entered_correctly == 'no':
        username = input("Enter your {} Username: ".format(system))
        password = input("Enter your {} Password: ".format(system))
        entered_correctly = input(
            "Was your information entered correctly (type 'no' if not or hit enter to continue)? ")
        print("\n")


def getUserName():
    return username


def getPassword():
    return password
