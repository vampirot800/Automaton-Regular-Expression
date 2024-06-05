# Ramiro Flores Villarreal
# A01710879
# 01 / 03 / 2024
# Implementation of Computational methods Project: Lexical Analysis E1
# Automaton / Regular Expression

class Automaton:
    def __init__(self):
        # Define states and transitions
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12'}
        self.input_symbols = {'C', 'A', 'E', 'L', 'R', 'M', 'T', 'N', 'B'}
        self.transitions = {
            'q0': {'C': 'q0', 'A': 'q1', 'E': 'q6'},
            'q1': {'L': 'q2', 'R': 'q5'},
            'q2': {'E': 'q3', 'M': 'q4'},
            'q3': {'N': 'q12'}, 
            'q4': {'A': 'q12'}, 
            'q5': {'C': 'q4'}, 
            'q6': {'L': 'q7', 'R': 'q9'}, 
            'q7': {'E': 'q8'},            
            'q8': {'B': 'q12'}, 
            'q9': {'T': 'q10'}, 
            'q10': {'A': 'q11'}, 
            'q11': {'R': 'q12'}, 
            'q12': {}, 
        }
        self.start_state = 'q0'
        self.current_state = 'q0'  # Initial state 'q0'
        self.final_state = 'q12'
        self.initial_symbol = 'C'  # Initial symbol to start the automaton

    def move(self, input_symbol):
        # Find the next state based on the current state and input symbol
        if input_symbol in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][input_symbol]
        else:
            raise ValueError(f"No transition defined for state {self.current_state} with input {input_symbol}")

    def process(self, input_sequence):
        # Process the initial symbol 'C' first
        self.current_state = self.start_state  # Reset to initial state
        self.move(self.initial_symbol)  # Process the initial symbol

        # Process the rest of the input sequence
        for symbol in input_sequence:
            self.move(symbol)
        return self.current_state

# Create an instance of the Automaton
automaton = Automaton()

# Test the automaton with an example input sequence
input_sequence = ['C','A', 'L', 'E', 'N']
final_state = automaton.process(input_sequence)
print(f"Final state: {final_state}")  # Expected Output: q12

# Test the automaton with an example input sequence
input_sequence = ['C','A', 'L', 'M', 'A']
final_state = automaton.process(input_sequence)
print(f"Final state: {final_state}")  # Expected Output: q12

# Test the automaton with an example input sequence
input_sequence = ['C','A', 'R', 'C', 'A']
final_state = automaton.process(input_sequence)
print(f"Final state: {final_state}")  # Expected Output: q12

# Test the automaton with an example input sequence
input_sequence = ['C','E', 'L', 'E', 'B']
final_state = automaton.process(input_sequence)
print(f"Final state: {final_state}")  # Expected Output: q12

# Test with another input sequence
input_sequence = ['C','E', 'R', 'T', 'A', 'R']
final_state = automaton.process(input_sequence)
print(f"Final state: {final_state}")  # Expected Output: q12

# Test with an invalid input sequence
try:
    input_sequence = ['A', 'R', 'X']
    final_state = automaton.process(input_sequence)
    print(f"Final state: {final_state}")
except ValueError as e:
    print(e)  # Expected to raise an error for invalid input
