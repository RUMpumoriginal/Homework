class CandyStash:
    def_max_count = 50
    max_count = 0

    def __init__(self, count, max_count = None):
        
        if max_count == None:
            self.max_count = self.def_max_count
        else:
            self.max_count = max_count
        self.count = count
    

    @staticmethod
    def validate_amount(value):
        if value < 0 or not isinstance(value, int):
            raise ValueError("Від'ємне значення цукерок!!!")


    @classmethod
    def full_stash(cls, max_count = None):
        if max_count == None:
            capacity = cls.def_max_count
        else:
            capacity = max_count
        return cls(capacity, max_count=capacity)
    

    @property
    def count(self):
        return self._value
    

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._value = min(value, self.max_count)


    def __str__(self):
        return f"CandyStash ({self.count}/{self.max_count})"


    def __add__(self, other):
        if isinstance(other, int):
            self.count += other
            return self
        return NotImplemented
    

    def __sub__(self, other):
        if isinstance(other, int):
            self.count = max(self.count - other, 0)
            return self
        return NotImplemented
    

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return f"{max(self._value, other._value)} have more candies then {min(self._value, other._value)}"
        elif isinstance(other, int):
            return f"{max(self._value, other)} more then {min(self._value, other)}"
        return NotImplemented





