# Day 1

def get2020(report):
    for i in range(0, len(report)):
        for j in range(0, len(report)):
            if i == j:
                continue
            if report[i] + report[j] == 2020:
                return report[i] * report[j]


def readReportFromFile(path):
    report = []
    for line in open(path):
        report.append(int(line.strip()))
    return report


def main():
    expense_report = readReportFromFile('./input/day_1_part_1.txt')
    return get2020(expense_report)


print(main())
