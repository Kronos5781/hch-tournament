from typing import List
from pydantic import BaseModel


class Game(BaseModel):
    start: str
    category: str
    playing_field: str
    team_1: str
    team_2: str


class Team(BaseModel):
    name: str
    category: str


class Category(BaseModel):
    name: str


class PlayingField(BaseModel):
    name: str


class Tournament(BaseModel):
    games: List[Game] | None = None
    teams: List[Team] | None = None
    categories: List[Category] | None = None
    playing_fields: List[PlayingField] | None = None
