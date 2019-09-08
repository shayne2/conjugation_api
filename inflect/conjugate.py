#!/usr/bin/env python3

from data_structs.verbs import VerbForm, Mood, Tempo, Person, Number, \
    person_to_int, number_to_int
from typing import Dict
import json

class VerbConjugator:
    def __init__(self) -> None:
        # load from text file
        with open('rules/regular_suffixes/present_indicative.json') as suffix_file:
            self.present_indicative_lookup = json.load(suffix_file)
        with open('rules/irregular_conjugations/present_indicative.json') as irreg_file:
            self.present_indicative_irregulars = json.load(irreg_file)

    def conjugate_verb(self, infinitive: str, verb_form: VerbForm) -> str:
        mood = verb_form.mood
        if mood == Mood.INDICATIVE:
            return self.conjugate_indicative(infinitive, verb_form)
        elif mood == Mood.SUBJUNCTIVE:
            return self.conjugate_subjunctive(infinitive, verb_form)
        else:
            return self.conjugate_imperative(infinitive, verb_form)

    def conjugate_indicative(self, infinitive: str, verb_form: VerbForm) -> str:
        tempo = verb_form.tempo
        if tempo == Tempo.PRESENT:
            return self.conjugate_by_number_and_person(
                infinitive,
                number_to_int(verb_form.number),
                person_to_int(verb_form.person),
                self.present_indicative_lookup,
                self.present_indicative_irregulars
            )
        elif tempo == Tempo.PRETERITE_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_IMPERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_MAIS_QUE_PERFEITO:
            raise NotImplementedError
        elif tempo == Tempo.PRESENT_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_PERFECT_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_IMPERFECT_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.FUTURE_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.CONDITIONAL_PERFECT:
            raise NotImplementedError
        else:
            raise NotImplementedError

    def conjugate_by_number_and_person(
        self,
        infinitive: str,
        number: int,
        person: int,
        regular_suffixes: Dict,
        irregulars: Dict
    ) -> str:

        if infinitive in irregulars:
            irregular_conjugation =  \
                irregulars[infinitive][number][person]
            if irregular_conjugation:
                return irregular_conjugation

        last_two_letters = infinitive[-2:]
        if last_two_letters not in regular_suffixes:
            raise ValueError("Invalid infinitive provided")

        suffix = regular_suffixes[last_two_letters][number][person]
        stem = infinitive[:-2]
        return "{}{}".format(stem, suffix)

    # WHICH??
    def get_past_participle(self, verb: str) -> str:
        raise NotImplementedError

    def get_present_progressive(self, verb: str) -> str:
        raise NotImplementedError

    def conjugate_subjunctive(self, verb: str, verb_form: VerbForm) -> str:
        raise NotImplementedError

    def conjugate_imperative(self, verb: str, verb_form: VerbForm) -> str:
        raise NotImplementedError


# TODO: Custom exception for bad state of mood + tempo combinations
