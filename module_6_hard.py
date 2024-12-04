class Figure:
    sides_count = 0

    def __init__(self, __sides,  __color, filled):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b
        else:
            return self.__color

