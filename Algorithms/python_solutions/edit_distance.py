"""
Edit Distance Calculation Module
============================================

This module provides functions to calculate the edit distance between two
strings using different distance metrics. It includes functions for Hamming
distance, Jaro similarity, and uses the Longest Common Subsequence and
Damerau-Levenshtein distance algorithms for more complex edit distance
calculations.


Functions
---------
edit_distance(str1: str, str2: str, distance: str = 'dl') -> float
    Compute the edit distance between two strings using a specified distance
    metric.

hamming_distance(str1: str, str2: str) -> int
    Calculate the Hamming distance between two strings.

jaro_distance(str1: str, str2: str) -> float
    Calculate the Jaro similarity between two strings.

"""

from Algorithms.python_solutions.dynamic_programming \
    import LongestCommonSubsequence, DamerauLevensteinDistance


def edit_distance(str1, str2, distance='dl'):
    """
    Compute the edit distance between two strings.

    This function calculates the edit distance between two input strings
    using one of the available distance metrics. You can choose the
    following metrics: Jaro, Hamming, LongestCommonSubsequence or
    DamerauLevensteinDistance.

    DamerauLevensteinDistance is the most universal of them.
    Jaro distance can be the metric for the distance between the strings
    containing matching and transposing characters.
    LongestCommonSubsequence distance is a metric for edit distance, using
    the length of LCS of the strings.
    Hamming distance works only for the strings with the same length and
    share a large share of characters (including their positions), e.g.
    'karoline' and 'kathrine'.

    Parameters
    ----------
    str1 : str
        The first input string.

    str2 : str
        The second input string.

    distance : str, optional
        The distance metric to use. Possible values are
        'jaro' for Jaro distance,
        'hamming' for Hammimg distance,
        'lcs' for distance based on the LongestCommonSubsequence or
        'dl' for DamerauLevensteinDistance.
        Default is 'dl'.

    Returns
    -------
    float
        The computed edit distance based on the selected distance metric.

    Raises
    ------
    ValueError
        Raised if the distance is 'hamming' and the input strings have
        different lengths.

    """
    if distance == 'jaro':
        return jaro_distance(str1, str2)
    elif distance == 'hamming':
        return hamming_distance(str1, str2)
    elif distance == 'lcs':
        return float(LongestCommonSubsequence(str1, str2).solve())
    elif distance == 'dl':
        return float(DamerauLevensteinDistance(str1, str2).solve_optimized())


def hamming_distance(str1, str2):
    """
    Calculate the Hamming distance between two strings.

    The Hamming distance is the number of positions at which the
    corresponding elements in the input strings of the same length are
    different.

    Parameters
    ----------
    str1 : str
        The first input string.

    str2 : str
        The second input string.

    Returns
    -------
    int
        The Hamming distance between the two input strings.

    Raises
    ------
    ValueError
        Raised if the input strings have different lengths.

    """
    if len(str1) != len(str2):
        raise ValueError(
            "Hamming distance is only defined for strings of equal length.")
    return sum(el1 != el2 for el1, el2 in zip(str1, str2))


def jaro_distance(str1, str2):
    """
    Calculate the Jaro similarity between two strings.

    The Jaro similarity measures the similarity between two strings.
    A higher value indicates more similarity between the strings.
    The general formula looks the following way:
    d = (matches / length1 + matches / length2 + (matches - transpositions)
    / matches) / 3, where
    matches are matches of the characters in the strings if they are not
    not farther than int(max(length1, length2) / 2) - 1 characters apart,
    length1 and length2 are lengths of the first and the second strings
    accordingly,
    transpositions is the number of matching characters that are not in the
    right order.

    Parameters
    ----------
    str1 : str
        The first input string.

    str2 : str
        The second input string.

    Returns
    -------
    float
        The Jaro similarity between the two input strings.

    """
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
    for i in range(min(len1, len2)):
        if matched2[k] != -1:
            if str1[i] != str2[i]:
                transpositions += 1
            k += 1

    transpositions /= 2
    jaro_sim = (matches / len1 +
                matches / len2 +
                (matches - transpositions) / matches) / 3
    return jaro_sim
