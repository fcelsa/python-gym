#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
an useful script to take decision
"""


from random import choice

choices = ["work on project alfa",
           "work on project beta",
           "work on project x",
           "take care personal finance",
           "take care business finance",
           "coding chose your...",
           "take care of junk on your computer",
           "some things in Quora",
           "read news feed",
           "stand up five minutes",
           "drink !!",
           "run somewhere",
           "something new... search on Google",
           "take a look on work to do list",
           "take a look on home to do list",
           "do nothing for five minutes",
           "fooling around at choice",
           "do something useful for someone else",
           "it's time to fuck around YT/Twitch"]

print("Now ! ", choice(choices))
