#!/usr/bin/env python3

def main():
    table = {}
    with open("cipher.txt", "r") as f:
        for line in f:
            line = line.replace(" ", "")
            line = line.strip("\n")
            for letter in line:
                if letter in table:
                    table[letter] += 1
                else:
                    table[letter] = 1

    output_table(table)

def output_table(table):
    print(table)
    with open("plain.txt", "a") as f:
        f.truncate(0)
        sorted_table = [value for value in sorted(table, key=table.__getitem__, reverse=True)]
        for item in sorted_table:
            f.write(item + " " + str(table[item]) + "\n")

if __name__ == "__main__":
    main()
