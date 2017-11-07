def run_demo():
    try:
        i = input()
    except EOFError:
        print("End of file was entered.")
    except KeyboardInterrupt:
        print("Kill signal was thrown.")
    finally:
        print("You entered: " + i)
