# Common utils 

import math

def det(A, B):
    """ Определитель матрицы, составленной из вектор-столбцов A и B """
    return A[0] * B[1] - A[1] * B[0]

def norm(u):
    """ Норма вектора u"""
    return math.sqrt(u[0] * u[0] + u[1] * u[1])

def normsq(u):
    """ Квадрат нормы вектора u """
    return (u[0]**2 + u[1]**2)

def proj(u, v):
    """ Проекция вектора v на вектор u"""
    d = (u[0] * v[0] + u[1] * v[1]) / (norm(u)**2)
    return (u[0] * d, u[1] * d)
    
    

def find_in(points, comp, index=0):
    """ Данная функция выполняет поиск в списке poinst, используя для сравнения функцию comp двух переменных """

    p = points[index]
    
    for point in points:
        if comp(p, point):
            p = point
    
    return p

def rotate(a, b, c):
    """ Данная функция определяет ориентацию поворота для векторов, построенных на трех точках (векторов ab и bc) """
    u = (b[0] - a[0], b[1] - a[1])
    v = (c[0] - b[0], c[1] - b[1])
    
    return det(u, v)
    
def min_point(p, prev, points):
    """ Данная функция находит минимальную (по величине полярного угла относительно точки p и нормированной нормали к вектору p - prev) точку в списке points """
    a = (p[0] - prev[0], p[1] - prev[1])
    u = (-a[1] / norm(a), a[0] / norm(a))
    res = points[0]
    v = (res[0] - p[0], res[1] - p[1])
    d = det(u, v) / norm(v)

    for point in points:
        v = (point[0] - p[0], point[1] - p[1])
        normv = norm(v)
        
        if normv == 0:
            continue
        
        new_d = det(u, v) / normv
        if new_d < d:
            res = point
            d = new_d
        elif new_d == 0:
            if normsq(v) > normsq(res):
                res = point
                d = new_d
            
            
    return res

def sort(p, vec, points):
    """ Данная функция сортирует точки в списке points по полярному углу относительно точки p и вектора vec (используется встроенная сортировка из python со сложностью O(nlogn)) """
    key = lambda point: det(vec, (point[0] - p[0], point[1] - p[1])) / norm((point[0] - p[0], point[1] - p[1])) 
    
    points = sorted(points, key=key)
    return points

def dist(A, B, a):
    """ Расстояние между прямой AB до точки a """
    u = (B[0] - A[0], B[1] - A[1])
    v = (a[0] - A[0], a[1] - A[1])
    
    return abs(det(u, v) / (norm(u)))
    
    