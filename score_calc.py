import sqlite3

crc_db=sqlite3.connect('CRICKET.db')
_cursor=crc_db.cursor()
# qwry='select * from match;'
_cursor.execute('select * from match;')
row=_cursor.fetchall()
# print(row)

### calculate score###

def calculate_score(row):
    points=0.0
    score=row[1]


    ##strike rate

    try:
        strike_rate=float(row[1]/float(row[2]))
    except:
        strike_rate=0
    if strike_rate>1: # for strike rate greater than 100
        points+=4
    elif strike_rate>=0.8: ##for strike rate grater than 80\100
        points+=2


    ##boundaries
    four,sixes=row[3],row[4]
    points+=four
    points+=2*sixes


    ## twos
    run=score-(4*four+6*sixes)
    points+=(run/2)

    ##wickets##
    wickets=int(row[8])
    points+=10*wickets
    if wickets>=5 : ## Additional 10 points for 5 wickets
        points+=10
    elif wickets>=3: ##Additional 5 points for 3 wickets
        points+=5

    ##economy##
    try:
        economy=float(int(row[7])/(int(row[5])/6))
        if 3.5<=economy<=4.5:
            points+=4
        elif 2<=economy<3.5:
            points+=7
        elif 0<economy<2:
            points+=10
    except:
        points+=0

    ##feilding##
    catch=10*float(row[9])
    stumping=10*float(row[10])
    run_out=10*float(row[11])
    points+=(catch+stumping+run_out)

    ##centuries
    if score >= 100:
        points+=10
    elif score>=50:
        points+=5

    return points

player_points={}
for i in row:
    player_points[i[0]]=calculate_score(i)

print(player_points)