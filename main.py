import matplotlib.pyplot as plt
import sys

from jarv import jarv_alg
from graham import graham_alg
from quickhull import quick_alg
import utils


def plot(hull, points):
        plt.plot([p[0] for p in hull], [p[1] for p in hull], 'b-')
        plt.plot([p[0] for p in points], [p[1] for p in points], 'ko')
        plt.plot(hull[0][0], hull[0][1], 'ro')
        plt.show()

def main(*args, **kwargs):
    # Первым аргументом командной строки передаем имя файла (относительный путь) с точками 
    # (каждая строка одна точка, координаты через пробел, комментарии начинаются с #, если какие-то точки нажо убрать)
    # Вторым аргументом передаем название алогоритма
    # Алгоритмы: jarvis (алгоритм Джарвиса), graham (алгоритм Грэхэма), quick (алгоритм Быстрая оболочка) (ввод не чувствителен к регистру)
    
    file_path = args[0]
    alg_name = args[1]
    points = []
    hull = []
    
    with open(file_path, 'r') as f:
        for line in f.readlines():
            if line[0] == '#': 
                continue
            ptlist = line.split()
            points.append((float(ptlist[0]), float(ptlist[1])))


    alg = alg_name.lower()
    if alg == 'jarvis':
        hull = jarv_alg(points)
    elif alg == 'graham':
        hull = graham_alg(points)
    elif alg == 'quick':
        hull = quick_alg(points)
    else:
        print("Error: alg w/ name {0} doensn't supported".format(alg))
        return

    plot(hull, points)
    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
