"""
Guido's Gorgeous Lasagna exercise module.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(actual_time: int) -> int:
    """
    Function for calculating remaining bake time.
    :return: int - remaining bake time
    """
    return EXPECTED_BAKE_TIME - actual_time

def preparation_time_in_minutes(layers: int) -> int:
    """
    Function calculating how much time all layers are needed to make them.
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers: int, actual_time: int) -> int:
    """
    Function calculating preparation time in minutes.
    """
    return preparation_time_in_minutes(layers) + actual_time

print("Expected time:", EXPECTED_BAKE_TIME)
print("Remaining:", bake_time_remaining(30))
print("Layers:", preparation_time_in_minutes(2))
print("Elapsed cooking time:", elapsed_time_in_minutes(11, 15))