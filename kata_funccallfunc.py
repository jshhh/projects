class Mycall:
    def __init__(self, n):
        print ('construct',n)
        self.n = n

    def __call__(self,n):
        return Mycall(n+self.n)

    def __eq__(self, other):
        if isinstance(other,int):
            return self.n == other

    def __add__(self, other):
        if isinstance(other,int):
            return Mycall(self.n + other)

    def __neg__(self):
        return Mycall(-self.n)

    def __sub__(self, other):
        return Mycall(self.n+(-other))

def abc(n):
    x = Mycall(n)
    return x


print(abc(2)(3)==5)