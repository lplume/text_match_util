#!/usr/bin/env python
# encoding: UTF-8

"""Text Match Util"""

import re
from fuzzywuzzy import fuzz

__author__ = "faildev"
__license__ = "GPLv3"
__version__ = "1.0"

# always return (1, 2, 3, 4)
# 4 oggetto "third" che ha effettuato il match            [match_object] useless???
# 1 in base al threshold (o match) True o False del match [match_result]
# 2 ratio in % (convertire in lista di ratio)             [match_ratio]
# 3 match sull'against                                    [matched]

# todos
# aggiungere levenshtein per match di typo
#   insert  = 0
#   replace = 2
#   delete  = 1

def strict_match(match, against, threshold=96):
    """Strict match, using == operator.
    Threshold does not make any sense, it's either
    0 or 100"""
    match_object = match == against
    match_ratio = match_object * 100
    match_result = match_ratio >= threshold
    matched = None
    if match_result:
        matched = against

    return match_result, match_ratio, matched, match_object

def nocase_match(match, against, threshold=96):
    """No case match, it lower the strings and match.
    Threshold does not make any sense, it's either
    the ratio will be 0 or 100 either True or False if it match or not"""
    match_object = match == against
    match_ratio = match_object * 100
    match_result = match_ratio >= threshold
    matched = None
    if match_result:
        matched = against

    return match_result, match_ratio, matched, match_object

def cred(dictionary, name, pattern):
    """Compile a regex with a given name into a dictionary"""
    dictionary[name] = re.compile(pattern)
    return dictionary

def rematch(pattern, against, dictionary=None):
    """Regex match against a pattern or against a compiled
    pattern into a cred dictionary with the pattern as a given name.
    The ratio will be 100 if there is a match. Threshold does not
    make any sense, if there is a match than it returns True"""
    if dictionary:
        compiled = dictionary[pattern]
    else:
        compiled = re.compile(pattern)

    match_object = compiled.match(against)
    match_result = False
    match_ratio = 0
    matched = None

    if match_object:
        match_result = True
        match_ratio = 100
        matched = match_object.group()

    return match_result, match_ratio, matched, match_object

def research(pattern, against, dictionary=None):
    """Regex match against a pattern or against a compiled
    pattern into a cred dictionary with the pattern as a given name.
    The ratio will be 100 if there is a match. Threshold does not
    make any sense, if there is a match than it returns True"""
    if dictionary:
        compiled = dictionary[pattern]
    else:
        compiled = re.compile(pattern)

    match_object = compiled.search(against)
    match_result = False
    match_ratio = 0
    matched = None

    if match_object:
        match_result = True
        match_ratio = 100
        matched = match_object.group()

    return match_result, match_ratio, matched, match_object

def refindall(pattern, against, dictionary=None):
    """TODO description"""
    if dictionary:
        compiled = dictionary[pattern]
    else:
        compiled = re.compile(pattern)

    match_object = compiled.findall(against)
    match_result = False
    match_ratio = 0
    matched = None

    if match_object:
        match_result = True
        match_ratio = 100
        matched = match_object

    return match_result, match_ratio, matched, match_object

def refinditer(pattern, against, dictionary=None):
    """TODO description"""
    if dictionary:
        compiled = dictionary[pattern]
    else:
        compiled = re.compile(pattern)

    match_object = compiled.finditer(against)
    match_result = False
    match_ratio = 0
    matched = None

    if match_object:
        match_result = True
        match_ratio = 100
        matched = match_object

    return match_result, match_ratio, matched, match_object

def frasimple(match, against, threshold=96):
    """Fuzzy(wuzzy) simple ratio: measurement of edit distance.
    Works fine for very short strings (such as a single word) and very long
    strings (such as a full book), but not so much for 3-10 word labels"""
    match_ratio = match_object = fuzz.ratio(match, against)
    match_result = match_ratio >= threshold
    matched = None

    if match_result:
        matched = against

    return match_result, match_ratio, matched, match_object

def frapartial(match, against, threshold=96):
    """Fuzzy(wuzzy) partial ratio.
    Good on searching partial match (match a substring or alike of a bigger
    string)"""
    match_ratio = match_object = fuzz.partial_ratio(match, against)
    match_result = match_ratio >= threshold
    matched = None

    if match_result:
        matched = against

    return match_result, match_ratio, matched, match_object

def fratoken_sort(match, against, threshold=96):
    """Fuzzy(wuzzy) token sort.
    Aims to solve ordering problems"""
    match_ratio = match_object = fuzz.token_sort_ratio(match, against)
    match_result = match_ratio >= threshold
    matched = None

    if match_result:
        matched = against

    return match_result, match_ratio, matched, match_object

def fratoken_set(match, against, threshold=96):
    """Fuzzy(wuzzy) token set.
    More flexible than only trying to solve ordening problems."""
    match_ratio = match_object = fuzz.token_set_ratio(match, against)
    match_result = match_ratio >= threshold
    matched = None

    if match_result:
        matched = against

    return match_result, match_ratio, matched, match_object



# leven php 0,2,1 typo su parole

# 1 - levn / sumchars