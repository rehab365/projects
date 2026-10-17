# import numpy as np

# a = [48,49,50,51,52]
# b = [10,30,50,70,90]
# print(np.mean(a))
# print(np.mean(b))
# print(round(np.std(a),2))
# print(round(np.std(b),2))conda

# data =[12,15,18,20,55]
# print(max(data)-min(data))
# print(np.ptp(data))



# clean=[12,15,18,20]
# print(max(clean)-min(clean))
import numpy as np
# from scipy import stats
data = [10, 12, 14, 15, 16, 18, 20, 95]
q1,q3 = np.percentile(data,[25,75])
print(q3-q1)
# print(stats.iqr(data))
import numpy as np

data = [2, 4, 5, 7, 8, 10, 12, 15, 100]

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = [x for x in data if x < lower or x > upper]
print(outliers)  # [100]




data = np.array([55, 70, 90, 65, 80, 75])
z = (data - data.mean()) / data.std()
print(z)