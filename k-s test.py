import pandas as pd
f1=r'C:\Users\tjsdx\Documents\as18-1.xlsx'
df1=pd.DataFrame(pd.read_excel(f1))
f1=r'C:\Users\tjsdx\Documents\as18-2.xlsx'
df2=pd.DataFrame(pd.read_excel(f1))
f1=r'C:\Users\tjsdx\Documents\as18-4.xlsx'
df4=pd.DataFrame(pd.read_excel(f1))
f1=r'C:\Users\tjsdx\Documents\as18-5.xlsx'
df5=pd.DataFrame(pd.read_excel(f1))
f1=r'C:\Users\tjsdx\Documents\as18-6.xlsx'
df6=pd.DataFrame(pd.read_excel(f1))
from scipy.stats import ks_2samp
r12=ks_2samp(df1['Best Ages'],df2['Best Ages'])
print(r12)
r14=ks_2samp(df1['Best Ages'],df4['Best Ages'])
print(r14)
r15=ks_2samp(df1['Best Ages'],df5['Best Ages'])
print(r15)
r16=ks_2samp(df1['Best Ages'],df6['Best Ages'])
print(r16)
r24=ks_2samp(df2['Best Ages'],df4['Best Ages'])
print(r24)
r25=ks_2samp(df2['Best Ages'],df5['Best Ages'])
print(r25)
r26=ks_2samp(df2['Best Ages'],df6['Best Ages'])
print(r26)
r45=ks_2samp(df4['Best Ages'],df5['Best Ages'])
print(r45)
r46=ks_2samp(df4['Best Ages'],df6['Best Ages'])
print(r46)
r56=ks_2samp(df5['Best Ages'],df6['Best Ages'])
print(r56)
