import random

def sort(a):
  for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            temp = a[j]; a[j] = a[j+1]; a[j+1] = temp

balls = [random.randint(10, 100) for p in range(0, 10)]

sort(balls)
print(balls)