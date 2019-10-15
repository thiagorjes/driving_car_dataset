import argparse 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def main(i,args):
    f = open(args)

    lines  = [line.rstrip("\n") for line in f.readlines()]
    numbers = {'1','2','3','4','5','6','7','8','9'}

    iters = []
    loss = []
    prev_line = ""
    for line in lines:
        args = line.split(' ')
        if args[0][-1:]==':' and args[0][0] in numbers :
            iters.append(int(args[0][:-1]))            
            loss.append(float(args[2]))
    ax.clear()
    ax.plot(iters,loss)
    plt.xlabel('iters')
    plt.ylabel('loss')
    plt.grid()

fig,ax = plt.subplots()

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig,main,interval=1000,fargs=[sys.argv[1]])
    plt.show()
