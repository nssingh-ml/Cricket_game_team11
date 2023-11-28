import sqlite3

crick_db=sqlite3.connect('CRICKET.db')
ckt_cursor=crick_db.cursor()

####MATCH TABLE###
try:
    ckt_cursor.execute('''
    CREATE TABLE match (player TEXT NOT NULL,
    scored INTEGER,
    faced INTEGER,
    fours INTEGER,
    sixes INTEGER,
    bowled INTEGER,
    maiden INTEGER,
    given INTEGER,
    wkts INTEGER,
    catches INTEGER,
    stumping INTEGER,
    runout INTEGER);
    ''')



    ###stats###
    ckt_cursor.execute( '''
    CREATE TABLE stats (player PRIMARY KEY,
    matches INTEGER,
    runs INTEGER,
    hundreds INTEGER,
    fifties INTEGER,
    value INTEGER,
    ctg TEXT NOT NULL);
    ''')
    ############################--------TEAMS TABLE---------###########################
    ckt_cursor.execute('''
    CREATE TABLE teams (name TEXT NOT NULL,
    players TEXT NOT NULL,
    value INTEGER);
    ''')


except:
    print("error in operation")
    ckt_cursor.rollback()



ckt_cursor.close()
