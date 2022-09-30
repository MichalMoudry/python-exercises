"""
Black jack execise module.
"""

from calendar import c


FACE_CARDS = ["J", "Q", "K"]

def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in FACE_CARDS:
        return 10
    elif card == "A":
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    val1, val2 = value_of_card(card_one), value_of_card(card_two)
    if val1 == val2:
        return (card_one, card_two)
    elif val1 > val2:
        return card_one
    return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    val1, val2 = value_of_card(card_one), value_of_card(card_two)
    summ = val1 + val2 + 11
    if val1 == 1 or val2 == 1: summ += 11
    if summ > 21:
        return 1
    else:
        return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    collection = FACE_CARDS.copy()
    collection.append("10")
    is_in_collection = card_one in collection or card_two in collection
    return (card_one == "A" or card_two == "A") and is_in_collection


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    higher = higher_card(card_one, card_two)
    return type(higher) is tuple


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    val1, val2 = value_of_card(card_one), value_of_card(card_two)
    return val1 + val2 in (9, 10, 11)
