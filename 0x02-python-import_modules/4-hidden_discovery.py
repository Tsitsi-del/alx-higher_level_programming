#!/usr/bin/python3

if __name__ == "__main__":
    """Function to print all names defined
    by hidden_4 module"""
    import hidden_4

    i = dir(hidden_4)
    for name in i:
        if name[:2] != "__":
            print(name)
