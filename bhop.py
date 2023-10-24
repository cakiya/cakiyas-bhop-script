"""
REQUIRES:
https://pypi.org/project/keyboard/
pip install keyboard  
python -m pip install keyboard
"""
import keyboard

spamming = False
def spam_space_16(spam):
    spamming = spam
    while spamming:
        print("test")

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        spam_space_16(True)
    if event.event_type == keyboard.KEY_UP and event.name == 'space':
        space_spam_16(False)