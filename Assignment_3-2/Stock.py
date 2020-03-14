import pandas as pd

df_1 = pd.read_csv(r'D:\Study\Pandas\Data\fundamentals.csv')

#1. 从fundemantals.csv开始！

# S&P500股票在2015年net income的均值是多少？
print(df_1[df_1['For Year'] == 2015]['Net Income'].mean())

# 最大值比最小值多多少？
print(df_1[df_1['For Year'] == 2015]['Net Income'].max() - df_1[df_1['For Year'] == 2015]['Net Income'].min())

# S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值是多少？
print((df_1[df_1['For Year'] == 2016]['Fixed Assets']/df_1[df_1['For Year'] == 2016]['Total Assets']).mean())

# 固定资产占总资产比例最小的股票是的代码（ticker symbol）是什么？
print(df_1['Ticker Symbol'].loc[(df_1[df_1['For Year'] == 2016]['Fixed Assets']/df_1[df_1['For Year'] == 2016]['Total Assets']).sort_values().head(1).index])

#2. 加入securities.csv

df_2 = pd.read_csv(r'D:\Study\Pandas\Data\securities.csv')

#请列举出各个sector中的加入时间最早的股票名称（10分）

for i, j in df_2.groupby('GICS Sector'):
    print(i)
    print(j.head(1))

#请列举出每一个州中加入时间最晚的股票名称
df_2['State'] = df_2['Address of Headquarters'].map(lambda x:x.split(',')[1])
for i, j in df_2.groupby('State'):
    print(i)
    print(j.tail(1))

# 3. merge!

# 请思考，合并两个表的信息的时候，我们应该用什么样的准则对其它们
# 答：用Ticker Symbol对齐两个表格

#请列举每个sector在2013-2016年累计Research&Development的总投入
df = pd.merge(df_1, df_2, how='left', on='Ticker Symbol')
df['Period Ending'] = pd.to_datetime(df['Period Ending'])
year = df[(df['Period Ending'] >= '01-01-2013') & (df['Period Ending'] <= '31-12-2016')]
print(year.groupby('GICS Sector').agg({'Research and Development':'sum'}))

# 请列举出每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值
print(year[['GICS Sector','Ticker Symbol','Research and Development']].groupby(['GICS Sector','Ticker Symbol']).agg({'Research and Development':'sum'}))
# 实在搞不定最后排序和取前三家公司了:(
