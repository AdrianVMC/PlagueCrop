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
        "WORM": {"MAIZE": 3, "RICE": 2, "WHEAT": 2},
        "BUG": {"MAIZE": 1, "RICE": 3, "BEAN": 3},
        "FLY": {"WHEAT": 3, "BEAN": 2, "RICE": 1},
    }
    return compatibility.get(plague_type, {}).get(crop_type, 1)


def get_plague_behavior(plague_type: str) -> dict:
    behaviors = {
        "WORM": {
            "infestation_power": 3,
            "damage_per_step": 2,
            "pesticide_resistance": 2
        },
        "BUG": {
            "infestation_power": 2,
            "damage_per_step": 1,
            "pesticide_resistance": 3
        },
        "FLY": {
            "infestation_power": 4,
            "damage_per_step": 1,
            "pesticide_resistance": 1
        }
    }
    return behaviors.get(plague_type, {"infestation_power": 1, "damage_per_step": 1, "pesticide_resistance": 1})


def should_infest(cell: Cell, infected_neighbors: int, infestation_power: int = 1, resistance: int = 1) -> bool:
    chance = infected_neighbors * 25 * infestation_power

    if cell.environment["humidity"] > 60:
        chance += 30

    if cell.environment["solar_intensity"] == 3:
        chance -= 10

    if cell.pesticide_level >= resistance:
        chance -= 30 * (cell.pesticide_level - resistance + 1)

    return chance >= 40


def update_cell(cell: Cell, neighbors: list[Cell], infestation_power: int = 1, settings: dict = None) -> None:
    settings = settings or {}
    infection_threshold = settings.get("infection_duration_threshold", 3)
    recovery_cooldown = settings.get("recovery_cooldown", 5)
    susceptibility_cooldown = settings.get("susceptibility_cooldown", 3)
    plague_type = settings.get("plague_type", "WORM")
    crop_type = settings.get("crop_type", "MAIZE")

    plague_behavior = get_plague_behavior(plague_type)
    infestation_power = plague_behavior["infestation_power"]
    pesticide_resistance = plague_behavior["pesticide_resistance"]
    damage_per_step = plague_behavior["damage_per_step"]

    cell.damage_capacity = get_damage_capacity(plague_type, crop_type)

    if not cell.occupied:
        return

    if cell.infestation_state == InfestationState.HEALTHY:
        if hasattr(cell, "susceptibility_cooldown") and cell.susceptibility_cooldown > 0:
            cell.susceptibility_cooldown -= 1
            return

        infected_neighbors = sum(1 for n in neighbors if n.infestation_state == InfestationState.INFESTED)
        if should_infest(cell, infected_neighbors, infestation_power, pesticide_resistance):
            cell.infestation_state = InfestationState.INFESTED
            cell.infection_duration = 1
            cell.plague_density = 1
            cell.susceptibility_cooldown = susceptibility_cooldown

    elif cell.infestation_state == InfestationState.INFESTED:
        cell.infection_duration += 1
        cell.plague_density = min(cell.plague_density + 1, 3)
        if cell.infection_duration >= infection_threshold:
            cell.infestation_state = InfestationState.RECOVERED
            cell.recovery_timer = recovery_cooldown
        else:
            if cell.crop_stage != CropStage.MATURE:
                for _ in range(min(cell.damage_capacity, damage_per_step)):
                    if cell.damage_level != DamageLevel.SEVERE:
                        cell.damage_level = advance_damage_level(cell.damage_level)

    elif cell.infestation_state == InfestationState.RECOVERED:
        cell.recovery_timer -= 1
        if cell.recovery_timer <= 0:
            cell.infestation_state = InfestationState.HEALTHY
            cell.infection_duration = 0
            cell.susceptibility_cooldown = susceptibility_cooldown
