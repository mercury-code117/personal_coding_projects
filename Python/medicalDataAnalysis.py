# Data for this project was supplied by:
# https://www.kaggle.com/datasets/prasad22/healthcare-dataset

import pandas as pd
import numpy as np
import scipy as stats
import matplotlib.pyplot as plt

df = pd.read_csv("Python/healthcare_dataset.csv")

print(df.head())

df.boxplot(by='Medical Condition', column=["Age"], grid=False)
plt.show()

# All of the boxplots shown are equally distributed, with very little or slight variance between the medical conditions.