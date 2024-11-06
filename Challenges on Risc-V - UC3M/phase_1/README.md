# Practice 1: Introduction to Assembly Language

**Course:** 2023/2024  
**Authors:**  
- Pablo Amor Molina - 100495855 ([10495855@alumnos.uc3m.es](mailto:10495855@alumnos.uc3m.es))
- Manuel Roldán Matea - 100500450 ([100500450@alumnos.uc3m.es](mailto:100500450@alumnos.uc3m.es))  

**Group:** 81  
**Degree:** Computer Engineering  
**Subject:** Computer Architecture  

## Table of Contents
1. [Exercise 1](#exercise-1)
   - [Sine and Cosine Functions](#sine-and-cosine-functions)
   - [Tangent Function](#tangent-function)
   - [Number E](#number-e)
2. [Exercise 2](#exercise-2)
   - [SinMatrix Function](#sinmatrix-function)
3. [Testing Battery](#testing-battery)
4. [Conclusions and Estimated Time](#conclusions-and-estimated-time)

## Exercise 1

### Sine and Cosine Functions
Developing the sine and cosine subroutines was the most labor-intensive part of the practice, as it required auxiliary subroutines:
1. **Simplifier**: Reduces any input number to a range of (-π/2, π/2) for sine and (-π, π) for cosine, avoiding overflow.
2. **Factorial**: Calculates the factorial of a number, used frequently within other functions.
3. **Exponent**: Calculates a base raised to a given exponent.

The sine function primarily uses registers `s` for stability, while terminal subroutines (like factorial) use `t` registers. Each subroutine is designed for reuse to minimize repetitive code.

#### Simplifier
This subroutine reduces a number based on its sign to stay within functional ranges. While not strictly necessary after discovering bounded ranges would suffice, it’s retained for completeness and supports operations with any input value.

#### Factorial
Calculates the factorial by iterating from 1 to the input number. This routine operates on integers only, as it’s used in iterative summations.

#### Exponent
Returns a base number raised to a specified exponent, iterating and multiplying the base with each loop to reach the target exponent.

### Tangent Function
The tangent function is simplified by using previously developed sine and cosine functions:
1. Stores the original value.
2. Calls `sin` and `cos` functions.
3. Checks if the cosine result is near zero to return infinity if so.
4. Returns the result of dividing sine by cosine.

### Number E
The calculation of `e` uses a simpler Taylor series expansion, utilizing the factorial subroutine for its denominator in each iteration. We used 7 iterations for optimal precision within the given requirements.

## Exercise 2

### SinMatrix Function
This function uses the previously created `sin` function to calculate the sine of each element in a matrix. The function iterates over the matrix using two loops for rows and columns, addressing memory locations appropriately.

Key steps:
1. Loads values from the first matrix using `lw`.
2. Calls the sine function.
3. Stores results in the second matrix with `sw`.
4. Increments memory addresses to ensure matched positions between matrices.

## Testing Battery

### Exercise 1
| Input    | Expected Results                  | Obtained Results                  |
|----------|-----------------------------------|-----------------------------------|
| 0        | sin: 0.0, cos: 1.0, tan: 0.0      | sin: 0.0, cos: 1.0, tan: 0.0      |
| π/2      | sin: 1.0, cos: 0.0, tan: ∞        | sin: 0.99994, cos: 0.00001, tan: ∞ |
| 1        | sin: 0.841, cos: 0.540, tan: 1.557| sin: 0.841, cos: 0.540, tan: 1.557|
| -1       | sin: -0.841, cos: 0.540, tan: -1.557 | sin: -0.841, cos: 0.540, tan: -1.557|
| 2.5      | sin: 0.598, cos: -0.801, tan: -0.747 | sin: 0.598, cos: -0.801, tan: -0.747 |
| -2.5     | sin: -0.598, cos: -0.801, tan: 0.747 | sin: -0.598, cos: -0.801, tan: 0.747 |
| 5        | sin: -0.958, cos: 0.283, tan: -3.380 | sin: -0.958, cos: 0.283, tan: -3.380 |
| -5       | sin: 0.958, cos: 0.283, tan: 3.380 | sin: 0.958, cos: 0.283, tan: 3.380 |

### Exercise 2
Results matched expected values, confirming function integrity.

## Conclusions and Estimated Time

This practice served as an excellent introduction to assembly language, particularly with RISC-V. Key challenges included:
- Managing floating-point numbers, where initial unfamiliarity slowed progress.
- Addressing overflow led to the development of the `simplifier` function for range limitations.
- Initial confusion regarding submission format, which created delays but was resolved through clarification.

We gained a solid understanding of RISC-V instruction sets and conventions, which will be valuable in future projects.

### Estimated Time Breakdown
| Task                       | Time Spent        |
|----------------------------|-------------------|
| Pseudocode                 | 2 hours 30 minutes|
| Sin and Cos Functions      | 2 hours           |
| Number E                   | 1 hour            |
| Exponent and Factorial     | 1 hour 30 minutes |
| Simplifier Subroutine      | 3 hours           |
| SinMatrix Function         | 1 hour 30 minutes |
| **Total**                  | **11 hours 30 minutes** |
