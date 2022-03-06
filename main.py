from random import randrange
from tkinter import *


def fpv_life():
    """
    Randomly generates your Spiritual FPV Handle.
    This is probably the most useful thing on the internet and its here, free.
    You're welcome.
    """
    race_names = ["Spirit", "Enlightened", "InfiniteSpirit", "Ghost", "Disembodied", "Omnipotent", "Lord",
                  "KingOfKings", "Almighty", "God", "Soulbringer", "Inshallah", "Incorporeal", "Divinity", "Vampire",
                  "Maker", "DemiGod", "Shyamalan", "DivineBeing", "Sacred", "Creator", "Beast", "Jeebus", "Satan",
                  "Father", "HolySpirit", "Goblin", "Yahweh", "MasterOf", "Holy", "ArchNemesis", "Brute",
                  "Allah", "Fiend", "MetaGod", "Deity", "Monster", "Villain", "Demon", "Power", "Jah", "Bohdi",
                  "Succubus", "Gandhi", "Devil", "MalignantSpirit", "Idol", "Imp", "Incubus", "Hellion", "GodOfWar",
                  "WarLord", "KingKong", "MoFo", "BossMan", "Captain", "Superlative"]
    drone_words = ["BarrelRolling", "YawSpinning", "RubiksCubed", "InvertedYawSpinning", "JuicyFlicking", "Stalling",
                   "ThrowBacking", "VannyRolling", "KnifeEdging", "PowerLooping", "Orbiting", "Split-S'n",
                   "Immelmanning", "MattyFliping", "TrippySpinning", "StructureDiving", "WallRiding", "BackwardDiving",
                   "WallBonking", "GimbalMashing", "HeadlessModer", "LiPoSucking", "PayloadDropping", "Inverted"]

    return drone_words[randrange(0, len(drone_words))] + race_names[randrange(0, len(race_names))] + 'FPV'


def main():
    name = fpv_life()
    master = Tk()
    w = Text(master, height=1, borderwidth=15, width=len(name))
    lab = Label(master)
    w.insert(1.0, name)
    w.pack()
    lab.pack()
    lab.config(text='FPV Pro-Race Handle')
    w.configure(state="disabled")
    mainloop()


if __name__ == '__main__':
    main()
