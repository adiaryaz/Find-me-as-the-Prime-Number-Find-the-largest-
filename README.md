# Find me as the Prime Number (Find the largest)

A program to find the largest prime number from a series of user inputs.

## 📝 Description

This program repeatedly asks the user if they want to enter a number. If the user agrees (by entering 'y'), they provide an integer. The program must check if this integer is a prime number. When the user decides to stop (by entering 'n'), the program identifies and displays the single largest prime number from all the valid numbers that were entered.

-----

## 🎯 Problem Statement

### Input:

  * A sequence of 'y' (yes) or 'n' (no) prompts to control the loop.
  * An integer input from the user following each 'y' prompt.

### Output:

  * The largest prime number found among all inputs.
  * "NotFound" if no prime numbers are entered.
  * "NoProceed" if an invalid input (like a negative number) is entered.

### Rules:

1.  The program runs in a loop, asking for input. 'y' continues the loop, 'n' stops it.
2.  A **prime number** is a natural number **greater than 1** (e.g., 2, 3, 5, 7...).
3.  The program must keep track of the largest prime number it has seen so far.
4.  If **no prime numbers** are found (or no numbers are entered), the result must be **"NotFound"**.
5.  Non-prime positive numbers (like 1, 4, 8, 10) are ignored.
6.  Entering a **negative number** is invalid and should output **"NoProceed"**.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
y
2
y
10
n
```

**Output:**

```
2
```

**Explanation:** `2` is a prime number. `10` is not prime and is ignored. The largest prime found is **2**.

### Example 2 (Sample 2)

**Input:**

```
y
2
y
3
y
5
n
```

**Output:**

```
5
```

**Explanation:** `2`, `3`, and `5` are all prime numbers. The largest among them is **5**.

### Example 3 (Sample 3)

**Input:**

```
y
4
y
8
n
```

**Output:**

```
NotFound
```

**Explanation:** Neither `4` nor `8` is a prime number. No primes were found.

### Example 4 (Sample 4)

**Input:**

```
n
```

**Output:**

```
NotFound
```

**Explanation:** No numbers were entered, so no primes were found.

### Example 5 (Sample 5)

**Input:**

```
y
3
y
-5
```

**Output:**

```
NoProceed
```

**Explanation:** The input `-5` is a negative number, which is not a valid input.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/find-largest-prime.git
    cd find-largest-prime
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Follow the 'y/n' prompts to enter numbers and see the result.
