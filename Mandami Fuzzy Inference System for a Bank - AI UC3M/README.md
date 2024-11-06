# Fuzzy Logic Inference System for Loan Risk Assessment

**Course:** 2023/2024  
**Authors:**  
- Pablo Amor Molina - 100495855 ([10495855@alumnos.uc3m.es](mailto:10495855@alumnos.uc3m.es))
- Sergio Verde Llorente - 100495899 ([10495899@alumnos.uc3m.es](mailto:10495899@alumnos.uc3m.es))
- Hugo Cuevas Romera - 100495962 ([10495962@alumnos.uc3m.es](mailto:10495962@alumnos.uc3m.es))  

**Group:** 81  
**Degree:** Computer Engineering  
**Subject:** Aritificial Inteligence  

## Table of Contents
1. [System Overview](#system-overview)
2. [System Components](#system-components)
   - [Fuzzification](#fuzzification)
   - [Rule Evaluation](#rule-evaluation)
   - [Composition](#composition)
   - [Defuzzification](#defuzzification)
3. [How to Use](#how-to-use)
4. [Key Functions](#key-functions)
   - [procesapp](#procesapp)
   - [fuzzy](#fuzzy)
5. [Results](#results)
6. [Conclusions](#conclusions)

## System Overview

This project implements a Fuzzy Logic Inference System to assist banks in determining the risk level of loan applications. It is based on the Mamdani fuzzy inference model, designed to process factors such as employment, age, income, and other personal details. These inputs are used to assess whether a loan should be approved or denied based on the risk score calculated by the system.

## System Components

The system follows the Mamdani inference model and is divided into four steps:

### Fuzzification
In this step, input variables are transformed into fuzzy values (degrees of membership) using predefined membership functions. Variables such as age, income, and employment are mapped to fuzzy sets to facilitate decision-making.

### Rule Evaluation
In this phase, the fuzzy rules are applied. These rules determine the relationship between the input variables and the output (loan risk level). The system calculates the antecedents and consequents for each rule, applying the degree of membership to determine the rule's influence on the final output.

### Composition
Once the rules are evaluated, the system combines the results to form a fuzzy set for the output (loan risk). This fuzzy set represents the degree of risk for each application.

### Defuzzification
The final step converts the fuzzy output set into a crisp value using the centroid method. This value represents the risk level of the loan application and helps the bank make a decision.

## How to Use

1. **Initialize the system** by loading fuzzy sets, rules, and loan application data.
2. **Process loan applications**: For each application, the system performs fuzzification, rule evaluation, composition, and defuzzification to calculate the risk score.
3. **Output the results**: The risk scores are saved in a results file for review and decision-making.

## Key Functions

### procesapp
This function performs the main fuzzy inference process:
- Fuzzifies input variables.
- Evaluates fuzzy rules.
- Combines the rule results.
- Defuzzifies the final fuzzy set to produce the risk score.

### fuzzy
This auxiliary function handles the fuzzification process. It receives the loan application data and converts each input variable into fuzzy degrees of membership.

## Results

The system produces a risk score for each loan application, saved in a results file. These scores assist in making decisions on loan approval. The fuzzy logic approach allows for nuanced decision-making, accounting for multiple variables and uncertainty in the data.

## Conclusions

This system efficiently assesses the risk of loan applications using fuzzy logic. The use of fuzzy sets allows the system to handle uncertain and imprecise data, providing a flexible tool for financial decision-making. The implementation follows the Mamdani inference model, ensuring that the results are accurate and interpretable.

