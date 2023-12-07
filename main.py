class FieldElement:

        def _init_(self, num, prime):
                if num >= prime or num < 0:
                        error = 'Num {} not in filed range 0 to {}'.format(num, prime -1)
                        raise ValueError(error)
                self.num = num
                self.prime - prime

        
        def _repr_(self):
                return 'FieldElement_{}({})'.format(self.prime, self.num)
        
        
        def _eq_(self, other):
                if other is None:
                        return False
                return self.num == other.num and self.prime == other.prime
        

        def _add_(self, other):
                if self.prime != other.prime:
                        raise TypeError('Cannot add numbers in different fields')
                num = (self.num + other.num) % self.prime
                return self._class_(num, self.prime)

        def _sub_(self, other):
                if self.prime != other.prime:
                        raise TypeError('Cannot subtract numbers in different fields')
                num = (self.num - other.num) % self.prime
                return self._class_(num, self.prime)
        
        def _mul_(self, other):
                if self.prime != other.prime:
                        raise TypeError('Cannot multiply numbers in different fields')
                num = (self.num * other.num) % self.prime
                return self._class_(num, self.prime)
        
        def _pow_(self, other):
                n = exponent
                while n < 0:
                    n += self.prime -1
                num = pow(self.num, n, self.prime)
                return self._class_(num, self.prime)
        

