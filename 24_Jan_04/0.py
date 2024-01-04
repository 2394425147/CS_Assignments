from Errors.MyError import MyError

def myfunction():
    try:
        raise MyError("Hello from MyError")
    except MyError as e:
        print(f"Caught MyError:\n{e}")



if __name__ == "__main__":
    myfunction()
