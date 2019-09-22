# coding=utf-8


def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    merged_intervals = []

    for interval in sorted_intervals:
        # merged_intervals이 있고
        # 현재 인터벌 첫 번째 값이 마지막 머지된 두 번째 값보다 작거나 같으면
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            # 마지막 머지된 값을 변경
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            merged_intervals.append(interval)

    return merged_intervals
