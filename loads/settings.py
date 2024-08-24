import json

# import values of settings
with open("settings.json", "r", encoding="utf-8") as settings:
    settings = json.load(settings)

    ShowEnemyShips = settings["Show Enemy Ships"]
    ShowYourShips = settings["Show Your Ships"]
    InfinityYourMoves = settings["Infinity Your Moves"]
    InfinityEnemyMoves = settings["Infinity Enemy Moves"]
    RandomShipGen = settings["Random Ship Generation"]
    PrintUserCompField = settings["Print User Comp Field"]
    PrintCompCompField = settings["Print Comp Comp Field"]
    Sounds = settings["Sounds"]
    IsMusic = settings["Music"]