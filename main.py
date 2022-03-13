from random import randrange
from tkinter import *


def fpv_life():
    """
    Randomly generates your Spiritual FPV Handle.
    This is probably the most useful thing on the internet and its here, free.
    You're welcome.
    """
    adjective = ["BarrelRolling", "YawSpinning", "RubiksCubing", "InvertedYawSpinning", "JuicyFlicking", "Stalling",
                 "ThrowBacking", "VannyRolling", "KnifeEdging", "PowerLooping", "Orbiting", "Split-S'n", "SIM-Racing",
                 "Immelmanning", "MattyFlipping", "TrippySpinning", "OfficeDiving", "BackwardDiving", "StockFlying"
                 "WallBonking", "GimbalMashing", "HeadlessModing", "LiPoSucking", "PayloadDropping", "Inverted",
                 "AcroRipping", "Brushless", "Freestyling", "Chicaning", "GapDiving", "PylonHugging", "CorkScrewing",
                 "BandoFenceJumping", "DriftChasing", "WallRiding", "FlagShredding", "KissDevoted", "ButterFlying",
                 "OldSchool", "BetaFlightLoving", "WhoopKing", "StockFlying", "BridgeDiving", "Toothpicked", "Jello",
                 "GateSmashing", "TowerSmashing", "LadderLooping", "RipSeshing", "SlalomSmashing", "ThrottleTrimming",
                 "MotorSmoking", "ESC-Burning", "LiPoKilling", "PowerHungry", "TrainChasing", "Overpowered"]
    noun = ["DroneTemplePilot", "SlipStreamer", "Ghost", "Thor", "SpaceCaptain", "Lord", "Mong", "Jedi", "StarLord"
            "King", "AlmightyDroneGod", "God", "BardwellKnowItAll", "SpacePilot", "StingyFanboy", "NurkFanboy"
            "SkyLord", "DemiGod", "Shyamalan", "SacrificialGoat", "Beast", "Jeebus", "ELRS-Fanboy", "PID-Master"
            "Daddy", "MamasBoy", "Goblin", "PantyDropper", "Master", "Gimp", "ArchNemesis", "Brute", "Satan",
            "Fiend", "MetaGod", "Deity", "Monster", "Villain", "Demon", "Bohdi", "LineMaster", "GeoFenceHacker"
            "Succubus", "Gandhi", "Devil", "MalignantSkyGod", "Idol", "Imp", "GodOfWar", "DJI-Fanboy", "DigitalSnob",
            "WarLord", "KingKong", "MoFo", "BossMan", "Captain", "Maniac", "SimulatorGod", "Spotter", "TBS-Fanboy"
            "Warrior", "Noob", "SpaceCadet", "PocketRocket", "HellBoi", "DRL-Champion", "SimHero", "Samurai",
            "AutoPilot", "PropBurner", "ESC-Burner"]

    # Remove the duplicates - coz im lazy.
    adjective = list(set(adjective))
    noun = list(set(noun))

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
