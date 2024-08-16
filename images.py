from pygame.image import load
from pygame import transform

OneDeckShipImg = load("images/OneDeckShip.png")
ShipStartImg = load("images/ShipStart.png")
TransformShipStartImg = transform.rotate(ShipStartImg, 90.0)
ShipContinueImg = load("images/ShipContinue.png")
TransformShipContinueImg = transform.rotate(ShipContinueImg, 90.0)
ShipEndImg = load("images/ShipEnd.png")
TransformShipEndImg = transform.rotate(ShipEndImg, 90.0)
FieldImg = load("images/Field.png")
HitImg = load("images/Hit.png")
SkipImg = load("images/Skip.png")
ClearImg = load("images/Clear.png")
RestartImg = load("images/Restart.png")
YouWinImg = load("images/YouWin.png")
YouLoseImg = load("images/YouLose.png")
GameStart = load("images/GameStart.png")