# Fuzzy Logic Inference System for Loan Risk Assessment
Course: 2023/2024
Authors:

PABLO AMOR MOLINA - (10495855@alumnos.uc3m.es)
SERGIO VERDE LLORENTE - (100495899@alumnos.uc3m.es)
HUGO CUEVAS ROMERA - (100495962@alumnos.uc3m.es)

Degree: Computer Engineering
Subject: Computer Architecture

## Overview

This project implements a Fuzzy Logic Inference System based on the Mamdani model to assist banks in making decisions regarding personal loan approvals. The system evaluates various factors such as employment, age, income, and others to calculate the risk level associated with each loan application.

The system uses fuzzy sets and rules to process loan applications and provide a risk score, helping banks decide whether to approve or reject a loan request.

## System Components

The system follows the Mamdani inference model, which consists of the following steps:

1. **Fuzzification**: Convert input variables into fuzzy degrees.
2. **Rule Evaluation**: Apply fuzzy rules to assess the input variables.
3. **Composition**: Combine the results of the evaluated rules.
4. **Defuzzification**: Convert the fuzzy output into a single numeric risk value.

These steps are repeated for each loan application to compute the corresponding risk level.

## Fuzzification

The input values (age, income, etc.) are converted into degrees of membership using predefined fuzzy sets. This process is based on fuzzy membership functions defined in the system configuration.

## Rule Evaluation

Fuzzy rules, stored in the system, evaluate the loan application's characteristics. The system calculates the antecedent and applies the result to the consequent membership function, adjusting the risk level accordingly.

## Composition

The resulting membership functions from the rules are combined into a fuzzy set for the output variable (risk level).

## Defuzzification

The final fuzzy set is defuzzified using the centroid method to generate a single numeric value representing the risk level of the loan application.

## How to Use

1. Initialize the system by loading all the necessary data, including fuzzy sets, rules, and loan applications.
2. The system processes each loan application in a loop, calling the `procesapp` function to compute the risk score.
3. The risk score is stored in an output file for further analysis or decision-making.

## Key Functions

- **`procesapp`**: This function handles the main fuzzy inference process, including fuzzification, rule evaluation, composition, and defuzzification.
- **`fuzzy`**: This auxiliary function performs fuzzification for a given loan application.

## Results

The risk score for each loan application is saved in a result file, allowing bank staff to review and make decisions based on the computed risk levels.

## Notes

- The code is fully delivered, except for a known issue in the function `readFuzzySetsFile` within the file `MFIS_Read_Functions.py`, where the list was initialized with fewer values than required, leading to out-of-range errors.

## Conclusion

This system provides an efficient and automated way to assess loan risks, streamlining the decision-making process for banks. It can handle multiple loan applications per day and generates precise risk scores based on well-defined fuzzy logic rules.
