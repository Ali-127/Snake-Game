import random


class Food:
    def __init__(self):
        self.position = [200, 200]

    def regenerate(self, width, height, block_size):
        # generate random positions
        x = round(random.randrange(0 + block_size, width - block_size) / 10.0) * 10.0
        y = round(random.randrange(0 + block_size, height - block_size) / 10.0) * 10.0
        self.position = [x, y]
