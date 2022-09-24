"""
Yacht exercise module.
"""
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice: list, category: str) -> int:
    match category:
        case "ONES": return dice.count(1)
        case "TWOS": return dice.count(2) * 2
        case "THREES": return dice.count(3) * 3
        case "FOURS": return dice.count(4) * 4
        case "FIVES": return dice.count(5) * 5
        case "SIXES": return dice.count(6) * 6
        case "FOUR_OF_A_KIND":
            sorted_dice = sorted(dice)
            first_element_count = dice.count(sorted_dice[0])
            last_element_count = dice.count(sorted_dice[-1])
            if first_element_count >= 4: return sum(sorted_dice[:-1])
            elif last_element_count >= 4: return sum(sorted_dice[1:])
            else: return 0
        case "FULL_HOUSE":
            count = 0
            for value in dice:
                count = dice.count(value)
                if count > 3 or count < 2:
                    return 0
            return sum(dice)
        case "LITTLE_STRAIGHT": return 30 if sorted(dice) == [1,2,3,4,5] else 0
        case "BIG_STRAIGHT": return 30 if sorted(dice) == [2,3,4,5,6] else 0
        case "YACHT": return 50 if dice.count(dice[0]) == len(dice) else 0
        case "CHOICE": return sum(dice)
        case _: return 0