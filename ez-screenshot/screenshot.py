#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
import pyscreenshot as ImageGrab
import argparse
import os

def main():
    with Listener(on_press = keypress) as l:
        l.join()

def keypress(key):
    if key == arg.keypress:
        im = ImageGrab.grab()
        im.save(arg.output_directory + arg.filename + '-' + str(arg.start_i) + '.png')
        arg.start_i += 1

p = argparse.ArgumentParser(description='Capture frames on screen ezily')
p.add_argument('-out', '--output-directory', type=str, default=os.getcwd())
p.add_argument('-i', '--start-i', type=int, default=0)
p.add_argument('-file', '--filename', type=str, default='screen')
p.add_argument('-key', '--keypress', default=Key.f8)
arg = p.parse_args()

if __name__ == '__main__':
    main()

