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

    # sounds settings
    Sounds = settings["Sounds"] # dict
    IsSounds = Sounds["Is Sounds"] # bool

    if IsSounds:
        Language = Sounds["Language"] # ru/en
        
        try:
            if Language.lower() not in ("ru", "en"):
                Language = "en"
        except AttributeError:
            Language = "en"

        Voice = Sounds["Voice"] #dict
        IsClasic = Voice["Is Classic"] # bool
        if not IsClasic:
            IsSwears = Voice["Is Swears"] #bool

    IsMusic = settings["Music"]
