import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
from numpy.random import randn
np.random.seed(42)
comp1 = np.random.randn(200)  # N(0, 1)
comp2 = 10 + 2* np.random.randn(200)  # N(10, 2)
values = Series(np.concatenate([comp1, comp2])) #concat(1,2) -1번째 문자열에 두번째 문자열을 합치는 함수와 동일
values.hist(bins=100, alpha=0.3, color='k', density=True)
values.plot(kind='kde', style='k--')