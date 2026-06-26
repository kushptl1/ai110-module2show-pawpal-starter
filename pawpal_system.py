from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional


@dataclass
class Owner:
    name: str
    preferences: Dict[str, str] = field(default_factory=dict)
    daily_time_budget: int = 0

    def update_preferences(self, pref: Dict[str, str]) -> None:
        pass

    def can_schedule(self, duration: int) -> bool:
        pass

    def summary(self) -> str:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: Optional[int] = None
    care_requirements: Dict[str, str] = field(default_factory=dict)

    def update_info(self, info: Dict[str, str]) -> None:
        pass

    def needs_task(self, task_type: str) -> bool:
        pass

    def summary(self) -> str:
        pass


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str
    recurrence: Optional[str] = None

    def is_high_priority(self) -> bool:
        pass

    def format_label(self) -> str:
        pass

    def matches_category(self, category: str) -> bool:
        pass

    def update(self, details: Dict[str, str]) -> None:
        pass


@dataclass
class Schedule:
    date: date
    tasks: List[Task] = field(default_factory=list)
    total_duration: int = 0
    notes: str = ""

    def add_task(self, task: Task, start_time: str) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def sort_by_time(self) -> None:
        pass

    def summary(self) -> str:
        pass

    def explain(self) -> str:
        pass


@dataclass
class Scheduler:
    owner: Owner
    pet: Pet
    task_list: List[Task] = field(default_factory=list)
    constraints: Dict[str, str] = field(default_factory=dict)

    def generate_schedule(self) -> Schedule:
        pass

    def filter_tasks(self) -> List[Task]:
        pass

    def rank_tasks(self) -> List[Task]:
        pass

    def assign_times(self, tasks: List[Task]) -> Schedule:
        pass

    def validate_schedule(self, schedule: Schedule) -> bool:
        pass
