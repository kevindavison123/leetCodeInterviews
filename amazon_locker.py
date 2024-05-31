# You have a locker system and the lockers are small, medium and large,
# You have packages that need to go into the lockers, they are of size small, medium and large
# Packages can only be placed in lockers of the same size or larger
# Design a system that can execute this rule
from enum import Enum


# A Locker which will need to know: its size, small, med, large. It will also need to know if it is vacant or not
# A Package, which will only need to know its size,
# Locker Data structure: Houses a collection of lockers and knows which locker to put the package in


class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


class Locker:
    count = 0

    def __init__(self, size: Size):
        Locker.count += 1
        self.id = Locker.count
        self.size = size
        self.vacant = True

    def get_id(self): return self.id

    def get_size(self): return self.size.value

    def is_vacant(self): return self.vacant

    def set_vacant(self, vacant): self.vacant = vacant


class Package:
    def __init__(self, size: Size):
        self.size = size

    def get_size(self): return self.size.value


class LockerManager:
    def __init__(self, lockers):
        self.lockers = lockers
        self.locker_map = {}

    def get_next_locker(self, package):
        for locker in self.lockers:
            if locker.get_size() >= package.get_size() and locker.is_vacant():
                locker.set_vacant(False)
                self.locker_map[locker.get_id()] = package
                return locker

    def empty_locker(self, locker_id):
        if locker_id in self.locker_map:
            package = self.locker_map[locker_id]
        for locker in self.lockers:
            if locker.get_id() == locker_id:
                locker.set_vacant(True)
        return package

    def print_locker_status(self):
        print("-------------")
        for locker in self.lockers:
            print(f"{locker.id}: size: {locker.get_size()}, vacant: {locker.is_vacant()}")


if __name__ == "__main__":
    locker_manager = LockerManager([Locker(Size.LARGE), Locker(Size.MEDIUM), Locker(Size.SMALL)])
    locker_manager.print_locker_status()
    locker_manager.get_next_locker(Package(Size.LARGE))
    locker_manager.get_next_locker(Package(Size.LARGE))
    locker_manager.get_next_locker(Package(Size.LARGE))
    locker_manager.get_next_locker(Package(Size.SMALL))
    locker_manager.print_locker_status()
    locker_manager.empty_locker(1)
    locker_manager.print_locker_status()
