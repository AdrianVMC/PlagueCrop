from enum import Enum, auto

class InfestationState(Enum):
    HEALTHY = auto()
    EXPOSED = auto()
    INFESTED_LIGHT = auto()
    INFESTED_SEVERE = auto()
    RECOVERED = auto()
    DAMAGED = auto()

class ResistanceLevel(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class DamageLevel(Enum):
    NONE = auto()
    LOW = auto()
    MODERATE = auto()
    SEVERE = auto()

class CropStage(Enum):
    GRAIN = auto()
    GROWING = auto()
    MATURE = auto()

class PlagueType(Enum):
    WORM = auto()
    BUG = auto()
    FLY = auto()

class Cell:
    def __init__(self, resistance_level=ResistanceLevel.MEDIUM, fertility=0.5):
        self.infestation_state = InfestationState.HEALTHY
        self.damage_level = DamageLevel.NONE
        self.crop_stage = CropStage.GROWING
        self.plague_type = None
        self.plague_density = 0
        self.damage_capacity = 1
        self.environment = {
            "humidity": 50,
            "solar_intensity": 2,
            "fertility": fertility
        }
        self.pesticide_level = 1
        self.occupied = False
        self.infection_duration = 0
        self.recovery_timer = 0
        self.susceptibility_cooldown = 0
        self.resistance_level = resistance_level
