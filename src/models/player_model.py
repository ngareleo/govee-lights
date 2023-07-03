from dataclasses import dataclass
import pandas as pd

@dataclass
class Player:
    name: str
    age: int
    height: float = 159
    pace_total: int = 50
    shooting_total: int = 50
    passing_total: int = 50
    dribbling_total: int = 50
    defending_total: int = 50
    physicality_total: int = 50
    crossing: int = 50
    finishing: int = 50
    heading_accuracy: int = 50
    short_passing: int = 50
    volleys: int = 50
    dribbling: int = 50
    curve: int = 50
    freekick_accuracy: int = 50
    long_passing: int = 50
    ball_control: int = 50
    acceleration: int = 50
    sprint_speed: int = 50
    agility: int = 50
    reactions: int = 50
    balance: int = 50
    shot_power: int = 50
    jumping: int = 50
    stamina: int = 50
    strength: int = 50
    long_shots: int = 50
    aggression: int = 50
    interceptions: int = 50
    positioning: int = 50
    vision: int = 50
    penalties: int = 50
    composure: int = 50
    marking: int = 50
    standing_tackle: int = 50
    sliding_tackle: int = 50
    gk_diving: int = 50
    gk_handling: int = 50
    gk_kicking: int = 50
    gk_reflexes: int = 50
    gk_speed: int = 50
    gk_positioning: int = 50

    def to_dataframe(self):
        return pd.DataFrame([self.__dict__])


