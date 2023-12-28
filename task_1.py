import doctest

class Book:
    def __init__(self, title: str, author: str, genre: str, publication_year: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param genre: Жанр книги
        :param publication_year: Год публикации книги

        Примеры:
        >>> book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self.author = author

        if not isinstance(genre, str):
            raise TypeError("Жанр книги должен быть типа str")
        self.genre = genre

        if not isinstance(publication_year, int):
            raise TypeError("Год публикации должен быть типа int")
        """
        Проверка на неотрицательность отстутствует,
        так как потенциально книга может быть издана
        до нашей эры
        """
        self.publication_year = publication_year

    def get_book_info(self) -> str:
        """
        Получение информации о книге

        :return: Информация о книге

        Примеры:
        >>> book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        >>> book.get_book_info()
        """
        ...

    def author_check(self, name: str) -> bool:
        """
        Проверка на авторство - совпадает ли имя аргумента с автором книги

        :return: Ответ на вопрос

        Примеры:
        >>> book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925)
        >>> book.author_check("F. Scott Fitzgerald")
        """
        ...


class Animal:
    def __init__(self, name: str, place: list(str), danger: bool, endangered: bool, individuals: int):
        """
        Создание и подготовка к работе объекта "Животное"

        :param name: Название животного
        :param place: Список мест обитания
        :param danger: Индикатор хищника
        :param endangered: Индикатор вымирания
        :param individuals: Количество особей

        Примеры:
        >>> amur_tiger = Animal("Amur tiger", ["Russian Far East", "Northeast China", "North Korea"], True, True, 600)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Название животного должно быть типа str")
        self.name = name

        if not isinstance(place, list):
            raise TypeError("Список мест обитания должен быть типа list")
        self.place = place

        if not isinstance(danger, bool):
            raise TypeError("Индикатор хищника должен быть типа bool")
        self.danger = danger

        if not isinstance(endangered, bool):
            raise TypeError("Индикатор вымирания должен быть типа bool")
        self.endangered = endangered

        if not isinstance(individuals, int):
            raise TypeError("Количество особей должно быть типа int")
        if individuals < 0:
            raise ValueError("Количество особей должно быть неотрицательным числом")
        self.individuals = individuals

    def place_compare(self, places: list(str)) -> list(str):
        """
        Функция, которая выбирает из передаваемого списка мест те, которые
        соответствуют местам обитания данного животного

        :return: Список подходящих мест

        Примеры:
        >>> amur_tiger = Animal("Amur tiger", ["Russian Far East", "Northeast China", "North Korea"], True, True, 600)  # инициализация экземпляра класса
        >>> places = ["North Korea", "South America", "Norway"]
        >>> amur_tiger.place_compare(places)
        """
        ...

    def update_individuals(self, places: dict()) -> None:
        """
        Функция, получает на вход словарь с обновленными данными
        о кличестве особей в разных местах обитания и изменяет
        параметр individuals.

        :return: None

        Примеры:
        >>> amur_tiger = Animal("Amur tiger", ["Russian Far East", "Northeast China", "North Korea"], True, True, 600)  # инициализация экземпляра класса
        >>> data = {"place_1": 200, "place_2": 300, "place_3": 20, "place_4": 100, }
        >>> amur_tiger.update_individuals(data)
        """
        ...


class Character:
    def __init__(self, x: int, y: int, hp: int, bag: list(str)):
        """
        Создание и подготовка к работе объекта "Персонаж"

        :param x: Координата Х
        :param y: Координата Y
        :param hp: Количество жизней
        :param bag: Список предметов в сумке

        Примеры:
        >>> nagibator = Character(0, 0, 100, ["Меч тысячи истин"])  # инициализация экземпляра класса
        """
        if not isinstance(x, int):
            raise TypeError("Координата Х должна быть типа int")
        self.x = x

        if not isinstance(y, int):
            raise TypeError("Координата Y должна быть типа int")
        self.y = y

        if not isinstance(hp, int):
            raise TypeError("Количество жизней должно быть типа int")
        if hp < 0:
            raise ValueError("Количество жизней должно быть неотрицательным числом")
        self.hp = hp

        if not isinstance(bag, list):
            raise TypeError("Список предметов в сумке должен быть типа list")
        self.bag = bag


    def run(self, x, y) -> None:
        """
        Перемещение персонажа на новые координаты

        :return: None

        Примеры:
        >>> nagibator = Character(0, 0, 100, ["Меч тысячи истин"])  # инициализация экземпляра класса
        >>> nagibator.run(1, 1)
        """
        ...

    def robbed(self) -> None:
        """
        Убирает из списка вещей в сумке случайную вещь

        :return: None

        Примеры:
        >>> nagibator = Character(0, 0, 100, ["Меч тысячи истин"])  # инициализация экземпляра класса
        >>> nagibator.robbed()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации