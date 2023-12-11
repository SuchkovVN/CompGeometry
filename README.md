# Как работает

Чтобы запустить просчет выполните команду:
```
python main.py <файл-с-точками> <алгоритм>
```
Например:
```
python main.py points.py quick
```
### Алгоритмы:

* алгоритм Джарвиса - jarvis
* алгоритм Грэхэма - graham
* алгоритм Быстрая оболочка - quick

Формат файла с точками: каждая строка - одна точка. Координаты через пробел. Комментарии начинаются с #. Расширение файла особой роли не играет (как вариант .txt или .py)
Пример:
```
1.3 2.6
1.65 3.7
1.4 2
1.89 3
# 4.2 5.1 <- данная точка будет пропущена программой
```