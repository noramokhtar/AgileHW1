import sys

def hello_world(name):
    print("Hello, {}!".format(name))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        hello_world(name)
    else:
        print("Please provide your name as a command-line argument.")
