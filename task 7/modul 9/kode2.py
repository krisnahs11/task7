import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sb 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import LogisticRegression
import math
import warnings
warnings.filterwarnings('ignore')

data = 'CarPrice_Assignment.csv'
dataset = pd.read_csv(data)
dataset.isna().sum()