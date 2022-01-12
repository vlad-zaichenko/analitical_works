import pandas as pd

#make df
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

#sort df
group_vals = df.sort_values(['grps','vals'], ascending = [True, False])


unique_grps = list(group_vals['grps'].unique())
sum_dict_values = {}

#sum firs 3 values of sorted group
for i in unique_grps:
    a = pd.Series(group_vals[group_vals.grps == i][:3].agg({'vals':'sum'}))
    sum_dict_values[i] = a[0]
    
print(sum_dict_values)