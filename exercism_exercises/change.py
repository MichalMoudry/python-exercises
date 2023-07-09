"""
Change exercise module.
"""

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Test function comment
    """
    result: list[int] = []
    for coin in reversed(coins):
        print(coin)
    return result

print(find_fewest_coins([1, 5, 10, 25, 100], 15))
