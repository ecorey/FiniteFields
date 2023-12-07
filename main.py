from finiteFields  import FieldElement
from ellipticCurves import Point


a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)

# print(a + b == c)
# print(a == a)

p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(None, None, 5, 7)

x = p1 + inf
print(x.x, x.y)