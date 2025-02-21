#include <string.h>
#include <math.h>

int DamerauLevensteinDistance(char *s1, char *s2) {
    // Create a table to store the results of subproblems
    int dp[strlen(s1) + 1][strlen(s2) + 1];
 
    // Initialize the table
    for (int i = 0; i <= strlen(s1); i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= strlen(s2); j++) {
        dp[0][j] = j;
    }
 
    // Populate the table using dynamic programming
    for (int i = 1; i <= strlen(s1); i++) {
        for (int j = 1; j <= strlen(s2); j++) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + fmin(dp[i-1][j], /*Deletion*/
                               fmin(dp[i][j-1], /*Insertion*/
                                   dp[i-1][j-1])); /*Substitution*/
            };
            if (0 < i && i < strlen(s1) && 0 < j && j < strlen(s2) &&
                s1[i] == s2[j - 1] && s1[i - 1] == s2[j])
              dp[i][j] = fmin(dp[i][j], dp[i - 2][j - 2] + 1); 
            /*Transposition*/
        }
    }
 
    // Return the edit distance
    return dp[strlen(s1)][strlen(s2)];
}
