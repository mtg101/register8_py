from register8 import Register8
from procgen_seed48 import Seed48
from procgen_name import ProcgenName
import copy



class PgLogo:
    """

    A logo from a ProcgenName


    """

    seed = None

    bg_colour_options = ["Black", "Blue", "Purple", "Red"]
    fg_colour_options = ["White", "Cyan", "Green", "Yellow"]

    tl_initial_fg_colour = None
    tl_initial_bg_colour = None
    initial = None

    tr_fg_colour = None
    tr_bg_colour = None

    bl_fg_colour = None
    bl_bg_colour = None

    br_fg_colour = None
    br_bg_colour = None

    symbol_options = ["", "", "", "", "", "", "", "", 
                      "*", "-", "!", "+", "# ", "/ ", "?", "~"]
    tr_symbol = None
    bl_symbol = None
    br_symbol = None


    def __init__(self, name: str):
        self.name = name
        self.generate()

    def generate(self):
        self.seed = Seed48().set_from_name(self.name)
        self.tl_initial_fg_colour = self.fg_colour_options[self.seed.w0_lo._val & 0b00000011]
        self.tl_initial_bg_colour = self.bg_colour_options[(self.seed.w0_lo._val >> 2) & 0b00000011]
        self.initial = self.name[0]

        self.tr_fg_colour = self.fg_colour_options[(self.seed.w0_lo._val >> 4) & 0b00000011]
        self.tr_bg_colour = self.bg_colour_options[(self.seed.w0_lo._val >> 6) & 0b00000011]
        self.bl_fg_colour = self.fg_colour_options[(self.seed.w0_hi._val >> 0) & 0b00000011]
        self.bl_bg_colour = self.bg_colour_options[(self.seed.w0_hi._val >> 2) & 0b00000011]
        self.br_fg_colour = self.fg_colour_options[(self.seed.w0_hi._val >> 4) & 0b00000011]
        self.br_bg_colour = self.bg_colour_options[(self.seed.w0_hi._val >> 6) & 0b00000011]

        self.tr_symbol = self.symbol_options[(self.seed.w1_lo._val >> 0) & 0b00001111]
        self.bl_symbol = self.symbol_options[(self.seed.w1_lo._val >> 4) & 0b00001111]
        self.br_symbol = self.symbol_options[(self.seed.w1_hi._val >> 0) & 0b00001111]

        return self
        

    def __repr__(self) -> str:

        return (
            f"\t\t\t\t\tSeed:\t\t{self.seed}\n"
            f"\t\t\t\t\tTL Initial: {self.initial}\tFG Colour: {self.tl_initial_fg_colour}\tBG Colour: {self.tl_initial_bg_colour}\n"
            f"\t\t\t\t\tTR Symbol: {self.tr_symbol}\tFG Colour: {self.tr_fg_colour}\tBG Colour: {self.tr_bg_colour}\n"
            f"\t\t\t\t\tBL Symbol: {self.bl_symbol}\tFG Colour: {self.bl_fg_colour}\tBG Colour: {self.bl_bg_colour}\n"
            f"\t\t\t\t\tBR Symbol: {self.br_symbol}\tFG Colour: {self.br_fg_colour}\tBG Colour: {self.br_bg_colour}\n"
        )



if __name__ == "__main__":
    logo = PgLogo("Cmdr Jameson")
    print(logo)
    logo = PgLogo("Max Power")
    print(logo)
    logo = PgLogo("Pikachu")
    print(logo)
    logo = PgLogo("Commander Shepard")
    print(logo)

