from turtle import *
clist = ['red', 'blue', 'green']
llist = len(clist)
for i, j in enumerate(clist):
    color(j)
    forward(100)
mainloop()