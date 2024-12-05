import random

def SymbolBackstory(symbolName, symbolLook, symbolLocation):
    """
    Generates a backstory for a given symbol.

    Args:
        symbolName (str): The name of the symbol.
        symbolLook (str): The appearance or look of the symbol (e.g., '&').
        symbolLocation (tuple): The location of the symbol as (x, y).

    Returns:
        str: A backstory describing the symbol.
    """
    # Example elements for dynamic story generation
    origins = [
        "an ancient civilization that vanished thousands of years ago",
        "a secret guild of alchemists who sought immortality",
        "a long-forgotten order of knights sworn to protect the realm",
        "a mischievous deity who used it to hide great treasures",
        "an arcane scholar whose experiments went horribly wrong"
    ]

    powers = [
        "unlock the gates to a hidden kingdom",
        "grant eternal wisdom to its bearer",
        "unleash a terrible curse if disturbed",
        "reveal the secrets of the universe",
        "summon a guardian to protect its secrets"
    ]

    rumors = [
        "hidden deep within a forbidden forest",
        "buried beneath the ruins of a lost city",
        "guarded by a creature of unimaginable power",
        "engraved on the walls of an ancient temple",
        "etched into the stars themselves"
    ]

    # Generate random elements for the story
    origin = random.choice(origins)
    power = random.choice(powers)
    rumor = random.choice(rumors)

    # Construct the backstory
    backstory = (
        f"The symbol '{symbolName}', marked by its distinctive appearance '{symbolLook}', is said to have originated from {origin}. "
        f"Legends tell that it possesses the power to {power}. For centuries, adventurers and scholars alike have sought it, "
        f"believing it to be {rumor}. Its current location is believed to be at coordinates {symbolLocation}, "
        f"but none who ventured there have returned to confirm the truth."
    )

    return backstory

def EnvironmentalClues(symbolName, symbolLocation):
    """
    Generates environmental clues that hint at the symbol's presence.

    Args:
        symbolName (str): The name of the symbol.
        symbolLocation (tuple): The location of the symbol as (x, y).

    Returns:
        list: A list of clues describing the environment around the symbol.
    """
    clues = [
        "The air grows colder as you approach, and a faint hum resonates in the distance.",
        "Strange symbols, similar to the symbol's appearance, are etched into nearby rocks.",
        "The ground is scorched in peculiar patterns, as if by ancient magic.",
        "A cluster of twisted trees forms a natural barrier, their branches pointing towards the symbol's location.",
        "The faint smell of sulfur and the sound of whispering winds surround the area.",
        "Nearby wildlife avoids the location, and the silence is almost unnatural.",
        "You notice an ancient inscription on a crumbling wall: 'Here lies the mark of destiny.'",
        "A hidden path leads through dense vegetation, the trail marked by faint glowing lights at night."
    ]

    selected_clues = random.sample(clues, 3)  # Select 3 random clues
    return selected_clues

# Example usage
symbolName = "LostKey"
symbolLook = "&"
symbolLocation = (42, 87)

backstory = SymbolBackstory(symbolName, symbolLook, symbolLocation)
environmentalClues = EnvironmentalClues(symbolName, symbolLocation)

print(backstory)
print("\nEnvironmental Clues:")
for clue in environmentalClues:
    print(f"- {clue}")


# Example usage
symbolName = "LostKey"
symbolLook = "&"
symbolLocation = (42, 87)

backstory = SymbolBackstory(symbolName, symbolLook, symbolLocation)
print(backstory)
