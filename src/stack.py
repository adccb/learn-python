class Stack():
    array = []
    def push(self, data):
        self.array.append(data)
    def pop(self):
        m = self.array[-1]
        del self.array[-1]
        return m
    def to_array(self):
        return self.array
