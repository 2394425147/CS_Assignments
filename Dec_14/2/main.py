from Models.Clock import Clock

def main():
    clock = Clock()
    clock.show_time()
    clock.set_time(-1, 0, 0) # This is invalid
    clock.show_time()
    clock.set_time(7, 27, 0) # This is valid
    clock.show_time()
    pass


if __name__ == "__main__":
    main()