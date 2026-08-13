class Buffer:
    def __init__(self):
        self.data = []


    def add(self, *a):
        for item in a:
            if isinstance(item, (list, tuple)):
                self.data.extend(item)
            else:
                self.data.append(item)


        while len(self.data) >= 5:
                    current_sum = sum(self.data[:5])
                    print(current_sum)
                    self.data = self.data[5:]


    def get_current_part(self):
        return self.data

