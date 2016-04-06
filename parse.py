import pandas as pd
from itertools import combinations

df = pd.read_csv('responses.csv')
timestamp_dict = {}
all_timestamps = []

for index, series in df.iterrows():
    times = series[1].split(", ")
    for time in times:
        if time not in timestamp_dict:
            timestamp_dict[time] = []
        timestamp_dict[time].append(index)

combs = combinations(timestamp_dict, 2)
availability_dict = {}
for c in combs:
    print c
    print timestamp_dict[c[0]]
    availability_dict[c] = tuple(set(timestamp_dict[c[0]]) & set(
                                 timestamp_dict[c[1]]))

# print availability_dict

def get_time_score(dudes):
    res = sum(get_person_weight(i) for i in dudes)
    return res

def get_person_weight(i):
    sureness = df.loc[i][2]
    return (sureness + 1) / 2.0

best_times = sorted(availability_dict.items(), key=lambda x: get_time_score(
                    x[1]), reverse=True)

for time, dudes in best_times[0:20]:
    print time, dudes, get_time_score(dudes)
