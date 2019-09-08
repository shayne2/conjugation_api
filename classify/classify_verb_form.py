#!/usr/bin/env python3

import re

from data_structs.verbs import VerbForm, Mood, Tempo, Person, Number
from typing import Tuple

subj_pattern =  re.compile("([a-z]+\se\s[a-z]+)|((^|\s)(nos|eu|voces?|a\sgente|eles?|elas?)($|\s))|((^|\s)(o|a|os|as|esses?|essas?|estas?|estes?)\s+[a-z]+)")

first_person_pattern = re.compile("(.*(^|\s)(nos|eu|a\sgente)($|\s).*)|(.*([a-z]+\se\seu($|\s))|(eu\se\s[a-z]+).*)")
plural_pattern = re.compile("(.*(^|\s)(nos|voces|eles|elas|esses|essas)($|\s).*)|(.*[a-z]+\se\s[a-z]+.*)")

class VerbFormClassifier:
    # TODO: Add ctor that pulls in some sort of a universal resource hehe

    # TODO: Enforce that only valid states are returned
    # AKA Valid (Mood, Tempo) tuple
    def classify_by_frame(
        self,
        before: str,
        infinitive: str,
        after: str
    ) -> VerbForm:
        person = self.classify_person(before, infinitive, after)
        number = self.classify_number(before, infinitive, after)
        return VerbForm(
            # Placeholder
            mood=Mood.INDICATIVE,
            tempo=Tempo.PRESENT,
            person=person,
            number=number
        )

    def classify_person(
        self,
        before: str,
        infinitive: str,
        after: str
    ) -> Tuple[Person, Number]:
        subj = self.get_subj(before, infinitive, after)
        if subj:
            processed_subj_str = subj.lower().replace('ó', 'o')
            if first_person_pattern.match(processed_subj_str):
                return Person.FIRST
        return Person.THIRD

    def classify_number(
        self,
        before: str,
        infinitive: str,
        after: str
    ) -> Tuple[Person, Number]:
        subj = self.get_subj(before, infinitive, after)
        if subj:
            processed_subj_str = subj.lower()
            if plural_pattern.match(processed_subj_str):
                return Number.PLURAL
        return Number.SINGULAR

    def get_subj(
            self,
            before: str,
            infinitive: str,
            after: str
        ) -> str:
        # TODO: Try-Catch
        for context_string, match_position in ((before, -1), (after, 0)):
            context_string = context_string.lower().replace('ó', 'o').replace('ê','e')
            match_list = subj_pattern.findall(context_string)
            if len(match_list) > 0:
                for extracted in match_list[match_position]:
                    if extracted:
                        return extracted.strip()
        return ''
