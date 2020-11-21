import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1",help="no1")
    #for positional args parser.add_argument("--number1",help="no1")
    parser.add_argument("number2",help="no2")
    #for positional args parser.add_argument("--number2",help="no2")
    mainparser = parser.parse_args()
    no1 = int(mainparser.number1)
    no2 = int(mainparser.number2)
    print(no1+no2)


