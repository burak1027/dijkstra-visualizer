import tkinter
from tkinter import *

import networkx
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


import  main as mn

def draw():
    N = int(t1.get())
    S = int(t2.get())
    D = int(t3.get())
    nodes = mn.createNode(N)
    accesibleNodes = mn.graph(nodes)
    list2 = mn.dijks(N, S, D)
    list2[0].reverse()
    t4.insert(END,str(list2[1]))
    t5.insert(END,str(list2[2]))
    t6.insert(END,str(list2[0]))


    visualize(accesibleNodes, list2[0])

def visualize(accesibleNodes,path):
    root = tkinter.Tk()
    root.wm_title("Embedding in TK")

    f = plt.figure()
    a = f.add_subplot(111)
    G = networkx.Graph()
    red_nodes=[]
    for i in range(len(path)-1,0,-1):
        red_nodes.append((path[i-1],path[i]))
    for i in range(len(accesibleNodes)):
        G.add_node(i,pos=(i-(i%2),(-(i%2))+0.2))
        count=0
    for i in accesibleNodes:
        for j in i:
            G.add_edge(count,j)
        count+=1
    pos=networkx.get_node_attributes(G,'pos')
    networkx.draw(G,pos,with_labels=1,ax=a)
    networkx.draw_networkx_edges(G,pos,ax=a,edgelist=red_nodes,edge_color='r')
    plt.ylim(-2, 2)
    canvas = FigureCanvasTkAgg(f, master=root)
    # canvas.show()
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    #
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    canvas.draw()
    # canvas = FigureCanvasTkAgg(f, master=root)
    # # canvas.get_tk_widget().grid(row=20, column=20)
    # # canvas.draw()
    # toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    # toolbar.update()
    # canvas.get_tk_widget().pack()
    # canvas.get_tk_widget().pack(side=LEFT, fill=NONE)

    # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    return f
def drawNodes():
    draw()

    return 0

window=Tk()
lbl1 = Label( text='Number of nodes')
lbl2 = Label(text='Start')
lbl3 = Label(text='Destination')
lbl4=Label(text='Running Time')
lbl5=Label(text='Cost')
lbl6 = Label(text='path')
t1 = Entry(bd=4)
t2 = Entry()
t3 = Entry()
t4= Entry()
t5= Entry()
t6= Entry()

tn1 = Button(text='draw path')
btn2 = Button( text='draw complexity')
lbl1.place(x=10, y=50)
t1.place(x=120, y=50)
lbl6.place(x=250, y=50)
t6.place(x=350, y=50)
lbl2.place(x=10, y=100)
t2.place(x=120, y=100)
lbl4.place(x=250, y=100)
t4.place(x=350, y=100)
lbl3.place(x=10, y=150)
t3.place(x=120, y=150)
lbl5.place(x=250, y=150)
t5.place(x=350, y=150)
b1 = Button( text='draw path',command=drawNodes)
b1.place(x=10, y=200)
window.title('Dijkstra Algorithm')
window.geometry("500x400")
window.mainloop()


