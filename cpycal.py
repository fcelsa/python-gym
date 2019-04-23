#!/usr/bin/python
# cpycal
#
# GNU Public License version 3 - See http://www.gnu.org/licenses/licenses.html
#
# (c) Fabio Celsalonga
#
# a compact calendar from command line useful for geektool 
# default behavior: show previus month and three next month, 
# current month and day highlighted, holidays and weekends coloured.
# total number of month are defined in variable numm.
# holidays list can be expanded with your.
#
# Important note:
# this python script is ok for Linux OS X and probably other *nix platform
# for Windows we need ansi.sys or you can retouch code with colorama library
# https://pypi.python.org/pypi/colorama
#
# Ver. 2.0 2015-12-09

import calendar
import datetime
import time
import locale

locale.setlocale(locale.LC_ALL, '')

nwhiline = '''\033[1;37m'''    # white
nblkline = '''\033[0;30m'''    # black
nbluline = '''\033[0;34m'''    # blue
ngrnline = '''\033[0;32m'''    # green
ncynline = '''\033[0;36m'''    # cyan
nredline = '''\033[0;31m'''    # red
nprpline = '''\033[0;35m'''    # purple
nyelline = '''\033[0;33m'''    # purple
ngryline = '''\033[0;37m'''    # gray
dgryline = '''\033[1;30m'''    # dark gray
bbluline = '''\033[1;34m'''    # bright blue
bgrnline = '''\033[1;32m'''    # bright green
bcynline = '''\033[1;36m'''    # bright cyan
bredline = '''\033[1;31m'''    # bright red
bprpline = '''\033[1;35m'''    # bright purple
byelline = '''\033[1;33m'''    # bright yellow
nrmlline = '''\033[0m'''      # return to normal at EOL
highline = '''\033[44;37;33m''' # evidenziato

# holydays list, default Italian; you can adjust this to your needs
h_list = ['01-01', '06-01', '25-04', '01-05', '02-06', '15-08', '01-11', '08-12', '25-12', '26-12']

numm = 4 # total number of month processed
now = time.localtime()
cury = now[0] if now[1] > 1 else now[0] -1
curm = now[1]-1 if now[1] > 1 else 12
curw = datetime.date(now[0], now[1], now[2]).isocalendar()[1]
ddw = 1

for i in range(numm, 0, -1):
    kw=datetime.date(cury, curm, ddw).isocalendar()[1]
    wdheader = calendar.weekheader(2)
    listday = wdheader.split(' ')
    for itemlday, value in enumerate(listday):
        if now[6]==itemlday and curm==now[1]:
            listday[itemlday] = byelline + listday[itemlday] + nrmlline
                
        if listday[itemlday]=="Sa":
            listday[itemlday] = ngryline + listday[itemlday] + nrmlline
        
        if listday[itemlday]=="Do":
            listday[itemlday] = bredline + listday[itemlday] + nrmlline
        
    print (calendar.month_name[curm],cury,"\nW |",listday[0],listday[1],listday[2],listday[3],listday[4],listday[5],listday[6])
    
    m = calendar.monthcalendar(cury,curm)
    for l in m:
        if int(kw)==int(curw):
            line = highline + '{:2d}|'.format(kw) + nrmlline
        else:
            line = '{:2d}|'.format(kw)
        
        for d in l:
            daym = '{0:02d}'.format(d)+"-"+'{0:02d}'.format(curm)
            
            if any(daym in s for s in h_list):
                line += bredline

            if d==now[2] and curm==now[1]:
                line += highline
            
            line = line + (' {:2d}'.format(d) if (d>0) else '   ') + nrmlline
           
            if d > 1 and d < 31 and datetime.date(cury, curm, d).isocalendar()[2] == 4: 
                ddw = d
                
        print line
                
        # calcolo esattamente quale sara' la prossima settimana 
        # perche' se mi limito ad incrementare kw di 1 (kw +=1) al cambio di anno ho problemi...
        # python e' fantastico in questo... la libreria datetime permette di incrementare una data
        # di tot giorni, settimane, mesi, anni...
        nextweek = datetime.date(cury,curm, ddw) + datetime.timedelta(weeks=1)
        kw=nextweek.isocalendar()[1]

    if curm<12:
        curm += 1
        ddw = 1
    else:
        curm = 1
        cury += 1
        ddw = 1
    if i>1:
        print
