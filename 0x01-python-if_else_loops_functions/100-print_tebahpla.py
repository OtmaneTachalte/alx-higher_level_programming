#!/usr/bin/python3

toggle_case = 0
for ascii_val in range(ord('z'), ord('a') - 1, -1):
    adjusted_ascii = ascii_val - toggle_case
    print(chr(adjusted_ascii), end='')
    toggle_case = 0 if toggle_case else 32  # Toggle between 0 and 32
