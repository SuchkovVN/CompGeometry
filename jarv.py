# Jarvis algorithm

from utils import det, find_in, min_point

def jarv_alg(points):
    Points = points.copy()
    res = []
    # Находим самую левую точку, добовляем её в оболочку и удаляем её из списка точек
    res.append(find_in(Points, lambda u, v: u[0] > v[0]))

    # Находим минимальную по полярному углу точку отн. первой точки в оболочке, удаляем её из списка точек.
    p = min_point(res[0], (res[0][0], res[0][1] -1.), Points)
    Points.remove(p)
    
    # Пока оболочка не замкнулась, ищем минимальную точку по отношению к предыдущей, добавляем её в оболочку и удаляем из списка точек
    while p != res[0]:
        res.append(p)
        p = min_point(p, res[-2], Points)
        Points.remove(p)
    
    # Добавим в конец первую точку, чтобы первая и последняя точки списка совпадали (замкнутость оболочки уже была определена выше, так что это просто формальность для рисунка)
    res.append(res[0])
    return res



