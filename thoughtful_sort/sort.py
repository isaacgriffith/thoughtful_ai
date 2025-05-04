def sort(width, height, length, mass):
    """Sorts a package based on its dimensions and mass into different categories.

    The function categorizes packages into three categories:
    - STANDARD: Neither bulky nor heavy
    - SPECIAL: Either bulky or heavy
    - REJECTED: Both bulky and heavy

    A package is considered:
    - Bulky if its volume (width * height * length) exceeds 1,000,000
    - Bulky if any dimension (width, height, or length) exceeds 150
    - Heavy if its mass exceeds 20

    Args:
        width (float): Width of the package in arbitrary units
        height (float): Height of the package in arbitrary units
        length (float): Length of the package in arbitrary units
        mass (float): Mass of the package in arbitrary units

    Returns:
        str: The category of the package - "STANDARD", "SPECIAL", or "REJECTED"

    Raises:
        ValueError: If any of the dimensions or mass is negative

    Examples:
        >>> sort(10, 10, 10, 10)
        'STANDARD'
        >>> sort(100, 100, 100, 10)
        'SPECIAL'
        >>> sort(10, 10, 10, 21)
        'SPECIAL'
        >>> sort(100, 100, 100, 21)
        'REJECTED'
    """
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("All dimensions must be positive")
    
    is_bulky = (width * height * length >= 1000000 or 
                width >= 150 or height >= 150 or length >= 150)
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
