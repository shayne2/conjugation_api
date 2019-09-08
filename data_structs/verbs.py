#!/usr/bin/env python3

from enum import Enum, auto
from typing import NamedTuple


class Mood(Enum):
    INDICATIVE = auto()
    SUBJUNCTIVE = auto()
    IMPERATIVE = auto()


class Tempo(Enum):
    # Simple
    PRESENT = auto()
    PRETERITE_PERFECT = auto()
    PRETERITE_IMPERFECT = auto()
    PRETERITE_MAIS_QUE_PERFEITO = auto()
    FUTURE = auto()
    CONDITIONAL = auto()

    # Perfect
    PRESENT_PERFECT = auto()
    PRETERITE_PERFECT_PERFECT = auto()
    PRETERITE_IMPERFECT_PERFECT  = auto()
    FUTURE_PERFECT = auto()
    CONDITIONAL_PERFECT = auto()

    # Imperative
    AFFIRAMTIVE = auto()
    NEGATIVE = auto()
    IMPERSONAL_INFINITIVE = auto()


class Person(Enum):
    FIRST = 0
    THIRD = 1


class Number(Enum):
    SINGULAR = 0
    PLURAL = 1


class VerbForm(NamedTuple):
    mood: Mood
    tempo: Tempo
    person: Person
    number: Number


def person_to_int(val: Person):
    lookup = (Person.FIRST, Person.THIRD)
    return lookup.index(val)

def number_to_int(val: Number):
    lookup = (Number.SINGULAR, Number.PLURAL)
    return lookup.index(val)
