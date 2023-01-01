from abc import ABC, abstractmethod


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Room(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_is_free(self):
        pass

    @abstractmethod
    def reserve(self, user: User):
        pass

    @abstractmethod
    def vacate(self):
        pass


class Audience(Room):
    def __init__(self, number=None, is_free: bool = True, reserved_by: User = None):
        self.number = number
        self.is_free = is_free
        self.reserved_by = reserved_by

    def get_is_free(self):
        return self.is_free

    def get_info(self):
        if self.is_free:
            return "audience number " + str(self.number) + " is free now."
        else:
            return "audience number " + str(self.number) + " is not free now."

    def reserve(self, user: User):
        self.is_free = False
        self.reserved_by = user

    def vacate(self):
        self.is_free = True


class Observer(ABC):
    @abstractmethod
    def attach(self, room: Room, user: User) -> None:
        pass

    @abstractmethod
    def detach(self, user: User) -> None:
        pass

    @abstractmethod
    def check_subs(self, room):
        pass

    @abstractmethod
    def notify(self, user: User, room: Room):
        pass


class ObserverAudience(Observer):
    def __init__(self) -> None:
        self.subscriptions = dict()
    
    def attach(self, audience: list, user: User) -> None:
        self.subscriptions[user] = audience

    def detach(self, user: User) -> None:
        self.subscriptions.pop(user)

    def notify(self, user: User, audience: Audience):
        print("Dear " + user.name + ", " + audience.get_info())
    
    def check_subs(self, audience_):
        for user, audiences in self.subscriptions.items():
            if audience_ in audiences:
                self.notify(user, audience_)


def vacate_audience(observer, audience):
    audience.vacate()
    observer.check_subs(audience)


def reserve_audience(observer, audience, user):
    audience.reserve(user)
    observer.check_subs(audience)


observer = ObserverAudience()
print("Oleg Ivanov makes subscription on audience number 1, 2, 3, 4.")

user1 = User("Oleg", "Ivanov")
user2 = User("Olia", "Ivanova")
user3 = User("Ivan", "Olegovish")

audience1 = Audience(1)
audience2 = Audience(2)
audience3 = Audience(3)
audience4 = Audience(4, False, user3)

observer.attach([audience1, audience2, audience3, audience4], user1)
print("Olia Ivanova reserves audience number 1, 2.")
print("-------------------------------------------------")
print("Notification to Oleg:")
reserve_audience(observer, audience1, user2)
reserve_audience(observer, audience2, user2)
print("-------------------------------------------------")
print("Ivan Olegovish vacates audience number 4.")
print("-------------------------------------------------")
print("Notification to Oleg:")
vacate_audience(observer, audience4)








