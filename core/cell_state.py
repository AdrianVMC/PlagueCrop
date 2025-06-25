from enum import Enum, auto


class InfestationState(Enum):
    HEALTHY = auto()
    INFESTED = auto()
    RECOVERED = auto()


class DamageLevel(Enum):
    NONE = 0
    LOW = 1
    MODERATE = 2
    SEVERE = 3


class CropStage(Enum):
    GROWING = auto()
    GRAIN_FILL = auto()
    MATURE = auto()


class PlagueType(Enum):
    WORM = "worm"
    BUG = "bug"
    MIDGE = "midge"


class Cell:
    def __init__(self):
        # Crop state
        self.crop_stage = CropStage.GROWING
        self.infestation_state = InfestationState.HEALTHY
        self.damage_level = DamageLevel.NONE

        # Plague attributes
        self.plague_type = None
        self.plague_density = 0         # 0 to 3
        self.reproduction_capacity = 1  # 1 to 3
        self.damage_capacity = 1        # 1 to 3

        # Environmental modifiers (can also be global)
        self.pesticide_level = 1        # 1 to 3
        self.environment = {
            "humidity": 50,             # 0 to 100
            "solar_intensity": 2        # 1 to 3
        }
        self.occupied = True

    def is_infestable(self):
        return self.infestation_state == InfestationState.HEALTHY

    def can_spread(self):
        return self.infestation_state == InfestationState.INFESTED and self.plague_density > 0
