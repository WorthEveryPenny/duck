import sys 

def default():
    print("Hello world")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "duck":
            print("soon")
        elif sys.argv[1] == "dog":
            print("woof!")
        else: 
            print("unknown")
    else:
        default()

if __name__ == "__main__":
    main()
