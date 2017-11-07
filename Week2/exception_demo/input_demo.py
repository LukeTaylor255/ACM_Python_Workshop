import Week2.mymath.shapes as shapes

def run_demo():
    try:
        print("Enter two floats.  Other values will generate exceptions.")
        i = input()
        width, height = map(float, i.split())
    except EOFError:
        print("End of file was entered.")
    except KeyboardInterrupt:
        print("Kill signal was thrown.")
    except ValueError:
        print("Enter exactly two floats")
    else:
        s = shapes.Rectangle(width, height)
        print("Rectangle with area = " + str(s.area()) + " and perimeter = " + str(s.perimeter()))
    finally:
        print("Exiting...")
