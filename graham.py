# Graham algorithm

from utils import det, find_in, sort, rotate

def graham_alg(points):
    Points = points.copy()
    n = len(Points)
    res = []
    # Ищем самую левую точку и добовляем в оболочку. Удаляем эту точку из списка точек
    res.append(find_in(Points, lambda u, v: u[0] > v[0]))
    Points.remove(res[0])
    
    # Сортируем точки относительно первой точки и вектора нормали к оси Оу в оболочке по полярному углу 
    Points = sort(res[0], (1.0, 0.), Points)
    res.append(Points[0])
    
    # В цикле перебираем точки списка
    j = 1
    for i in range(0, n - 1):
        # Выбираем очережную точку
        t = Points[i]
        
        # В случае, если точки образуют левый поворот, удаляем j-ую точку оболочки. Проходимся так по всем j до j = 1
        while rotate(res[j - 1], res[j], t) <= 0 and j > 0:
            res.pop(j)
            j = j - 1
        
        # Добовляем t в оболочку
        res.append(t)
        j = j + 1
    
    # Замыкаем список точек оболочки для рисунка
    res.append(res[0])
    return res