#!/usr/bin/env python3

def main():
    table = [0 for i in range(26)]
    with open("cipher.txt", "r") as f:
        for line in f:
            line = line.replace(" ", "")
            line = line.strip("\n")
            for letter in line:
                letter = letter.upper()
                table[ord(letter) - ord("A")] += 1

    output_table(table)

def output_table(table):
    with open("plain.txt", "a") as f:
        f.truncate(0)
        for index, item in enumerate(table):
            if item == 0:
                continue
            f.write(chr(ord("A") + index) + " " + str(item) + "\n")

if __name__ == "__main__":
    main()
