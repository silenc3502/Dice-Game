
import sys
import os

from player.repository.player_repository_impl import PlayerRepositoryImpl

# 프로젝트 루트 경로 추가
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


playerRepository = PlayerRepositoryImpl.getInstance()
player = playerRepository.create()
print(f"player: {player}")
foundPlayer = playerRepository.findById(player.getId())
print(f"foundPlayer: {foundPlayer}")
playerList = playerRepository.findAll()
print(f"playerList: {playerList}")