from random import randrange
from tkinter import *


def fpv_life():
    """
    Randomly generates your Spiritual FPV Handle.
    This is probably the most useful thing on the internet and its here, free.
    You're welcome.
    """
    spirit_names = ["Spirit", "Enlightened", "InfiniteSpirit", "Ghost", "Disembodied", "Omnipotent", "Lord",
                    "KingOfKings", "Almighty", "God", "Soulbringer", "Inshallah", "Incorporeal", "Divinity", "Vampire",
                    "Maker", "DemiGod", "Shyamalan", "DivineBeing", "Sacred", "Creator", "Beast", "Jeebus", "Satan",
                    "Father", "HolySpirit", "Goblin", "Yahweh", "MasterOf", "Holy", "Archfiend", "Brute", "Superlative",
                    "Allah", "Fiend", "MetaGod", "Deity", "Monster", "Villain", "Demon", "Power", "Jah", "Bohdi",
                    "Succubus", "Gandhi", "Devil", "MalignantSpirit", "Idol", "Imp", "Incubus", "Hellion"]
    drone_names = ["BarrelRoll", "YawSpin", "RubiksCube", "InvertedYawspin", "JuicyFlick", "Stall", "Throwback",
                   "VannyRoll", "KnifeEdge", "PowerLoop", "Orbit", "Split-S", "Immelmann", "Mattyflip", "TrippySpin",
                   "Dive", "WallRide", "BackwardDive", "WallBonk", "Quad", "Kwad", "Hexicopter", "Octocopter",
                   "Gimbal", "HeadlessMode", "BVLOS_", "LiPo", "Payload"]
    return drone_names[randrange(0, len(drone_names))] + spirit_names[randrange(0, len(spirit_names))] + 'FPV'


def main():
    name = fpv_life()
    master = Tk()
    w = Text(master, height=1, borderwidth=15, width=len(name))
    w.insert(1.0, name)
    w.pack()
    w.configure(state="disabled")
    mainloop()


if __name__ == '__main__':
    main()
