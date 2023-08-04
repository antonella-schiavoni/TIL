"""
Probability of disease

A test indicating the presence of disease in cats is 95% accurate in terms of both sensitivity and specificity.
The prevalence of the disease is 3% which means only 3% of known cats have the disease. If your cat tests possitive (negative) for the disease, what's the probability that your cat has (doesn't have) the disease?

Write a program which takes in the accuracy of a test as well as the percent of a population which has the disease and returns a list containing:
- Fistly, the probability that an individual has the disease given a positive test result.
- Secondly, the probability that an individual does not have the disease given a negative test result.

Note that
- You can assume the sensitivity and specificity are equal to the accuracy.
- You should't use any libraries.
- Your output values will automatically be rounded to the fourth decimal.
"""

def probability_of_disease(accuracy, prevalence):
    P_diseased = prevalence
    P_not_diseased = 1 - P_diseased

    TPR = accuracy
    TNR = accuracy
    FPR = 1 - TNR

    # Applying bayes theorem
    p_disease_given_possitive = (TPR * P_diseased) / ((TPR * P_diseased) + (FPR * P_not_diseased))
    p_no_disease_given_possitive = (TPR * P_not_diseased) / ((TPR * P_not_diseased) + (FPR * P_diseased))
    
    return [p_disease_given_possitive *100, p_no_disease_given_possitive*100]
