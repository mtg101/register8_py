from procgen_person import PgPerson
from procgen_seed48 import Seed48
from procgen_ship import PgShip
from procgen_name import ProcgenName


class PlayerCaptain:
    """

    A person with a ship.


    """

    name = None
    seed = None

    captain = None
    ship = None


    def __init__(self, name: str):
        self.name = name
        self.generate()

    def generate(self):
        self.seed = Seed48().set_from_name(self.name)
        self.captain = PgPerson(self.name)
        self.ship = PgShip(ProcgenName().multi_from_seed(self.seed).name)

        return self
        

    def __repr__(self) -> str:
        return (
            f"\t\t\tPlayer Captain: {self.name}\n"
            f"\t\t\t\tSeed:\t\t{self.seed}\n"
            f"\t\t\t\tCaptain:\t\t{self.captain}\n"
            f"\t\t\t\tShip:\n{self.ship}\n"
        )



if __name__ == "__main__":
    pc = PlayerCaptain("Yui")
    print(pc)
    pc = PlayerCaptain("Mio")
    print(pc)
    pc = PlayerCaptain("Ritsu")
    print(pc)
    pc = PlayerCaptain("Mugi")
    print(pc)

