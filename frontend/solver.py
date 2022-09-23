from itertools import permutations

from frontend.models import BaseMatch, MatchState, Person, Sex


def solve(people: list[Person], matches: list[BaseMatch]):
    no_matches = [m for m in matches if m.match_state == MatchState.NO_MATCH]
    perfect_matches = [m for m in matches if m.match_state == MatchState.PERFECT_MATCH]

    females = [p for p in people if p.sex == Sex.FEMALE]
    males = [p for p in people if p.sex == Sex.MALE]

    # Get all fixed Male-Female combinations from the PerfectMatches
    fixed = []
    for match in perfect_matches:
        males = [m for m in males if m.id != match.male.id]
        females = [f for f in females if f.id != match.female.id]
        fixed.append((match.male, match.female))

    # We try to 'give' each non-fixed Male a Female
    n_males = len(males)
    perms = permutations(females, n_males)

    possible_solutions = []

    # check each permutation of the non-fixed people if it is possible
    for i, perm in enumerate(perms):
        # generate (Male, Female) of this permutation
        combinations = list(zip(males, perm))
        possible = True

        # check if combination of (Males, Females) is possible with the known
        # NoMatches
        for combination in combinations:
            for no_match in no_matches:
                if (
                    combination[0].pk == no_match.male.pk
                    and combination[1].pk == no_match.female.pk
                ):
                    possible = False
                if (
                    combination[0].pk == no_match.female.pk
                    and combination[1].pk == no_match.male.pk
                ):
                    possible = False

        if possible:
            # Combine the known PerfectMatches with the found combination and add it
            # as a candidate
            possible_solutions.append(fixed + combinations)

    return possible_solutions
