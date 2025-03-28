# package_sorter.py

def sort(width, height, length, mass):
    """
    Classifies a package into the appropriate dispatch stack based on size and weight.

    Args:
        width (int): Width of the package in centimeters.
        height (int): Height of the package in centimeters.
        length (int): Length of the package in centimeters.
        mass (int): Mass of the package in kilograms.

    Returns:
        str: One of "STANDARD", "SPECIAL", or "REJECTED".
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"
