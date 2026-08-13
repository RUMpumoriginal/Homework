class MoneyBox:
    def __init__(self, n):
        self.m = 0
        self.n = n
        

    def can_add(self, v):
        if isinstance(v, int):
            if self.m:
                if self.m + v <= self.n:
                    return True
                else:
                    return False
            elif v < self.n:
                return True
            else:
                return False
        else:
            return False


    def __add__(self, k):
        if self.can_add(k):
            self.m += k
            return self
        return NotImplemented

