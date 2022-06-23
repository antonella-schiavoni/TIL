# Read a pandas dataframe stored as pickle

# How To Use
import joblib
import pandas as pd

SRC_PATH = None
DST_PATH = None

df = joblib.load(SRC_PATH)
df.to_csv(DST_PATH, index=False)
