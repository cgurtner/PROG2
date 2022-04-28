import pandas as pd

points = pd.DataFrame(
    {'Points': [80, 93, 78, 85, 97, 75, 88, 91]},
    index=['LA2', 'PM2', 'PROG2', 'AN2', 'PHYS2', 'BWP2', 'COM2', 'WAHR']
)

print('The Points obtained by student are', points, sep='\n')

# Aufgabe 2
print('\nAufgabe 2\n')
print(points['Points']['PROG2'])
print(points.Points.PROG2)

# Aufgabe 3
print('\nAufgabe 3\n')
print(points['Points'].mean())
print(points.Points.mean())

# Aufgabe 4
print('\nAufgabe 4\n')
print(round(points['Points'].mean()))

# Aufgabe 5
print('\nAufgabe 5\n')
print(points['Points'].nlargest(n=3))

# Aufgabe 6
print('\nAufgabe 6\n')
points['Grade'] = (points['Points']*5 / 100) + 1
print(points)
