# Quick Hull algorithm

from utils import find_in, det, dist
import math

def quick_hull_helper(S, P, Q, hull):
    # Базовый случай: список на входе пуст
    if not S:
        return

    # Ищем самую удаденную от прямой PQ точку среди S
    farest = S[0]
    d = dist(P, Q, farest)
    for point in S:
        new_dist = dist(P, Q, point)
        if new_dist > d:
            d = new_dist
            farest = point
    
    # Добовляем найденную точку в оболочку после точки P
    hull.insert(hull.index(P) + 1, farest)
    
    # Делим S на два подмножества
    # S1 - все точки лежащие слева от PC (C - наиболее удаленная от PQ из пункта выше)
    # S2 - все точки лежащие слева от CQ
    S1 = []
    S2 = []
    pf = (farest[0] - P[0], farest[1] - P[1])
    fq = (Q[0] - farest[0], Q[1] - farest[1])
    for p in S:
        if det(pf, (p[0] - P[0], p[1] - P[1])) > 0:
            S1.append(p)
        elif det(fq, (p[0] - farest[0], p[1] - farest[1])) > 0:
            S2.append(p)

    # Рекурсивно вызываем функцию для S1 и S2
    quick_hull_helper(S1, P, farest, hull)
    quick_hull_helper(S2, farest, Q, hull)
    
    
    
        
    

def quick_alg(points):
    res = []
    S  = points.copy()
    
    # Находим самую правую и самую левую точки (L и R). Добовляем их в оболочку
    leftmost = find_in(S, comp=lambda u, v: u[0] > v[0])
    rightmost = find_in(S, comp=lambda u,v: u[0] < v[0])
    res.append(leftmost)
    res.append(rightmost)
    
    # Поделим исходное множество точек на два: S1 множество точек, находящихся слева от прямой LR
    # Множество точек S2, находящихся справа от LR
    lr = (rightmost[0] - leftmost[0], rightmost[1] - leftmost[1]) # LR vector
    S1 = [] # left from LR
    S2 = [] # Right from LR
    for p in S:
        u = (p[0] - leftmost[0], p[1] - leftmost[1])
        d = det(lr, u)
        if d > 0:
            S1.append(p)
        elif d < 0:
            S2.append(p)
    
    # Рекурсивно вызываем вспомогательную функцию к S1 и S2
    quick_hull_helper(S1, leftmost, rightmost, res)
    quick_hull_helper(S2, rightmost, leftmost, res)

    # Замыкаем список точек для рисунка
    res.append(res[0])
    return res
            
          
    

