import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

month_year_input = str(input())
month_year = month_year_input + '.csv'

xl = pd.read_csv(month_year)
xl_Category = list(xl['Категория'])
xl_summ = list(xl['Сумма в рублях'])

sns.barplot(x = xl_Category, y= xl_summ, estimator = sum).set(title = month_year)
plt.ylabel('траты в руб.')
plt.show()