# Day 1

expense_report = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def get2020(report):
    for i in range(0, len(report)):
        for j in range(0, len(report)):
            if i == j:
                continue
            if report[i] + report[j] == 2020:
                return report[i] * report[j]


def main():
    return get2020(expense_report)


print(main())
