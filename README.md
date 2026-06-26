# Project_1_7_dnagy6
**[YOUTUBE LINK](https://youtu.be/ZtpWeXyEXUM)**

# Hybrid Training & Pace Calculator

## Project Overview
As an Exercise Physiologist and a fitness coach, I built the Hybrid Training & Pace Calculator to solve a practical problem: bouncing between different apps to program a training week. Programming for hybrid athletes requires managing heavy lifting and endurance running simultaneously. This terminal-based Python app brings barbell percentage math and running pace splits into one cohesive tool. 

## Course Competency Mapping
This project serves as a practical application of Python Crash Course textbook (Chapters 1–7). The required fundamentals used are below:

* **User Interaction:** The app uses the `input()` function to pause and accept user data (strings for lift names, floats for weights and times).
* **Iteration:** A core `while` loop keeps the main menu active so users can run multiple calculations without restarting. `for` loops are used to instantly generate full 4-week training blocks and list estimated race finish times.
* **Control Flow:** `if`, `elif`, and `else` blocks handle the main menu routing. I also implemented `try` and `except ValueError` blocks to catch invalid inputs and prevent the program from crashing.
* **Collections:** 
  * *Dictionaries:* Used to map out standard working percentages and to actively log a user's session PRs.
  * *Lists & Tuples:* Used to structure immutable race distances (5K, 10K, etc.) and specific rep ranges for the training blocks.
* **Variables & Math:** Handles string formatting (`.title()`) for clean output, and uses Python's mathematical operators (`//`, `%`) to convert raw decimal times into standard `MM:SS` runner splits.

## Core Features
1. **Lifting Calculator:** Takes a 1-Rep Max and automatically generates a 4-week linearly periodized strength block (including a deload week), complete with target weights and rep ranges.
2. **Pace Calculator:** Converts distance and total time into standard runner's splits and estimates finish times for common race lengths.
3. **Session PR Tracker:** Actively remembers and logs the heaviest weights entered for specific lifts during the current session so you don't lose your numbers.

## How to Run
1. Ensure Python 3 is installed on your machine.
2. Clone this repository.
3. Run `python hybrid_calculator.py` (or `python3 hybrid_calculator.py` on macOS/Linux) in your terminal.

---
**Author:** Dakota Nagy
**Date:** June 28, 2026
