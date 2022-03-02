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
                    "Father", "HolySpirit", "Goblin", "Yahweh", "MasterOf", "Holy", "ArchNemesis", "Brute", "Superlative",
                    "Allah", "Fiend", "MetaGod", "Deity", "Monster", "Villain", "Demon", "Power", "Jah", "Bohdi",
                    "Succubus", "Gandhi", "Devil", "MalignantSpirit", "Idol", "Imp", "Incubus", "Hellion", "GodOfWar",
                  "WarLord", "KingKong"]
    drone_words = ["BarrelRoll", "YawSpin", "RubiksCube", "InvertedYawspin", "JuicyFlick", "Stall", "Throwback",
                   "VannyRoll", "KnifeEdge", "PowerLoop", "Orbit", "Split-S", "Immelmann", "Mattyflip", "TrippySpin",
                   "Dive", "WallRide", "BackwardDive", "WallBonk", "Quad", "Kwad", "Hexicopter", "Octocopter",
                   "Gimbal", "HeadlessMode", "BVLOS_", "LiPo", "Payload"]
    return drone_words[randrange(0, len(drone_words))] + race_names[randrange(0, len(race_names))] + 'FPV'


def main():
    name = fpv_life()
    master = Tk()
    w = Text(master, height=1, borderwidth=15, width=len(name))
    lab = Label(master)
    w.insert(1.0, name)
    w.pack()
    lab.pack()
    lab.config(text='FPV Race Handle')
    w.configure(state="disabled")
    mainloop()


if __name__ == '__main__':
    main()
