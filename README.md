# Automaton-Regular-Expression

## Description
The language I chose to model is Elven.

The words included in my lexical analysis are as follows:

Calen: Sindarin word for 'green'
Calma: Quenya word for 'Lamp'
Carca: Quenya word for 'fang'
Celeb: Quenya word for 'silver'
Certar: Quenya word for 'Runes', referring in particular to the "Alphabet of Daeron".

The modeling technique I decided to use was a Deterministic Finite Automaton (DFA) to represent my solutions since they provide a precise and deterministic approach to lexeme parsing, which is suitable for the context of lexical analysis.

## Model of the Solution

I modeled my automaton to cover the 5 words from the elvish language provided

![DFA](Automaton.jpeg)
 
There are 13 states, initial state being q0 and ending state being q12
The symbols in between transitions are: 'C', 'A', 'E', 'L', 'R', 'M', 'T', 'N', 'B'

This model succesfully covers the 5 words from the elven alfabet.

The presented automaton is equivalent to the following regular expression:

DFA -> RE:
C(ALEN|ALMA|ARCA|ELEB|ERTAR)

## Implementation

For my implementation of a lexical analysis, I followed the regular expression in the regex_test.py file.
The file tests 8 strings and the program should return "''Matches the pattern" if the string is accepted or "''does not match the pattern" if the string is not part of the language.

the strings tested can be modified to prove that no other string would be accepted other than the 5 words.

## Tests

The tests can be seen in the end of both files, i used 6 tests in the automaton, 1 for each word parsed succesfully and an extra one to prove the automaton works and no words other than the ones in the language can be generated.

in the regex_test.py file, i test the following 8 strings:
    'CALEN',  # Should match
    'CALMA',  # Should match
    'CARCA',  # Should match
    'CELEB',  # Should match
    'CERTAR', # Should match
    'CALEB',  # Should not match (incomplete)
    'CERTAB', # Should not match (invalid)
    'CAL',    # Should not match (invalid)

## Analysis

The **complexity** of my model is in general n, where n  is the length of the string to be processed. 

I used the regex library from Python to better parse.
My time complexity = O(n) 

Initially, I attempted to implement the automaton using Prolog. However, as I delved deeper into Prolog, I found it to be quite confusing, which led me to explore alternative approaches.

I decided to follow the recommendation of implementing the automaton in Python. This approach proved to be much more straightforward and intuitive for me. I was able to swiftly translate my automaton into a functional implementation.

In Python, I developed a class-based implementation of the automaton. This implementation defines states, input symbols, transitions, and methods to move through the automaton and process input sequences. By structuring the code into a class, I achieved better organization and modularity, facilitating easier maintenance and extension of the solution.

Additionally, I translated the automaton into a regular expression for lexical analysis. This regular expression succesfuly captures the patterns recognized by the automaton, allowing for efficient and concise parsing of input strings


## References

- how to program an automaton python - Google Search. (n.d.). https://www.google.com/search?sca_esv=abb5a476f07ba204&q=how+to+program+an+automaton+python&tbm=vid&source=lnms&prmd=visbnmtz&sa=X&ved=2ahUKEwihvtXSx8WGAxU4I0QIHbCOECcQ0pQJegQIChAB&biw=1443&bih=742&dpr=2#fpstate=ive&vld=cid:841b4817,vid:rsxjCkvYoAw,st:0v