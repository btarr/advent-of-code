# Day 1

# Part 1
def get2020SumOfTwo(report):
    for i in range(0, len(report)):
        for j in range(0, len(report)):
            if i == j:
                continue
            if report[i] + report[j] == 2020:
                return report[i] * report[j]


# Part 2
def get2020SumOfThree(report):
    for i in range(0, len(report)):
        for j in range(0, len(report)):
            for k in range(0, len(report)):
                if i == j or j == k or i == k:
                    continue
                if report[i] + report[j] + report[k] == 2020:
                    return report[i] * report[j] * report[k]


def readReportFromFile(path):
    report = []
    for line in open(path):
        report.append(int(line.strip()))
    return report


def main():
    expense_report = readReportFromFile('./input/day_1_part_1.txt')
    return get2020SumOfThree(expense_report)


print(main())
