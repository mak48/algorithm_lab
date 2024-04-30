from time import perf_counter
import pandas as pd
import matplotlib.pyplot as plt
from simple import *
from map_alg import *
from pers_tree import *

def draw(col_name):
    data = pd.read_csv("results.csv")
    grouped_data = data.groupby('name')
    plt.figure(figsize=(10, 6))
    for name, group in grouped_data:
        plt.plot(group['rect'], group[col_name], label=name)
    plt.xlabel('кол-во прямоугольников')
    plt.ylabel(col_name + ' время в секундах')
    plt.legend()
    plt.show()
draw("prep")
draw("result")
draw("full")

def tester_simple():
    for i in range(11):
        minutes = 0
        write_rect(2 ** i)
        for i in range(10):
            start = float(perf_counter())
            enumeration(2 ** i, 100000)
            minutes += float(perf_counter()) - start
        minutes /= 10
        print(2 ** i, minutes)
def tester_map_1():
    for i in range(10):
        minutes = 0
        write_rect(2 ** i)
        for i in range(10):
            start = float(perf_counter())
            prepare_map(2 ** i)
            minutes += float(perf_counter())-start
        minutes /= 10
        print(2**i, minutes)
def tester_map_2():
    for i in range(10):
        minutes = 0
        write_rect(2 ** i)
        for i in range(10):
            k, x, y = prepare_map(2 ** i)
            start = float(perf_counter())
            solver_map(100000, k, x, y)
            minutes += float(perf_counter()) - start
        minutes /= 10
        print(2**i, minutes)
def tester_tree_1():
    for i in range(11):
        minutes = 0
        write_rect(2 ** i)
        for i in range(10):
            start = float(perf_counter())
            prepare_tree(2 ** i)
            minutes += float(perf_counter()) - start
        minutes /= 10
        print(2 ** i, minutes)
def tester_tree_2():
    for i in range(11):
        minutes = 0
        write_rect(2 ** i)
        for i in range(10):
            k, x, y = prepare_tree(2 ** i)
            start = float(perf_counter())
            solver_tree(100000, k, x, y)
            minutes += float(perf_counter())-start
        minutes /= 10
        print(2 ** i, minutes)
def write_rect(n):
    f = open("прямоугольники.txt", "w")
    for i in range(n):
        f.write(str(10*i) + " "+str(10*i)+" "+str(10*(2*n-i))+" "+str(10*(2*n-i))+"\n")
def write_p(n):
    f = open("точки.txt", "w")
    for i in range(n):
        f.write(str(pow(1009 * i,31)%(20*n))+" "+str(pow(1013 * i, 31) % (20 * n)) + "\n")