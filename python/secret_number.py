#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret_number = 5
guess = raw_input ("Type a number for your chance to win € 100.000.000,- : ")

try:

    guess = int(guess)
    if guess == secret_number:
        print "Üüüüüüiiiii you just won € 100.000.000,- !!"
    else:
        print "Sorry, this was not a lucky guess."

except ValueError as e:
    print "Only numbers can win."

