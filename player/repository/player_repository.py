from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass
