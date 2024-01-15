# correcter.py

"""
Swaps the old "raw-wood" signal to "artillery-wagon", or some other configurable
signal. Creates a blueprint that aligns to the player's origin, so you don't 
have to manually replace it.

Requirements:
    factorio-draftsman >= 0.9.0
"""

from draftsman.blueprintable import Blueprint
from draftsman.entity import ArithmeticCombinator

# bottom
# tile -147, 130 
# tile -75, 130
# tile -3, 130
# tile 69, 130
# tile 141, 130

# top
# tile -147, -130
# tile -75, -130
# tile -3, -130
# tile 69, -130
# tile 141, -130

def main():
    replacement_signal = "artillery-wagon"

    blueprint = Blueprint()
    
    combinator = ArithmeticCombinator("arithmetic-combinator", direction=2)
    combinator.set_arithmetic_conditions(replacement_signal, "+", 0, "signal-A")

    positions = [
        # Top
        (-147, -130),
        (-75,  -130),
        (-3,   -130),
        (69,   -130),
        (141,  -130),
        # Bottom
        (-147,  130),
        (-75,   130),
        (-3,    130),
        (69,    130),
        (141,   130),
    ]

    for position in positions:
        print(position)
        combinator.tile_position = position
        blueprint.entities.append(combinator)

    # Snapping stuff
    blueprint.snapping_grid_size = (600, 600)
    blueprint.absolute_snapping = True
    blueprint.snapping_grid_position = (-300, -300)
    blueprint.position_relative_to_grid = (300, 300)
    

    print(blueprint.to_dict())
    print(blueprint.to_string())


if __name__ == "__main__":
    main()