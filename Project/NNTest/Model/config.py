from dataclasses import dataclass


@dataclass
class TrainingConfig:
    epochs: int
    loss_func: str
    metrics: list
    optimizer: str
