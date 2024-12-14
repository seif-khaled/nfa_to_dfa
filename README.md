# DFA-NFA Converter

This project defines a class `dfa_nfa`, which converts a Non-deterministic Finite Automaton (NFA) table into a Deterministic Finite Automaton (DFA) table.

## Features

### What the Code Does

#### 1. **Initialization**
- Initializes the NFA structure using `self.table` and sets up the alphabet in `self.alpha`.

#### 2. **NFA Generation**
- **`genreate_nfa`**: Interactively takes user input to create an NFA transition table.
  - Prompts for transitions for each state, including epsilon (ε) transitions.

#### 3. **Epsilon Closure**
- **`get_epslin_closrue`**: Computes the epsilon closure of a given state, which is crucial for converting an NFA into a DFA.

#### 4. **Conversion to DFA**
- **`convert_to_dfa`**: Implements the subset construction algorithm:
  - Tracks and aggregates new sets of states during the conversion process.
  - Builds the DFA transition table by combining NFA states based on epsilon closures and transitions.

#### 5. **Helper Methods**
- **`remove_all_instances`**: Cleans up state lists by removing specific items (like `-1`).
- **`show_nfa_repsenration_`**: Placeholder for visualizing the NFA graph using Graphviz (currently not implemented).

#### 6. **Output**
- Outputs the DFA transition table in a dictionary format.

---

### Input Requirements

#### 1. **Interactive NFA Generation**
- **Number of States**: Total states in the NFA.
- **Alphabet**: The set of symbols used in transitions (e.g., `a`, `b`).
- **Transitions for Each State**:
  - Transition for each alphabet symbol (target state or states).
  - Epsilon (ε) transitions (list of reachable states).

#### 2. **DFA Conversion**
- Requires the generated NFA table, the alphabet (`alpha`), and the number of alphabet symbols (`breakpoint`).

---

### Example Output
The program outputs the resulting DFA transition table in dictionary format after conversion.

---

## Future Enhancements
- Implement the **`show_nfa_repsenration_`** function to visualize the NFA graph using Graphviz.

