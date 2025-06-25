from core.cell_state import Cell, InfestationState, PlagueType, CropStage, ResistanceLevel
from core.rules_engine import update_cell, get_damage_capacity
from random import randint, random

class CellAutomaton:
    def __init__(self, rows: int, cols: int, settings: dict = None):
        self.rows = rows
        self.cols = cols
        self.settings = settings or {}
        self.grid = [[self._create_cell() for _ in range(cols)] for _ in range(rows)]
        self.seed_infestation()

    def _create_cell(self) -> Cell:
        humidity = self.settings.get("humidity", 50)
        solar_intensity = self.settings.get("solar_intensity", 2)
        pesticide_level = self.settings.get("pesticide_level", 1)
        fertility = self.settings.get("soil_fertility", 0.5)
        occupation_density = self.settings.get("occupation_density", 80) / 100.0

        resistance_str = self.settings.get("resistance_level", "MEDIUM").upper()
        resistance_level = ResistanceLevel[resistance_str] if resistance_str in ResistanceLevel.__members__ else ResistanceLevel.MEDIUM

        cell = Cell(resistance_level=resistance_level, fertility=fertility)
        cell.environment["humidity"] = humidity
        cell.environment["solar_intensity"] = solar_intensity
        cell.pesticide_level = pesticide_level
        cell.occupied = random() < occupation_density

        crop_stage_str = self.settings.get("crop_stage", "GROWING")
        try:
            cell.crop_stage = CropStage[crop_stage_str]
        except KeyError:
            cell.crop_stage = CropStage.GROWING

        return cell

    def seed_infestation(self):
        plague_type = self.settings.get("plague_type", "WORM")
        crop_type = self.settings.get("crop_type", "MAIZE")
        damage_capacity = get_damage_capacity(plague_type, crop_type)

        density = self.settings.get("infestation_density", "MEDIUM").upper()
        total_cells = self.rows * self.cols

        count = {
            "LOW": total_cells // 100,
            "MEDIUM": total_cells // 40,
            "HIGH": total_cells // 20
        }.get(density, 5)

        seeded = 0
        attempts = 0
        max_attempts = count * 10

        while seeded < count and attempts < max_attempts:
            x = randint(0, self.rows - 1)
            y = randint(0, self.cols - 1)
            cell = self.grid[x][y]
            if cell.infestation_state == InfestationState.HEALTHY and cell.occupied:
                cell.infestation_state = InfestationState.INFESTED_LIGHT
                cell.plague_type = plague_type
                cell.plague_density = 1
                cell.damage_capacity = damage_capacity
                seeded += 1
            attempts += 1

    def initialize_with_settings(self, settings: dict):
        self.settings = settings
        self.grid = [[self._create_cell() for _ in range(self.cols)] for _ in range(self.rows)]
        self.seed_infestation()

    def get_grid(self):
        return self.grid

    def get_neighbors(self, row: int, col: int) -> list:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append(self.grid[nx][ny])
        return neighbors

    def step(self):
        for x in range(self.rows):
            for y in range(self.cols):
                cell = self.grid[x][y]
                neighbors = self.get_neighbors(x, y)
                infestation_power = self.settings.get("infestation_power", 1)
                update_cell(cell, neighbors, infestation_power=infestation_power, settings=self.settings)
