from pygame.image import load
from pygame import transform

OneDeckShipImg = load("image/images/OneDeckShip.png")

ShipStartImg = load("image/images/ShipStart.png")
TransformShipStartImg = transform.rotate(ShipStartImg, 90.0)

ShipContinueImg = load("image/images/ShipContinue.png")
TransformShipContinueImg = transform.rotate(ShipContinueImg, 90.0)

ShipEndImg = load("image/images/ShipEnd.png")
TransformShipEndImg = transform.rotate(ShipEndImg, 90.0)

FieldImg = load("image/images/Field.png")
HitImg = load("image/images/Hit.png")
SkipImg = load("image/images/Skip.png")
RestartImg = load("image/images/Restart.png")
YouWinImg = load("image/images/YouWin.png")
YouLoseImg = load("image/images/YouLose.png")
GameStart = load("image/images/GameStart.png")