#!/usr/bin/env python3

frequency_single = "etaoinsrhldcumfpgwybvkxjqz"
frequency_double = "th he an in er on re ed nd ha at en es of nt ea ti to io le is ou ar as de rt ve"
frequency_triple = "the and tha ent ion tio for nde has nce tis oft men"

def main():
    single = {}
    double = {}
    triple = {}
    with open("cipher.txt", "r") as f:
        for line in f:
            line = line.replace(" ", "")
            line = line.strip("\n")
            length = len(line)
            for i in range(length):
                if i < length - 2:
                    if line[i:i+3] in triple:
                        triple[line[i:i+3]] += 1
                    else:
                        triple[line[i:i+3]] = 1
                if i < length - 1:
                    if line[i:i+2] in double:
                        double[line[i:i+2]] += 1
                    else:
                        double[line[i:i+2]] = 1
                if i < length:
                    if line[i] in single:
                        single[line[i]] += 1
                    else:
                        single[line[i]] = 1

    output_table(single, frequency_single, "single.txt")
    output_table(double, frequency_double.split(" "), "double.txt")
    output_table(triple, frequency_triple.split(" "), "triple.txt")

def output_table(table, comparison, file_name):
    with open(file_name, "a") as f:
        f.truncate(0)
        sorted_table = [value for value in sorted(table, key=table.__getitem__, reverse=True)]
        for index, item in enumerate(sorted_table):
            if index >= len(comparison):
                break
            f.write(item + " " + str(table[item]) + " = " + comparison[index] + "\n")

if __name__ == "__main__":
    main()
