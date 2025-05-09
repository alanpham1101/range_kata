from collections import defaultdict
from functools import cmp_to_key
from enum import Enum

from range import Range


class Generation(Enum):
    SILENT_GENERATION = "silent_generation"
    BABY_BOOMERS = "baby_boomers"
    GENERATION_X = "generation_x"
    GENERATION_Y = "generation_y"
    GENERATION_Z = "generation_z"
    GENERATION_ALPHA = "generation_alpha"


class GenerationMapping:
    GENERATION_NAMES = {
        Generation.SILENT_GENERATION: "Silent Generation",
        Generation.BABY_BOOMERS: "Baby Boomers",
        Generation.GENERATION_X: "Generation X",
        Generation.GENERATION_Y: "Generation Y",
        Generation.GENERATION_Z: "Generation Z",
        Generation.GENERATION_ALPHA: "Generation Alpha"
    }

    GENERATION_RANGES = {
        Generation.SILENT_GENERATION: Range.less_than(1946),
        Generation.BABY_BOOMERS: Range.closed(1946, 1964),
        Generation.GENERATION_X: Range.closed(1965, 1980),
        Generation.GENERATION_Y: Range.closed(1981, 1996),
        Generation.GENERATION_Z: Range.closed(1997, 2012),
        Generation.GENERATION_ALPHA: Range.greater_than(2012)
    }


def analyze_member_demography(members: list[dict]) -> dict[str, list[dict]]:
    def compare(member1, member2):
        return int(member1["birthdate"][:4]) - int(member2["birthdate"][:4])

    res = defaultdict(list)
    generations = list(GenerationMapping.GENERATION_RANGES.items())

    gen_index = 0
    for member in sorted(members, key=cmp_to_key(compare)):
        year = int(member["birthdate"][:4])
        while gen_index < len(generations):
            name, ranges = generations[gen_index]
            if ranges.contains(year):
                res[GenerationMapping.GENERATION_NAMES[name]].append(member)
                break
            gen_index += 1
    return res


def check_member_format(members: dict) -> bool:
    for member in members:
        if "name" not in member or "birthdate" not in member:
            return False
    return True
