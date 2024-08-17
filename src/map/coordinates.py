class Coordinates:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __repr__(self):
        return f'x: {self.__x}, y: {self.__y}'
