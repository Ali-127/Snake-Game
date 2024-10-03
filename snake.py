class Snake:
    def __init__(self):
        self.body = []
        self.reset()

    def move(self, direction):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1].copy()  # without using copy the same list is referencing

        # increment head position with given directions
        self.body[0][0] += direction[0]
        self.body[0][1] += direction[1]

    def grow(self):
        self.body.append(self.body[-1])  # grow snake

    def reset(self):
        self.body = [[250, 100], [240, 100], [230, 100]]  # reset snake to first position
