import random, os, time
import rnd_names

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

a1 = fighters(rnd_names.r_name, rnd_names.rnd_w, rnd_names.rnd_h, rnd_names.r_r)

a1.info()

