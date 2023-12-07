from finiteFields  import FieldElement
from ellipticCurves import Point


a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)

print(a + b == c)
print(a == a)