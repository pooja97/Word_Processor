# Flyweight pattern for Word processor in python3

created a Character class that stores only the unicode code point of the character. 
A Flyweight factory that given a unicode code point returns the Flyweight character object for the character. 
A single point of access to the same Flyweight factory from anywhere in the program. (Singleton pattern)

Created a Flyweight factory for fonts. In this factory the input is a triple: the font name (Times, Courier, etc), point size (12, 13, etc) and style (bold, italic, underline,
etc). This factory also has a single point of access. (Singleton)

For the Character Flyweight to work we need to a way to story the extrinsic state of the character objects, that is the font information. 
For this we will use a RunArray. A RunArray keeps track of runs in a sequence. 
