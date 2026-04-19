from register8 import Register8
from procgen_seed48 import Seed48
from procgen_name import ProcgenName
import copy



class PgPerson:
    """

    A person that generates its properties from the name provided.


    """

    # OMG just yolo the types... I didn't want to go all Rust for a simple test of this algo but really Python!?! WTF!!111eleven
    name = None
    seed = None

    pronoun_types = ["He/Him", "She/Her", "They/Them", "Ze/Hir", "Xe/Xem", "Ey/Em", "One/One", "We/Us"]
    pronouns = None

    comms_types = ["Voice (native)", "Voice (translated)", "Voice (translated)", "Voice (translated)", 
                   "Voice (translated)", "Voice (translated badly)", "Sign (translated)", "Colour Spectrum (translated)"]
    comms = None

    race = None


    def __init__(self, name: str):
        self.name = name
        self.generate()

    def generate(self):
        self.seed = Seed48().set_from_name(self.name)
        self.pronouns = self.pronoun_types[self.seed.w0_lo._val & 0b00000111]
        self.race = ProcgenName().single_from_seed(self.seed).name
        self.comms = self.comms_types[(self.seed.w0_lo._val >> 3) & 0b00000111]

        return self
        

    def __repr__(self) -> str:

        return (
            f"\t\t\tPerson: {self.name}\n"
            f"\t\t\t\tSeed:\t\t{self.seed}\n"
            f"\t\t\t\tPronouns:\t{self.pronouns}\n"
            f"\t\t\t\tRace:\t\t{self.race}\n"
            f"\t\t\t\tComms:\t\t{self.comms}\n"
        )



if __name__ == "__main__":
    person = PgPerson("Cmdr Jameson")
    print(person)
    person = PgPerson("Ford Prefect")
    print(person)
    person = PgPerson("Arthur Dent")
    print(person)
    person = PgPerson("Zaphod Beeblebrox")
    print(person)

