import random, os, time
import rnd_names
import sqlite3

conn = sqlite3.connect('fighters.db')
cur = conn.cursor()
os.system('cls')
class fighters:
    def __init__(self,name, weight, height, rate):
        self.name = name
        self.weight = weight
        self.height = height
        self.rate = rate
    def info(self):
        print('Fighter |   Name:    ',self.name)
        print('        |   Weight:  ',self.weight)
        print('        |   Height:  ',self.height)
        print('        |   Rate:    ',self.rate)

a1 = fighters(rnd_names.rand()[0],rnd_names.rand()[1],rnd_names.rand()[2],rnd_names.rand()[3])
a2 = fighters(rnd_names.rand()[0],rnd_names.rand()[1],rnd_names.rand()[2],rnd_names.rand()[3])

# cur.execute("""create table if not exists fighters(
#             Name text,
#             Weight text,
#             Height text,
#             Rate int);
#             """)
a = (rnd_names.rand()[0],rnd_names.rand()[1],rnd_names.rand()[2],rnd_names.rand()[3])
# cur.execute('insert into fighters values(?,?,?,?);', a)
command = input('Enter query: ')
cur.execute(command)

for p in cur.fetchall():
    print(p[0::])

conn.commit()
conn.close()


