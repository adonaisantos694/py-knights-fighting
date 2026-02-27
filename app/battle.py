from typing import Dict, Any
from .knight import Knight


def fight(knight_1: Knight, knight_2: Knight) -> None:
    damage_to_1 = knight_2.power - knight_1.protection
    damage_to_2 = knight_1.power - knight_2.protection

    knight_1.take_damage(damage_to_1)
    knight_2.take_damage(damage_to_2)


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
