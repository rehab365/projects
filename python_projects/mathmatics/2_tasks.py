def z_score(x,mean,std):
    return (x - mean) / std
z = z_score(45,60,10)
print(z)
# Explain in your own words what a z-score of -2.5 means, without using the word "standard deviation" in your explanation
# A z-score of -2.5 indicates that the value is 
# 2.5 units below the average of the dataset.
# This means that the value is significantly
# lower than most of the other values in the dataset, 
# suggesting it is an outlier or less common
# compared to the majority of the data points.
import numpy as np

hours = [1, 2, 3, 4, 5]
score = [50, 55, 65, 70, 85]

r = np.corrcoef(hours, score)[0, 1]
print(r)  # ≈ 0.98 (طردي قوي جدًا)