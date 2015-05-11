#!/usr/bin/env python

from voice.voice import test_voice

"""
This is the entry point of my AI engine.
It is meant to call the various functions
under various modules. 

voice synthesis - pyttsx
"""

def main():
    test_voice("this is the first utterance of the bot")
    
if __name__ == '__main__':
    main()
