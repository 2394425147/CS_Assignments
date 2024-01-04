from Errors.MyError import MyError

def myfunction():
    raise MyError("Raised as MyError")


if __name__ == "__main__":
    myfunction()
