#coding:utf8
#time:'下午5:14:16-7-11:2016'
#author:Gru_GHT

import pygame
import time
def soundw():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('alert.wav')
    pygame.mixer.music.play()
    time.sleep(1)