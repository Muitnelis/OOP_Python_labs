class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self.author  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    # вместо set_pages используется метод pages и @pages.setter
    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает длительность аудиокниги."""
        return self.duration

    # вместо set_duration используется метод duration и @duration.setter
    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает длительность аудиокниги."""
        if not isinstance(new_duration, float):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом")
        self.duration = new_duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.pages!r})"
