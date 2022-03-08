from random import randrange
from tkinter import *


def fpv_life():
    """
    Randomly generates your Spiritual FPV Handle.
    This is probably the most useful thing on the internet and its here, free.
    You're welcome.
    """
    adjective = ["BarrelRolling", "YawSpinning", "RubiksCubed", "InvertedYawSpinning", "JuicyFlicking", "Stalling",
                 "ThrowBacking", "VannyRolling", "KnifeEdging", "PowerLooping", "Orbiting", "Split-S'n",
                 "Immelmanning", "MattyFlipping", "TrippySpinning", "OfficeWindowDiving", "BackwardDiving",
                 "WallBonking", "GimbalMashing", "HeadlessModing", "LiPoSucking", "PayloadDropping", "Inverted",
                 "AcroRipping", "Brushless", "Freestyle", "Chicaning", "GapDiving", "PylonHugging", "CorkScrewing",
                 "BandoFenceJumping", "DriftChasing", "WallRiding", "FlagShredding", "KissDevoted", "ButterFlight",
                 "OldSchool", "BetaFlightLoving", "WhoopKing", "StockFlyer", "BridgeDiver", "Toothpick", "Jello",
                 "GateSmashing", "TowerSmashing", "LadderLooping", "RipSeshing", "SexySlalom", "ThrottleTrimming",
                 "MotorSmoking", "ESC_Burning", "LiPoKilling"]
    noun = ["DroneTemplePilot", "SlipStreamer", "Ghost", "Thor", "SpaceCaptain", "Lord", "Mong", "Jedi",
            "King", "Almighty", "God", "SoulMan", "Inshallah", "BardwellKnowItAll", "SpacePilot", "Vampire",
            "SkyLord", "DemiGod", "Shyamalan", "DivineBeing", "SacrificialGoat", "Creator", "Beast", "Jeebus",
            "Daddy", "MamasBoy", "Goblin", "PantyDropper", "Master", "Gimp", "ArchNemesis", "Brute", "Satan",
            "Allah", "Fiend", "MetaGod", "Deity", "Monster", "Villain", "Demon", "Power", "Jah", "Bohdi",
            "Succubus", "Gandhi", "Devil", "MalignantSkyGod", "Idol", "Imp", "Incubus", "Hellion", "GodOfWar",
            "WarLord", "KingKong", "MoFo", "BossMan", "Captain", "Superlative", "Maniac", "SimulatorGod",
            "Warrior", "Noob", "SpaceCadet", "PocketRocket", "HellBoi", "DRL_Champion", "SimHero", "Samurai",
            "AutoPilot", "PropBurner", "StarLord", "Spotter", "TBS_Fanboy", "DJI_Fanboy", "DigitalSnob",
            "GeoFenceHacker", "ELRS_Fanboy"]

    return adjective[randrange(0, len(adjective))] + noun[randrange(0, len(noun))] + 'FPV'


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
