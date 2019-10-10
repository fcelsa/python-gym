#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
today.py: excercise with date and time, show today things...

Copyright (c) 2019 Fabio Celsalonga
MIT License

"""

import os
import sys
import calendar
import datetime
import time
import locale
import math
import decimal

fullPathFileName = os.path.realpath(__file__)

dec = decimal.Decimal
locale.setlocale(locale.LC_ALL, '')


def calc_easter(year):
    """Return Easter Sunday for the year in the form YYYY-MM-GG"""
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return datetime.date(year, month, day)

def holyday_list(selectedYear):
    # holydays list, default Italian; you can adjust this to your needs
    h_list = ['01-01', '06-01', '25-04', '01-05', '02-06', '15-08', '01-11',
              '08-12', '25-12', '26-12']
    easter_date = calc_easter(selectedYear)
    easter_date_monday = easter_date + datetime.timedelta(days=1)
    h_list.extend([easter_date.strftime('%d-%m'),
                  easter_date_monday.strftime('%d-%m')])
    return h_list

def moon_position(now):
    diff = now - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))
    return lunations % dec(1)

def moon_phase(now, verbose):
    pos = moon_position(now)
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    str_index = " " + str(index)
    if verbose:
        return {
            0: "🌑 Luna nuova      " + str(round(float(pos), 4)) + str_index,
            1: "🌒 Luna crescente  " + str(round(float(pos), 4)) + str_index,
            2: "🌓 Primo quarto    " + str(round(float(pos), 4)) + str_index,
            3: "🌔 Gibbosa cresente" + str(round(float(pos), 4)) + str_index,
            4: "🌕 Luna piena      " + str(round(float(pos), 4)) + str_index,
            5: "🌖 Gibbosa calante " + str(round(float(pos), 4)) + str_index,
            6: "🌗 Ultimo quarto   " + str(round(float(pos), 4)) + str_index,
            7: "🌘 Luna calante    " + str(round(float(pos), 4)) + str_index
        }[int(index) & 7]
    else:
        return {
            0: "🌑",
            1: "🌒",
            2: "🌓",
            3: "🌔",
            4: "🌕",
            5: "🌖",
            6: "🌗",
            7: "🌘"
        }[int(index) & 7]


def main():
    now = datetime.datetime.today()
    dataEstesa = '{:%A %d %B %Y}'.format(now)
    dataNormal = '{:%d/%m/%Y}'.format(now)

    if len(sys.argv) == 1:
        print('{:%a %d %b  w.%V}'.format(now) + "  %s " % (moon_phase(now, False)))
        print(dataNormal)
        print(len(sys.argv))

    else:
        print('{:%a %d %b  w.%V}'.format(now) + "  %s " % (moon_phase(now, False)))
        print(dataEstesa)
        print(len(sys.argv))

if __name__ == "__main__":
    main()
