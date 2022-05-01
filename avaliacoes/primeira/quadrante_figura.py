import math

p1x, p1y = input().split()
p2x, p2y = input().split()
p3x, p3y = input().split()
p4x, p4y = input().split()

p1x, p1y = int(p1x), int(p1y)
p2x, p2y = int(p2x), int(p2y)
p3x, p3y = int(p3x), int(p3y)
p4x, p4y = int(p4x), int(p4y)

if (p1x > 0) and (p1y > 0) and (p2x > 0) and (p2y > 0) and (p3x > 0) and (p3y > 0) and (p4x > 0) and (p4y > 0):
    print("S")
else:
    print("N")

lado = math.sqrt((p1x - p2x)**2 + (p1y - p2y)**2)

print("{:.2f}". format(lado * lado))
