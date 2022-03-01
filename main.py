from random import randrange
from tkinter import *


def fpv_life():
    """
    Randomly generates your Spiritual FPV Handle.
    This is probably the most useful thing on the internet and its here, free.
    You're welcome.
    """
    spirit_names = ("Yoga", "Soulbringer", "DemiGod", "God", "Deity", "Enlightened", "Bohdi", "Gandhi", "Divine", "Metaphysical", "Sacred", "Holy", "Disembodied", "Ethereal", "Ghost", "Incorporeal", "Rainbow", "Pure", "Rarefied", "Superlative", "Jesus", "Allah", "Inshallah", "Om", "Shyamalan", "Incense")
    drone_names = ("BarrelRoll", "YawSpin", "RubiksCube", "InvertedYawspin", "JuicyFlick", "Stall", "Throwback", "VannyRoll", "KnifeEdge", "PowerLoop", "Orbit", "Split-S", "Immelmann", "Mattyflip", "TrippySpin", "Dives", "WallRide", "BackwardDive", "WallBonk", "UAV", "Quad", "Kwad", "Hexicopter", "Octocopter", "RTF", "BNF", "Gimbal", "HeadlessMode", "Autonomous", "BVLOS", "LiPo", "Part107", "Payload")
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
