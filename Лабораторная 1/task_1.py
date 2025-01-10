# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    from abc import ABC, abstractmethod


    class Furniture(ABC):
        def __init__(self, material: str, height: float, width: float):
            """
            Инициализация объекта класса Furniture.

            :param material: Материал, из которого изготовлена мебель. Должен быть строкой.
            :param height: Высота мебели в сантиметрах. Должен быть положительным числом.
            :param width: Ширина мебели в сантиметрах. Должен быть положительным числом.

            :raises ValueError: Если height или width не положительные числа.

            >>> table = Furniture('дерево', 75, 120)
            >>> table.material
            'дерево'
            """
            if height <= 0 or width <= 0:
                raise ValueError("Height and width must be positive numbers.")
            self.material = material
            self.height = height
            self.width = width

        @abstractmethod
        def assemble(self) -> None:
            """
            Собрать мебель.

            :return: None

            >>> table = Furniture('дерево', 75, 120)
            >>> table.assemble()  # Пример вызова метода
            """
            ...

        @abstractmethod
        def disassemble(self) -> None:
            """
            Разобрать мебель.

            :return: None

            >>> table = Furniture('дерево', 75, 120)
            >>> table.disassemble()  # Пример вызова метода
            """
            ...


    class Tree(ABC):
        def __init__(self, species: str, age: int, height: float):
            """
            Инициализация объекта класса Tree.

            :param species: Вид дерева. Должен быть строкой.
            :param age: Возраст дерева в годах. Должен быть неотрицательным целым числом.
            :param height: Высота дерева в метрах. Должен быть положительным числом.

            :raises ValueError: Если age отрицательное число или height не положительное.

            >>> oak = Tree('дуб', 50, 20.5)
            >>> oak.species
            'дуб'
            """
            if age < 0 or height <= 0:
                raise ValueError("Age must be non-negative and height must be positive.")
            self.species = species
            self.age = age
            self.height = height

        @abstractmethod
        def grow(self, years: int) -> None:
            """
            Увеличить высоту дерева на заданное количество лет.

            :param years: Количество лет для роста. Должен быть неотрицательным целым числом.

            :return: None

            >>> oak = Tree('дуб', 50, 20.5)
            >>> oak.grow(5)  # Пример вызова метода
            """
            ...

        @abstractmethod
        def shed_leaves(self) -> None:
            """
            Сбросить листья дерева.

            :return: None

            >>> oak = Tree('дуб', 50, 20.5)
            >>> oak.shed_leaves()  # Пример вызова метода
            """
            ...


    class SocialNetwork(ABC):
        def __init__(self, name: str, user_count: int):
            """
            Инициализация объекта класса SocialNetwork.

            :param name: Название социальной сети. Должен быть строкой.
            :param user_count: Количество пользователей. Должен быть неотрицательным целым числом.

            :raises ValueError: Если user_count отрицательное число.

            >>> facebook = SocialNetwork('Facebook', 2900000000)
            >>> facebook.name
            'Facebook'
            """
            if user_count < 0:
                raise ValueError("User count must be non-negative.")
            self.name = name
            self.user_count = user_count

        @abstractmethod
        def add_user(self) -> None:
            """
            Добавить нового пользователя в социальную сеть.

            :return: None

            >>> facebook = SocialNetwork('Facebook', 2900000000)
            >>> facebook.add_user()  # Пример вызова метода
            """
            ...

        @abstractmethod
        def remove_user(self) -> None:
            """
            Удалить пользователя из социальной сети.

            :return: None

            >>> facebook = SocialNetwork('Facebook', 2900000000)
            >>> facebook.remove_user()  # Пример вызова метода
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
