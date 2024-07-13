from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        nick = self.nickname
        return (f"Dwarf warrior {nick}. {nick} has a "
                f"hummer of the {self._hummer_level} level")