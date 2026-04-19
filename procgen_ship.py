from register8 import Register8
from procgen_seed48 import Seed48
from procgen_name import ProcgenName
from procgen_logo import PgLogo
import copy



class PgShip:
    """

    A ship that generates its properties from the name provided.


    """

    name = None
    seed = None

    shape_options = ["Circle", "Square", "Triangle", "Hexagon", "Pentagon", "Star", "Hash", "Slash"]
    shape = None

    colour_options = ["WHite", "Red", "Cyan", "Purple", "Green", "Blue", "Yellow", "White"]
    colour = None

    cargo = None
    cabins = None

    def __init__(self, name: str):
        self.name = name
        self.generate()

    def generate(self):
        self.seed = Seed48().set_from_name(self.name)
        self.shape = self.shape_options[self.seed.w0_lo._val & 0b00000111]
        self.colour = self.colour_options[(self.seed.w0_lo._val >> 3) & 0b00000111]
        self.cargo = self.seed.w0_hi._val
        self.cabins = self.seed.w1_lo._val & 0b00000111

        return self
        

    def __repr__(self) -> str:

        return (
            f"\t\t\tShip: {self.name}\n"
            f"\t\t\t\tSeed:\t\t{self.seed}\n"
            f"\t\t\t\tShape:\t\t{self.shape}\n"
            f"\t\t\t\tColour:\t\t{self.colour}\n"
            f"\t\t\t\tCargo:\t\t{self.cargo}m3\n"
            f"\t\t\t\tCabins:\t\t{self.cabins}\n"
        )



if __name__ == "__main__":
    ship = PgShip("GCU Problem Child")
    print(ship)
    ship = PgShip("DC Carl")
    print(ship)
    ship = PgShip("GCU Opp I Did It Again")
    print(ship)
    ship = PgShip("NCC-1701A")
    print(ship)

