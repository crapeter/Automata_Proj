# CS 5383: Final Project

NFA Simulation using Breadth-First Search (BFS)

## Group Members

- Craig Peterson
- Ethan Norales De La Rosa

## Description

This project implements a Non-Deterministic Finite Automaton (NFA)
simulator in Python. The program reads an NFA definition and one or
more input strings from a text file or from user input, then determines whether each input string is accepted or rejected by the NFA.

The implementation uses a Breadth-First Search (BFS) approach to
explore all possible state transitions for each symbol in the
input string.

## Programming Language

Python 3

## Files

- runNFA.py → Main Python program containing all logic
- proj-1-machine.txt → Example input, user input not needed
- proj-1-machine-1.txt → Example input, user input required
- test.txt → Example input with larger alphabet, more states and more transitions, user input not needed
- README.txt → This documentation file

## Input Format

The input file must define the NFA as a 5-tuple:

    (alphabet, states, init_state, final_states, transitions)

followed by a separator line containing:

    ),

and then a list of input strings (Beta) in parentheses.

    (1101, 0001, 1110),

Example input file:

    (
      (
        (0, 1),
        (q0, q1, q2),
        q0,
        (q2),
        ((q0, 0, q0), (q0, 1, q0),(q0, 0, q1),(q1, 1, q2))
      ),
      (1101, 0001, 1110)
    )

In this example:

- Alphabet: {0, 1}
- States: {q0, q1, q2}
- Initial State: q0
- Final State(s): {q2}
- Transitions: (q0,0,q0), (q0,1,q0), (q0,0,q1), (q1,1,q2)
- Input strings: 1101, 0001, 1110

## Assumptions

1. The NFA is represented as a 5-tuple:
   (alphabet, states, init_state, final_states, transitions)
2. The input file can span multiple lines for readability.
3. A line containing only '),' separates the NFA from the Beta input.
4. The first two lines are always open parentheses and are not part of the NFA.
5. Multi-line parentheses are flattened into a single tuple during parsing.

## How to Compile and Run

Windows:

```text
1. Open Command Prompt.
2. Navigate to the directory containing runNFA.py and your input file:
   cd path\to\your\project
3. Run the program:
   python runNFA.py {one of the above input files}
```

Mac / Linux:

```text
1. Open Terminal.
2. Navigate to the project directory:
   cd /path/to/your/project
3. Run the program:
   python3 runNFA.py {one of the above input files}
```

## Program Behavior

- If Beta (the input strings) is empty:

  The program will prompt the user to manually enter strings:

  ```text
  Please input a string: 1101
  Accepted

  Please input another string:
  Bye Bye
  ```

  Entering an empty line will exit the program.

- If Beta contains predefined input strings, the program will automatically evaluate and print the results:

  ```text
  (accepted, accepted, rejected)
  ```

## Example Output

Given an example input file above (proj-1-machine), the output would be:

```text
(accepted, accepted, rejected)
```

## Dependencies

No external libraries required.
Uses only built-in Python libraries (sys).

## Notes

- To visualize each step of the NFA simulation, you can uncomment
  the print statements inside the NFA() function to display the
  current symbol and possible next states.
- Input parsing assumes correct formatting; malformed input may
  cause parsing errors.
