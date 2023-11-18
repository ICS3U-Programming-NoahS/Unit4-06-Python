#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 18th, 2023
# This program displays all possible RGB combinations


def main():
    # Using nested loops to display all the possible RGB combinations
    for r in range(0, 256):
        for g in range(0, 256):
            for b in range(0, 256):
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        r, g, b, "RGB({}, {}, {})".format(r, g, b)
                    )
                )


if __name__ == "__main__":
    main()
