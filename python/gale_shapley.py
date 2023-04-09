"""
Write a function that takes in two two-dimensional lists and returns a list of lists. Known as the Gale Shapley algorithm.
"""


def stableInternships(interns, teams):

    unmatched = list(range(len(interns)))
    pref = [{x:i for i, x in enumerate(t)} for t in teams]

    intern_pref = [0] * len(interns)

    pairs = {}

    while unmatched:
        idx = unmatched.pop()
        elem = interns[idx][intern_pref[idx]]
        intern_pref[idx] += 1

        if elem not in pairs:
            pairs[elem] = idx

        else:
            if pref[elem][idx] < pref[elem][pairs[elem]]:
                unmatched.append(pairs[elem])
                pairs[elem] = idx
    
            else:
                unmatched.append(idx)

    return [[y, x] for x, y in pairs.items()]


if __name__ == "__main__":
    print(stableInternships([[1, 2, 3], [4, 5,6]], [[1, 2, 3], [4, 5, 6]])) # [[1, 4], [0, 1]]