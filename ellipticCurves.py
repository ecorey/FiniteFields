class Point:

    # y^2 = x^3 + ax + b
    # y^2 = x^3 + 5x + 7
    def _init_(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) are not ion the curve'.format(x, y))
        
    
    def _eq_(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b
    

    def _ne_(self, other):
        return not (self == other)
    
    
    def _add_(self, other):

        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {} and {} are not on the same curve'.format(self, other))

        if self.x is None:
            return other
        if other.x is None:
            return self
        
        if self == other and self.y == 0 * self.x:
            return self._class_(None, None, self.a, self.b)
        