import pandas as pd

_root = "c://Research//voice//"
_file = _root + "20230227_D1.csv"

df = pd.read_csv(_file)
df_ret = df.iloc[:, :257]

df_ret.to_csv(_root+"20230227_D1_new.csv", index=None)

file = open("", "")
