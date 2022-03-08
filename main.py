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
                 "AcroRipping", "Brushless", "Freestyling", "Chicaning", "GapDiving", "PylonHugging", "CorkScrewing",
                 "BandoFenceJumping", "DriftChasing", "WallRiding", "FlagShredding", "KissDevoted", "ButterFlying",
                 "OldSchool", "BetaFlightLoving", "WhoopKing", "StockFlying", "BridgeDiving", "Toothpicked", "Jello",
                 "GateSmashing", "TowerSmashing", "LadderLooping", "RipSeshing", "SlalomSmashing", "ThrottleTrimming",
                 "MotorSmoking", "ESC_Burning", "LiPoKilling", "PowerHungry"]
    noun = ["DroneTemplePilot", "SlipStreamer", "Ghost", "Thor", "SpaceCaptain", "Lord", "Mong", "Jedi",
            "King", "TheAlmighty", "God", "BardwellKnowItAll", "SpacePilot",
            "SkyLord", "DemiGod", "Shyamalan", "SacrificialGoat", "Beast", "Jeebus",
            "Daddy", "MamasBoy", "Goblin", "PantyDropper", "Master", "Gimp", "ArchNemesis", "Brute", "Satan",
            "Fiend", "MetaGod", "Deity", "Monster", "Villain", "Demon", "Bohdi",
            "Succubus", "Gandhi", "Devil", "MalignantSkyGod", "Idol", "Imp", "GodOfWar",
            "WarLord", "KingKong", "MoFo", "BossMan", "Captain", "Maniac", "SimulatorGod",
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
