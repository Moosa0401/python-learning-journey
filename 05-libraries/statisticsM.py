"""
https://docs.python.org/3/library/statistics.html#module-statistics
"""
import statistics

def main():
    grade = [100,100,80,75, 83, 35]
    avg = statistics.mean(grade)
    print(avg)

main()