# environment.py
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def limit_position(self, x, y):
        # Wrap around when agent goes out of bounds
        if x < 0:
            x = self.width
        elif x > self.width:
            x = 0
        if y < 0:
            y = self.height
        elif y > self.height:
            y = 0
        return x, y
