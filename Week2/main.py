import Week2.mymath
import Week2.exception_demo
if __name__ == "__main__":
    print("Enter a command:")
    command = input()
    if("sin" in command):
        while(True):
            val = input()
            if(val == "exit"):
                exit(0)
            print(Week2.mymath.math.sin(float(val)))
    elif("sq" in command):
        sq = Week2.mymath.shapes.Square(3)
        print(sq.area())
    else:
        Week2.exception_demo.input_demo.run_demo()
