#!/usr/bin/python3

import inspect
import os
import subprocess
import time
import plac

class N:
    def __init__(self, character="?", dot=None, dash=None):
        self.character = character
        self.dot = dot
        self.dash = dash
    
    def decode(self, parsed_character):
        try:
            if len(parsed_character) == 0:
                return self.character
            elif parsed_character[0] == ".":
                return self.dot.decode(parsed_character[1:])
            elif parsed_character[0] == "-":
                return self.dash.decode(parsed_character[1:])
        except AttributeError:
            return "?"

MORSE_GRAPH = N(
    dot=N(
        "e",
        dot=N(
            "i",
            dot=N(
                "s",
                dot=N(
                    "h",
                    dot=N("5"),
                    dash=N("4"),
                ),
                dash=N(
                    "v",
                    dash=N("3"),
                )
            ),
            dash=N(
                "u",
                dot=N("f"),
                dash=N(
                    dash=N("2"),
                )
            ),
        ),
        dash=N(
            "a",
            dot=N(
                "r",
                dot=N("l"),
                dash=N(
                    dot=N("+"),
                )
            ),
            dash=N(
                "w",
                dot=N("p"),
                dash=N(
                    "j",
                    dash=N("1"),
                )
            ),
        ),
    ),
    dash=N(
        "t",
        dot=N(
            "n",
            dot=N(
                "d",
                dot=N(
                    "b",
                    dot=N("6"),
                    dash=N("="),
                ),
                dash=N(
                    "x",
                    dot=N("/"),
                ),
            ),
            dash=N(
                "k",
                dot=N("c"),
                dash=N("y"),
            ),
        ),
        dash=N(
            "m",
            dot=N(
                "g",
                dot=N(
                    "z",
                    dot=N("7"),
                ),
                dash=N("q"),
            ),
            dash=N(
                "o",
                dot=N(
                    dot=N("8"),
                ),
                dash=N(
                    dot=N("9"),
                    dash=N("0"),
                ),
            ),
        ),
    ),
)

def morsedekoder(morse: str, format="iås"):
    formats = {
        "prikkstrek": (".", "-", " ", "/"),
        "iås": ("I", "Ås", " ", "/"),
    }
    dot, dash, new_character, space = formats[format]
    message_decoded = []
    for word in morse.split(space):
        word_decoded = []
        for character in word.split(new_character):
            if character == "":
                continue
            parsed = []
            while len(character) > 0:
                if character.startswith(dot):
                    parsed.append(".")
                    character = character[len(dot):]
                elif character.startswith(dash):
                    parsed.append("-")
                    character = character[len(dash):]
                else:
                    character = character[1:]
            decoded = MORSE_GRAPH.decode(parsed)
            word_decoded.append(decoded)
        message_decoded.append("".join(word_decoded))
    return " ".join(message_decoded)
    

if __name__ == "__main__":
    print(plac.call(morsedekoder))
