class Book:
    title = "Название"
    author = "Автор"
    year = "Год издания"

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"


class Circle:
    def __init__(self, radius=0):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if isinstance(radius, (int, float)) and radius >= 0:
            self.__radius = radius
        else:
            raise ValueError


book = Book()
book.title = "Грокаем алгоритмы"
book.author = "Бхаргава"
book.year = 2017
print(book.get_info())

circle = Circle()
circle.set_radius(12)
circle.set_radius(1.23)
# circle.set_radius(-234)
# circle.set_radius("sdf")
