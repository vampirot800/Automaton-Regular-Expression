# Ramiro Flores Villarreal
# A01710879
# 01 / 03 / 2024
# Implementation of Computational methods Project: Lexical Analysis E1
# Automaton 

class Automaton:
    def __init__(self):

        # Definition of states and transitions
        self.states = {'p0', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12'}
        self.input_symbols = {'C', 'A', 'E', 'L', 'R', 'M', 'T', 'N', 'B'}
        self.transitions = {
            'p0': {'C': 'q0'}, 
            'q0': {'A': 'q1', 'E': 'q6'},
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
        
        self.start_state = 'p0'
        self.current_state = 'p0'  # Initial state
        self.final_state = 'q12'


    # Functions 
    # Find the next state based on the current state and input symbol

    def move(self, input_symbol):
        if input_symbol in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][input_symbol]
        else:
            raise ValueError(f"No transition defined for state {self.current_state} with input {input_symbol}")

    # Resets to initial state, processes the initial symbol 'C' and then the rest 

    def process(self, input_sequence):
        self.current_state = self.start_state 

        for symbol in input_sequence:
            self.move(symbol)
        return self.current_state

# Automaton Instance
automaton = Automaton()

# Words to test
words = ['CALEN', 'CALMA', 'CARCA', 'CELEB', 'CERTAR']

# Test each word
for word in words:
    try:
        final_state = automaton.process(word)
        if final_state == automaton.final_state:
            print(f"The word '{word}' is accepted by the automaton.")
        else:
            print(f"The word '{word}' is not accepted by the automaton.")
    except ValueError as e:
        print(e)
