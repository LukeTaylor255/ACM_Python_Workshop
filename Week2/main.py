import Week2.mymath
import Week2.exception_demo
import sys

if __name__ == "__main__":
    print("Enter a command.  Type help for usage")
    while(True):
        sys.stdout.write("> ")
        command = input()
        if("sin" in command):
            val = float(command.split()[1])
            print(Week2.mymath.math.sin(val))
        elif("sq" in command):
            val = float(command.split()[1])
            sq = Week2.mymath.shapes.Square(val)
            print(sq.area())
        elif("help" in command):
            print("Type sin for a demo of sine, square for a demo of a square's area\
            , except for a demo of exceptions, or exit to quit.")
        elif("exit" in command):
            exit(0)
        else:
            Week2.exception_demo.input_demo.run_demo()
