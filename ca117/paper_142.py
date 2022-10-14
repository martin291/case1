#!/usr/bin/env python3
import sys

for line in sys.stdin:
    rps = line.strip().split()
    if rps[0] == "rock":
        if rps[1] == "scissors":
            print("Player 1 wins")
        elif rps[1] == "paper":
            print("Player 2 wins")
        elif rps[1] == "rock":
            print("Draw")
    elif rps[0] == "paper":
        if rps[1] == "scissors":
            print("Player 2 wins")
        elif rps[1] == "paper":
            print("Draw")
        elif rps[1] == "rock":
            print("Player 1 wins")
    elif rps[0] == "scissors":
        if rps[1] == "scissors":
            print("Draw")
        elif rps[1] == "paper":
            print("Player 1 wins")
        elif rps[1] == "rock":
            print("Player 2 wins")
