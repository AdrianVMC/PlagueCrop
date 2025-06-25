from core.cell_state import (
    Cell,
    InfestationState,
    DamageLevel,
    PlagueType,
    CropStage
)


def advance_damage_level(current_level: DamageLevel) -> DamageLevel:
    if current_level == DamageLevel.NONE:
        return DamageLevel.LOW
    elif current_level == DamageLevel.LOW:
        return DamageLevel.MODERATE
    elif current_level == DamageLevel.MODERATE:
        return DamageLevel.SEVERE
    return DamageLevel.SEVERE


def get_damage_capacity(plague_type: str, crop_type: str) -> int:
    compatibility = {
        "WORM": {"MAIZE": 3, "RICE": 2, "WHEAT": 1},
        "BUG": {"MAIZE": 1, "RICE": 3, "WHEAT": 1},
        "MIDGE": {"MAIZE": 1, "RICE": 1, "WHEAT": 3},
    }
    return compatibility.get(plague_type, {}).get(crop_type, 1)


def should_infest(cell: Cell, infected_neighbors: int, infestation_power: int = 1) -> bool:
    chance = infected_neighbors * 25 * infestation_power

    if cell.environment["humidity"] > 60:
        chance += 30

    if cell.environment["solar_intensity"] == 3:
        chance -= 10

    if cell.pesticide_level == 2:
        chance -= 20
    elif cell.pesticide_level == 3:
        chance -= 35

    return chance >= 40


def update_cell(cell: Cell, neighbors: list[Cell], infestation_power: int = 1, settings: dict = None) -> None:
    settings = settings or {}
    infection_threshold = settings.get("infection_duration_threshold", 3)
    recovery_cooldown = settings.get("recovery_cooldown", 5)

    if cell.infestation_state == InfestationState.HEALTHY:
        infected_neighbors = sum(1 for n in neighbors if n.infestation_state == InfestationState.INFESTED)
        if should_infest(cell, infected_neighbors, infestation_power):
            cell.infestation_state = InfestationState.INFESTED
            cell.infection_duration = 1
            cell.plague_density = 1

    elif cell.infestation_state == InfestationState.INFESTED:
        cell.infection_duration += 1
        cell.plague_density = min(cell.plague_density + 1, 3)
        if cell.infection_duration >= infection_threshold:
            cell.infestation_state = InfestationState.RECOVERED
            cell.recovery_timer = recovery_cooldown
        else:
            if cell.crop_stage != CropStage.MATURE:
                for _ in range(cell.damage_capacity):
                    if cell.damage_level != DamageLevel.SEVERE:
                        cell.damage_level = advance_damage_level(cell.damage_level)

    elif cell.infestation_state == InfestationState.RECOVERED:
        cell.recovery_timer -= 1
        if cell.recovery_timer <= 0:
            cell.infestation_state = InfestationState.HEALTHY
            cell.infection_duration = 0
