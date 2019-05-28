'''
Jorge Alejandro González Guerra
1889169
'''

from tkinter import Tk, Canvas
import sys

root = Tk()
c = Canvas(root, width=280, height=280)

colors = {
    'a': '#ffff00',
    'c': '#00ffff',
    'd': '#ffcc66',
    'm': '#800080',
    'r': '#ff0000',
    'v': '#00bb00'
}

file = open('data.txt')
lines = file.readlines()

# c.create_rectangle(0,0,20,20,fill="#ff0000",outline="")

for ln, line in enumerate(lines):
    for cn, char in enumerate(line):
        if char == '\n':
            continue
        if char not in colors:
            print('[Error] Unknown color \'%s\' at line %s:%s' % (char, ln, cn))
            quit(1)
        color = colors[char]
        print('(%s, %s) %s: %s' % (cn*20, ln*20, char, color))
        c.create_rectangle(cn * 20, ln * 20, (cn+1)*20, (ln+1)*20, fill=color, outline='')

c.pack()
c.mainloop()
