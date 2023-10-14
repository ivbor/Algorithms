from Algorithms.python_solutions.dynamic_programming \
    import LongestCommonSubsequence, DamerauLevensteinDistance


def edit_distance(str1, str2, distance='jaro'):
    if distance == 'jaro':
        return jaro_distance(str1, str2)
    elif distance == 'hamming':
        return hamming_distance(str1, str2)
    elif distance == 'lcs':
        return LongestCommonSubsequence(str1, str2).solve()
    elif distance == 'dl':
        return DamerauLevensteinDistance(str1, str2).solve()


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError(
            "Hamming distance is only defined for strings of equal length.")
    return sum(el1 != el2 for el1, el2 in zip(str1, str2))


def jaro_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 == 0 or len2 == 0:
        return 0.0

    max_dist = max(len1, len2) // 2 - 1
    matches = 0
    transpositions = 0
    matched2 = [-1] * len2

    for i in range(len1):
        start = max(0, i - max_dist)
        end = min(i + max_dist + 1, len2)
        for j in range(start, end):
            if str1[i] == str2[j] and matched2[j] == -1:
                matches += 1
                matched2[j] = i
                break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(len1):
        if matched2[k] != -1:
            if str1[i] != str2[matched2[k]]:
                transpositions += 1
            k += 1

    jaro_sim = (matches / len1 +
                matches / len2 +
                (matches - transpositions) / matches) / 3
    return jaro_sim
