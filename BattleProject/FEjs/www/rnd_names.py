import random

names = ['Tom','Genry', 'Sam', 'Antony', 'Andy', 'John', 'Bill', 'James']
surnames = ['Hendricks', 'Everman', 'Cloudy', 'Brown', 'Whitesiry', 'Alibi', 'Ericson']

def rand():
    rnd1 = random.randint(0,7)
    rnd2 = random.randint(0,6)
    rnd_w = random.randint(50,120)
    rnd_h = random.randint(168,202)
    rnd_r = random.randint(1,10)

    r_name = names[rnd1] + ' ' + surnames[rnd2]
    r_w = rnd_w
    r_h = rnd_h
    r_r = rnd_r
    return r_name,r_w,r_h, r_r