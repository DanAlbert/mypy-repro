from dataclasses import dataclass

from game.theater import FrontLine
from ..packageplanningtask import PackagePlanningTask


@dataclass
class PlanCas(PackagePlanningTask[FrontLine]):
    pass
