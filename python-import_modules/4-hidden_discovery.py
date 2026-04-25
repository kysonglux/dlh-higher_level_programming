#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # dir() returns a sorted list of all names defined in the module
    all_names = dir(hidden_4)

    for name in all_names:
        # Check if the name does NOT start with "__"
        if not name.startswith("__"):
            print(name)
