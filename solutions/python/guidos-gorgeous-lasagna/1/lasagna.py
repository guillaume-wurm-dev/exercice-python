EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    Parameters:
        number_of_layers (int): number of lasagna layers

    Returns:
        int: total preparation time, assuming 2 minutes per layer.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time in minutes.

    Parameters:
        number_of_layers (int): The number of lasagna layers.
        elapsed_bake_time (int): The number of minutes the lasagna has already baked.

    Returns:
        int: The total elapsed time, including preparation and baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time