#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Marcus Chiriboga'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    dot, dash, pause = ".", "-", " "
    """ This code seperates the bits into 2 opposite list. The
    smallest item in each is used to calculate the "opperators speed"
     """
    bits_list = bits.strip("0").split("0")
    bits_split_by_1_instead = bits.strip("0").split("1")
    time_unit = 0
    for item in bits_split_by_1_instead+bits_list:
        if not time_unit and not item == "":
            time_unit = len(item)  # finding the smallest amount of 0's or 1's
        elif len(item) < time_unit and not item == "":
            time_unit = len(item)

    """ With the time_unit we can set up replacement variables and swap them out
       """
    large_key = "1" * time_unit * 3
    small_key = "1" * time_unit
    answer = bits.replace(large_key, dash).replace(small_key, dot)
    answer = answer.replace("0" * 7 * time_unit, pause*3)
    answer = answer.replace("0" * 3 * time_unit, pause)
    answer = answer.replace("0", "").strip()
    print("final: " + answer)
    return answer


def decode_morse(morse):
    # your code here
    morse_sequence = str(morse)
    answer = []
    morse_sequence.strip()
    list_of_characters = morse_sequence.split(" ")
    for char in list_of_characters:
        if char == "":
            answer.append(" ")
        else:
            answer.append(MORSE_2_ASCII[char])
    bits_list = "".join(answer)
    bits_list = " ".join(bits_list.split())
    return bits_list


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa
    small_bits = "10001"
    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(small_bits))}")
    print("\nCompleted.")
