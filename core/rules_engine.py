from core.cell_state import (
    Cell,
    InfestationState,
    DamageLevel,
    PlagueType,
    CropStage
)


def advance_damage_level(current_level: DamageLevel) -> DamageLevel:
    """Returns the next level of damage, up to SEVERE."""
    if current_level == DamageLevel.NONE:
        return DamageLevel.LOW
    elif current_level == DamageLevel.LOW:
        return DamageLevel.MODERATE
    elif current_level == DamageLevel.MODERATE:
        return DamageLevel.SEVERE
    return DamageLevel.SEVERE

def get_damage_capacity(plague_type: str, crop_type: str) -> int:
    """
    Returns how damaging a given plague is to a specific crop (1 to 3).
    """
    compatibility = {
        "WORM": {"MAIZE": 3, "RICE": 2, "WHEAT": 1},
        "BUG": {"MAIZE": 1, "RICE": 3, "WHEAT": 1},
        "MIDGE": {"MAIZE": 1, "RICE": 1, "WHEAT": 3},
    }
    return compatibility.get(plague_type, {}).get(crop_type, 1)


def should_infest(cell: Cell, infected_neighbors: int) -> bool:
    """
    Determines whether a healthy cell should become infested based on:
    - Number of infected neighbors
    - Environmental humidity
    - Solar intensity
    - Pesticide level
    """

    # Base chance scales with number of infected neighbors
    chance = infected_neighbors * 25

    # High humidity boosts infestation significantly
    if cell.environment["humidity"] > 60:
        chance += 30

    # High solar intensity discourages spread slightly
    if cell.environment["solar_intensity"] == 3:
        chance -= 10

    # Pesticides reduce chance sharply
    if cell.pesticide_level == 2:
        chance -= 20
    elif cell.pesticide_level == 3:
        chance -= 35

    return chance >= 40


def update_cell(cell: Cell, neighbors: list[Cell]) -> None:
    """
    Applies state transition rules to a given cell based on its own status and its neighbors.
    Modifies the cell in-place.
    """
    if cell.infestation_state == InfestationState.HEALTHY:
        infected_neighbors = sum(1 for n in neighbors if n.infestation_state == InfestationState.INFESTED)
        if should_infest(cell, infected_neighbors):
            cell.infestation_state = InfestationState.INFESTED
            cell.plague_density = 1
    elif cell.infestation_state == InfestationState.INFESTED:
        # Simulate plague development
        cell.plague_density = min(cell.plague_density + 1, 3)

        # Damage progression
        if cell.crop_stage != CropStage.MATURE:
            if cell.damage_level != DamageLevel.SEVERE:
                cell.damage_level = advance_damage_level(cell.damage_level)
    elif cell.infestation_state == InfestationState.INFESTED:
        cell.plague_density = min(cell.plague_density + 1, 3)

        if cell.crop_stage != CropStage.MATURE:
            for _ in range(cell.damage_capacity):  # más daño si la plaga es fuerte
                if cell.damage_level != DamageLevel.SEVERE:
                    cell.damage_level = advance_damage_level(cell.damage_level)

