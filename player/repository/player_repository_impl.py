import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository
from utility.input_generator import InputGenerator


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __playerList = []

    MIN = 0
    MAX = 2

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self):
        userInputPlayerName = InputGenerator.createPlayerUserInput()
        player = Player(userInputPlayerName)

        self.__playerList.append(player)

        return player

    def findAll(self):
        return self.__playerList

    def findById(self, id):
        for player in self.__playerList:
            if player.getId() == id:
                return player

        return None
    