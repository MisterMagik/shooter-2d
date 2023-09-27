#import pygame
import sys
#import math 
#sys.path.insert(0, './src/entity')
#sys.path.insert(0, './src/object')
#import player
#import enemy
#import wall
sys.path.append('./core')
#import core.core as core
import core


def main():
    c = core.Core(1280,720)
    c.run()
    pass

if __name__ == "__main__":
    main()
