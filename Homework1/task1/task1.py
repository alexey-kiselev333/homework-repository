def check_power_of_2(a: int) -> bool:
    """

    The function checks if the number is a degree of two
    Args:
        a:
    Returns:True or False

    Example:
        if a==128 then return True
        if a==0 then return False

    """
    return not (bool(a & (a - 1))) and a != 0
