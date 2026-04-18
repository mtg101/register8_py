from register8 import Register8
import random



class ProcgenName:
    """
    Uses the Elite-style the_one_string with pairs of letters
    that can be used to form syllables in words / name for the procgen world.

    I'm going to borrow the romanization of Hiragana from Japanese to give me Japanese-sounding names.
    And I'm going to bastardize it so I have enough for 128 pairs (max 8bit index 254 for last pair)

    Single chars: like Elite, just ignore space when printing ("A TADA" is "TADA", "BAN KIRU" becomes "BANKIRU")

    Spaces aren't needed because if you want multiple names, you ask for them. 

    """
    # the one magic string!
    # pairs of letters that we'll use to generate all the names for the game
    # Japanese-sounding by basing it on romanticized Hiragana
    # 'Pascal' case so I can see what's going on, C64 will be all caps / single char font
    the_one_string = (
        "A I U E O N "
        "KaKiKuKeKoKy"
        "SaSiSuSeSoSy"
        "TaSiTuTeToTy"
        "NaNiNuNeNoNy"
        "HaHiHuHeHoHy"
        "MaMiMuMeMoMy"
        "YaYiYuYeYoY "
        "RaRiRuReRoRy"
        "WaWiWuWeWoWy"
        "GaGiGuGeGoGy"
        "ZaZiZuZeZoZY"
        "DaDiDuDeDoDY"
        "BaBiBuBeBoBy"
        "PaPiPuPePoPy"
        "JaJiJuJeJoJy"

        "KaKiKuKeKoKy"
        "SaSiSuSeSoSy"
        "TaSiTuTeToTy"
        "NaNiNuNeNoNy"
        "HaHiHuHeHoHy"
        "' - "
    )

    # 128 pairs for 256 len is what we want here
    @classmethod
    def len(cls):
        return len(cls.the_one_string)
    
    # creates name of len pairs from RNG
    def rng_len(self, len: int):
        self.name = ""
        for i in range(len):
            pair_index = random.randint(0, 127) * 2
            self.name = self.name + self.the_one_string[pair_index : pair_index + 2]
            self.name = self.name.replace(" ", "")

        return self
    
    # name
    name = "not set"

    # LFSR register
    lfsr = Register8(0x17)

    def __repr__(self) -> str:
        return (
            "Name:\n"
            f"\t{self.name}\n"
            f"\t{self.lfsr}"
        )

    def c64_style_lfsr_right(self):
        # shift right
        self.lfsr.shr()

        # if carry, XOR with magic $1D
        if self.lfsr.carry:
            self.lfsr.XOR(0xB8)

        return self

    def c64_style_lfsr_left(self):
        # shift right
        self.lfsr.shl()

        # if carry, XOR with magic $1D
        if self.lfsr.carry:
            self.lfsr.XOR(0x1D)

        return self
    





# def elite_tidy(w0, w1, w2):
#     """
#     Mimics the Elite 'next_lsr' routine. 
#     Each step generates a new 48-bit state (3 x 16-bit words).
#     """
#     # 1. Add w0 and w1 to get a new w0
#     # On a 6502, this is a 16-bit addition with carry
#     tmp = (w0 + w1) & 0xFFFF
#     new_w0 = tmp
    
#     # 2. Add the original w1 and w2 to get a new w1
#     new_w1 = (w1 + w2) & 0xFFFF
    
#     # 3. Add the NEW w0 and NEW w1 to get a new w2
#     new_w2 = (new_w0 + new_w1) & 0xFFFF
    
#     return new_w0, new_w1, new_w2


# # The actual syllable table used in the 1984 original
# SYLLABLES = (
#     "..LEXEGEZACEBISO"
#     "USESARADIRETERI"
#     "BERIETENPHQUGE"
#     "LEDIORLALAREVE"
#     "BESHINORQUENTA"
#     "GUSTARBITA"
# )

# def generate_name(w0, w1, w2):
#     name = ""
#     # Usually 3 or 4 syllables
#     # Elite uses a specific bit in the seed to decide length
#     length = 3 if (w0 & 0x40) else 4
    
#     # We work on a copy of the seeds so we don't 'ruin' the system coordinates
#     tw0, tw1, tw2 = w0, w1, w2
    
#     for _ in range(length):
#         # Extract 6 bits from the middle of the seed (The Window)
#         index = (tw1 >> 8) & 0x3F
        
#         # Get the pair of characters from the table
#         char1 = SYLLABLES[index * 2]
#         char2 = SYLLABLES[index * 2 + 1]
        
#         if char1 != ".": name += char1
#         if char2 != ".": name += char2
        
#         # Scramble the seeds for the NEXT syllable in the same name
#         tw0, tw1, tw2 = elite_tidy(tw0, tw1, tw2)
        
#     return name.capitalize()

# # The 'Lave' Seed (Initial state of Galaxy 1)
# w0, w1, w2 = 0x5A4A, 0x0248, 0xB753

# for i in range(5):
#     # 1. Get the name of the current system
#     system_name = generate_name(w0, w1, w2)
    
#     # 2. Coordinates are pulled from the high bytes of the seeds
#     x_coord = w1 >> 8
#     y_coord = w0 >> 8
    
#     print(f"System: {system_name:8} | Coordinates: ({x_coord}, {y_coord})")
    
#     # 3. 'Jump' to the next system in the galaxy
#     w0, w1, w2 = elite_tidy(w0, w1, w2)






if __name__ == "__main__":
    name = ProcgenName().rng_len(3)
    print(name)
    print("right shift:")
    # Example usage
    for _ in range(8):
        print(name.lfsr)
        state = name.c64_style_lfsr_right()

    print("\nright left:\n")
    # Example usage
    for _ in range(8):
        print(name.lfsr)
        state = name.c64_style_lfsr_left()



