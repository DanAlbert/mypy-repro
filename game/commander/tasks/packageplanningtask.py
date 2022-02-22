from dataclasses import dataclass
from typing import Generic, TypeVar

MissionTargetT = TypeVar("MissionTargetT", bound=MissionTarget)


@dataclass
class PackagePlanningTask(Generic[MissionTargetT]):
    target: MissionTargetT
