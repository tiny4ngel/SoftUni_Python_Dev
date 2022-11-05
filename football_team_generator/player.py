class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting
        
    @property
    def name(self):
        return self.__name

    def __str__(self):
        result = []

        result.append(f"Player: {self.__name}")
        result.append(f"Sprint: {self.__sprint}")
        result.append(f"Dribble: {self.__dribble}")
        result.append(f"Passing: {self.__passing}")
        result.append(f"Shooting: {self.__shooting}")

        return '\n'.join(str(r) for r in result)

