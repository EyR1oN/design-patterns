from abc import ABC, abstractmethod


class TestPaper(ABC):
    @abstractmethod
    def count_maks_mark(self) -> float:
        pass


class StandardTest(TestPaper):
    def __init__(self, theme, author, tasks: list, maks_mark: int = 0) -> None:
        self.theme = theme
        self.author = author
        self.tasks = tasks
        self.maks_mark = maks_mark

    def count_maks_mark(self) -> float:
        self.maks_mark = len(self.tasks)
        return self.maks_mark


class SimplifiedTest(TestPaper):
    def __init__(self, theme, author, tasks: list, maks_mark: int = 0) -> None:
        self.theme = theme
        self.author = author
        self.tasks = tasks
        self.maks_mark = maks_mark

    def count_maks_mark(self) -> float:
        self.maks_mark = len(self.tasks)*3
        return self.maks_mark


class SpecialTest(TestPaper):
    def __init__(self, theme, author, tasks: list, maks_mark: int = 0) -> None:
        self.theme = theme
        self.author = author
        self.tasks = tasks
        self.maks_mark = maks_mark

    def count_maks_mark(self) -> float:
        self.maks_mark = (len(self.tasks)+2) * 3 / (len(self.tasks)/2)
        return self.maks_mark


class TestFactory():

    def create_test_paper(self, tasks, type: str) -> object:
        if type == 'standard':
            theme = "Linear Programming"
            author = "Oleg Ivanov"
            return StandardTest(theme, author, tasks)
        elif type == 'special':
            theme = "Linear Programming for Engineers"
            author = "Ivan Olegov"
            return SpecialTest(theme, author, tasks)
        else:
            theme = "Linear Programming for Beginners"
            author = "Olga Ivanova"
            return SimplifiedTest(theme, author, tasks)


test_factory = TestFactory()
test_type = "standard"
test = test_factory.create_test_paper(["How are you?", "What is your name?"], test_type)
print("--------------------------------------------------------------------------")
print("The max mark for this test can be: " + str(test.count_maks_mark()) + ".")

test_type1 = "special"
test1 = test_factory.create_test_paper(["How are you?", "What is your name?"], test_type1)
print("--------------------------------------------------------------------------")
print("The max mark for this test can be: " + str(test1.count_maks_mark()) + ".")

test_type2 = "simplified"
test2 = test_factory.create_test_paper(["How are you?", "What is your name?"], test_type2)
print("--------------------------------------------------------------------------")
print("The max mark for this test can be: " + str(test2.count_maks_mark()) + ".")
