from core.cell_state import (
    Cell,
    InfestationState,
    DamageLevel,
    PlagueType,
    CropStage,
    ResistanceLevel
)
import random


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
    # Base chance from neighbor pressure
    base_chance = min(30 * infected_neighbors, 90)  # Máximo 90%

    # Environmental modifiers
    humidity = cell.environment.get("humidity", 50)
    solar = cell.environment.get("solar_intensity", 2)
    fertility = cell.environment.get("fertility", 0.5)

    humidity_factor = max(0, humidity - 50) / 2      # hasta +25
    solar_penalty = 10 if solar == 3 else 0
    fertility_modifier = 1.0 - (fertility * 0.3)      # entre 1.0 y 0.7

    # Plant resistance modifier
    resistance_factor = {
        ResistanceLevel.HIGH: -30,
        ResistanceLevel.MEDIUM: 0,
        ResistanceLevel.LOW: 20
    }.get(cell.resistance_level, 0)

    # Pesticide effect
    pesticide_effect = -15 * max(0, cell.pesticide_level - resistance)

    # Probabilidad final
    final_prob = (
        base_chance
        + humidity_factor
        - solar_penalty
        + resistance_factor
        + pesticide_effect
    )

    # Ajustar por fertilidad del suelo
    final_prob *= fertility_modifier

    # Limitar entre 5% y 95%
    final_prob = max(5, min(95, final_prob))

    # Decidir infección
    if random.random() < final_prob / 100:
        if cell.infestation_state == InfestationState.HEALTHY:
            return True
        elif cell.infestation_state == InfestationState.EXPOSED:
            cell.exposure_level = min(3, cell.exposure_level + 1)
            return cell.exposure_level >= 2  # múltiples exposiciones
    return False


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

        infected_neighbors = sum(1 for n in neighbors if n.infestation_state in [InfestationState.INFESTED_LIGHT, InfestationState.INFESTED_SEVERE])
        if should_infest(cell, infected_neighbors, infestation_power, pesticide_resistance):
            cell.infestation_state = InfestationState.INFESTED_LIGHT
            cell.infection_duration = 1
            cell.plague_density = 1
            cell.susceptibility_cooldown = susceptibility_cooldown

    elif cell.infestation_state == InfestationState.INFESTED_LIGHT:
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
    
    if cell.infestation_state == InfestationState.HEALTHY:
        if cell.susceptibility_cooldown > 0:
            cell.susceptibility_cooldown -= 1
        return

    infected_neighbors = sum(
        1 for n in neighbors if n.infestation_state in [InfestationState.INFESTED_LIGHT, InfestationState.INFESTED_SEVERE]
    )

    if should_infest(cell, infected_neighbors, infestation_power, pesticide_resistance):
        cell.infestation_state = InfestationState.EXPOSED
        cell.exposure_level = 1
        cell.susceptibility_cooldown = susceptibility_cooldown

    elif cell.infestation_state == InfestationState.EXPOSED:
        # Puede volver a HEALTHY o progresar a INFESTED_LIGHT
        if random.random() < 0.2:  # 20% chance to recover naturally
            cell.infestation_state = InfestationState.HEALTHY
        elif cell.exposure_level >= 2:
            cell.infestation_state = InfestationState.INFESTED_LIGHT
            cell.plague_density = 1

    elif cell.infestation_state == InfestationState.INFESTED_LIGHT:
        cell.plague_density = min(cell.plague_density + 0.2, 3)  # Crecimiento más lento
        if cell.plague_density > 1.5:
            cell.infestation_state = InfestationState.INFESTED_SEVERE
        
        # Daño progresivo
        if random.random() < 0.3:  # 30% chance de causar daño cada paso
            if cell.damage_level != DamageLevel.SEVERE:
                cell.damage_level = advance_damage_level(cell.damage_level)

    elif cell.infestation_state in [InfestationState.INFESTED_LIGHT, InfestationState.INFESTED_SEVERE]:
        # Comportamiento más agresivo
        cell.plague_density = min(cell.plague_density + 0.5, 5)  # Mayor densidad
        if random.random() < 0.6:  # 60% chance de causar daño
            if cell.damage_level != DamageLevel.SEVERE:
                cell.damage_level = advance_damage_level(cell.damage_level)
        
        # Posibilidad de recuperación después de mucho tiempo
        if cell.infection_duration >= recovery_cooldown * 1.5:
            if random() < 0.1:  # 10% chance de comenzar recuperación
                cell.infestation_state = InfestationState.RECOVERED
