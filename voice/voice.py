import pyttsx
def test_voice(test_phrase):
    engine = pyttsx.init()
    engine.say(test_phrase)
    engine.runAndWait()
    
def test_console():
    pass
