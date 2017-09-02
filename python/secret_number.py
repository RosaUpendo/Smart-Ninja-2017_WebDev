#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main():
    secret_number = random.randint(1,100)


    while True:
        guess = raw_input("Type a number for your chance to win € 100.000.000,- : ")
        try:
            guess = int(guess)
            if guess == secret_number:
                print "Üüüüüüiiiii you just won € 100.000.000,- !!"
                break
            else:
                print "Sorry, this was not a lucky guess."

        except ValueError as e:
            print "Only numbers can win."

if __name__ == "__main__":
    main()


