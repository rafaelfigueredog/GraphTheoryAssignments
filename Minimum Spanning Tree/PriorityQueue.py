class PriorityQueue:
  
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        minimo = 0
        if( self.isEmpty() ):
            return
        for i in range(1,len(self.items)):
            if self.items[i] < self.items[minimo]:
                minimo = i
        item = self.items[minimo]
        self.items[minimo:minimo+1] = []
        return item

    def __str__(self):
        fila =  str(self.items)
        return fila
