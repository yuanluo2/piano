from tkinter import *
from pygame import mixer

root = Tk()
root.geometry('1370x300')
root.resizable(height = False, width = False)
root.title('钢琴')

mixer.init()
mixer.set_num_channels(16)

key_sounds_mapping = {
    '1': mixer.Sound('audio/a49.mp3'),
    '2': mixer.Sound('audio/a50.mp3'),
    '3': mixer.Sound('audio/a51.mp3'),
    '4': mixer.Sound('audio/a52.mp3'),
    '5': mixer.Sound('audio/a53.mp3'),
    '6': mixer.Sound('audio/a54.mp3'),
    '7': mixer.Sound('audio/a55.mp3'),
    '8': mixer.Sound('audio/a56.mp3'),
    '9': mixer.Sound('audio/a57.mp3'),
    '0': mixer.Sound('audio/a48.mp3'),
    'q': mixer.Sound('audio/a81.mp3'),
    'w': mixer.Sound('audio/a87.mp3'),
    'e': mixer.Sound('audio/a69.mp3'),
    'r': mixer.Sound('audio/a82.mp3'),
    't': mixer.Sound('audio/a84.mp3'),
    'y': mixer.Sound('audio/a89.mp3'),
    'u': mixer.Sound('audio/a85.mp3'),
    'i': mixer.Sound('audio/a73.mp3'),
    'o': mixer.Sound('audio/a79.mp3'),
    'p': mixer.Sound('audio/a80.mp3'),
    'a': mixer.Sound('audio/a65.mp3'),
    's': mixer.Sound('audio/a83.mp3'),
    'd': mixer.Sound('audio/a68.mp3'),
    'f': mixer.Sound('audio/a70.mp3'),
    'g': mixer.Sound('audio/a71.mp3'),
    'h': mixer.Sound('audio/a72.mp3'),
    'j': mixer.Sound('audio/a74.mp3'),
    'k': mixer.Sound('audio/a75.mp3'),
    'l': mixer.Sound('audio/a76.mp3'),
    'z': mixer.Sound('audio/a90.mp3'),
    'x': mixer.Sound('audio/a88.mp3'),
    'c': mixer.Sound('audio/a67.mp3'),
    'v': mixer.Sound('audio/a86.mp3'),
    'b': mixer.Sound('audio/a66.mp3'),
    'n': mixer.Sound('audio/a78.mp3'),
    'm': mixer.Sound('audio/a77.mp3'),

    'Q': mixer.Sound('audio/b49.mp3'),
    'W': mixer.Sound('audio/b50.mp3'),
    'E': mixer.Sound('audio/b52.mp3'),
    'R': mixer.Sound('audio/b53.mp3'),
    'T': mixer.Sound('audio/b54.mp3'),
    'Y': mixer.Sound('audio/b56.mp3'),
    'U': mixer.Sound('audio/b57.mp3'),
    'I': mixer.Sound('audio/b81.mp3'),
    'O': mixer.Sound('audio/b87.mp3'),
    'P': mixer.Sound('audio/b69.mp3'),
    'A': mixer.Sound('audio/b84.mp3'),
    'S': mixer.Sound('audio/b89.mp3'),
    'D': mixer.Sound('audio/b73.mp3'),
    'F': mixer.Sound('audio/b79.mp3'),
    'G': mixer.Sound('audio/b80.mp3'),
    'H': mixer.Sound('audio/b83.mp3'),
    'J': mixer.Sound('audio/b68.mp3'),
    'K': mixer.Sound('audio/b71.mp3'),
    'L': mixer.Sound('audio/b72.mp3'),
    'Z': mixer.Sound('audio/b74.mp3'),
    'X': mixer.Sound('audio/b76.mp3'),
    'C': mixer.Sound('audio/b90.mp3'),
    'V': mixer.Sound('audio/b67.mp3'),
    'B': mixer.Sound('audio/b86.mp3'),
    'N': mixer.Sound('audio/b66.mp3')
}

key_gamut_mapping = {
    '1': 'C2',
    '2': 'D2',
    '3': 'E2',
    '4': 'F2',
    '5': 'G2',
    '6': 'A2',
    '7': 'B2',
    '8': 'C3',
    '9': 'D3',
    '0': 'E3',
    'q': 'F3',
    'w': 'G3',
    'e': 'A3',
    'r': 'B3',
    't': 'C4',
    'y': 'D4',
    'u': 'E4',
    'i': 'F4',
    'o': 'G4',
    'p': 'A4',
    'a': 'B4',
    's': 'C5',
    'd': 'D5',
    'f': 'E5',
    'g': 'F5',
    'h': 'G5',
    'j': 'A5',
    'k': 'B5',
    'l': 'C6',
    'z': 'D6',
    'x': 'E6',
    'c': 'F6',
    'v': 'G6',
    'b': 'A6',
    'n': 'B6',
    'm': 'C7',
    'Q': 'C#2',
    'W': 'D#2',
    'E': 'F#2',
    'R': 'G#2',
    'T': 'A#2',
    'Y': 'C#3',
    'U': 'D#3',
    'I': 'F#3',
    'O': 'G#3',
    'P': 'A#3',
    'A': 'C#4',
    'S': 'D#4',
    'D': 'F#4',
    'F': 'G#4',
    'G': 'A#4',
    'H': 'C#5',
    'J': 'D#5',
    'K': 'F#5',
    'L': 'G#5',
    'Z': 'A#5',
    'X': 'C#6',
    'C': 'D#6',
    'V': 'F#6',
    'B': 'G#6',
    'N': 'A#6'
}

i = 1
n = 1
black_x_pos = 22
key_button_mapping = {}
for key in key_sounds_mapping.keys():
    if not key.isupper():
        key_button_mapping[key] = Button(root, height = 15, width = 4, bg = 'white', text = key_gamut_mapping[key] + '\n' + key, anchor = 's')
        key_button_mapping[key].grid(row = 0, column = i)
        i += 1
    else:
        key_button_mapping[key] = Button(root, height = 6, width = 3, bg = 'black', text = key_gamut_mapping[key] + '\n' + key, anchor = 's', fg = 'white')
        key_button_mapping[key].place(x = black_x_pos, y = 0)
        
        res = n % 5
        if res == 1 or res == 3 or res == 4:
            black_x_pos += 38
        else:
            black_x_pos += 76
        n += 1
    


def KeyPressed(event):
    key_sounds_mapping[event.keysym].play()
    key_button_mapping[event.keysym].flash()

root.bind("<Key>", KeyPressed)
root.mainloop()