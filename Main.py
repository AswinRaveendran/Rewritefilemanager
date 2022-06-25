def looping():
    """This is to loop this programme"""
    last = input("Do you want to continue action\nIf yes press 1\nTo exit press any key\n")
    if last == "1":
        programme()
    else:
        print("Thank you for using Rewrite")


def getdate():
    """This function is used to get time"""
    import datetime
    return datetime.datetime.now()


def writefile():
    """This function is used to write the data into a new file"""
    name = input("Enter name of file\n")
    with open(name, "a") as f:
        time = str(getdate())
        content = "[" + time + "] " + input("Enter details\n")
        f.write("\n" + content)


def readfile():
    """This function is used to read a file"""
    name = input("Enter the name of file\n")
    with open(name) as f:
        print(f.read())


def programme():
    """Calling the entire programme"""
    selection = int(input("Press 1 for loging\nPress 2 for retrieving\n"))
    if selection == 1:
        try:
            writefile()
        except:
            print("input invalid")
    elif selection == 2:
        try:
            readfile()

        except:
            print("file not found")

    else:
        print("invalid entry")
    looping()


print("Welcome to rewrite center")
programme()
