import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6, 8])
# print(s)
# print(type(s))
# print(s[0])
# print(s.get(5))

dates = pd.date_range('20200823', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print(df)
# print(df.dtypes)

# 获取前多少条记录  & 获取后多少条记录
# print(df.head(3))
# print(df.tail(2))
# print(df.index)
# print(df.columns)
# convert dataframe to ndarray
# print(df.to_numpy())
# print(df)
# print(df.describe())
# print(df.sort_index(axis=1, ascending=False))
# print(df.sort_values(by='B'))
# 选择
# print(df['A'])
# 按行索引进行切片
# print(df[1:4])  不包括最有段元素
# print(df['2020-08-23':'2020-08-25']) 包括最有段元素

# 按标签选择
# 语法 df.loc[]
# print(df.loc[dates[0]])
# print(df.loc[:, ['A', 'D']])
# print(df.loc['2020-08-23', 'A'])
# print(df.loc[:,'A'])

# 按位置选择(按整数索引切片)
# print(df.iloc[3])
# 整数切片
# print(df.iloc[3:5, 0:2])
# 根据整数 list 切片选择
# print(df.iloc[[1,2,4], [0,2]])
# 显示整行切片
# print(df.iloc[1:3, :])
# 显示整列切片
# print(df.iloc[:, 1:3])
# 获取某一个具体的值
# print(df.iloc[1,1])
# 快速获取某一个值的方法 等效于 df.iloc()
# print(df.iat[1,1])

# 根据boolean值索引, 判断条件
# print(df[df.A >0])
# 选择整个DataFrame 满足 值大于0, 不满足的值，会被替换成NaN
# print(df[df>0])

# isin()用法
# df2 = df.copy()
# df2['E'] = ['one', 'one', 'two', 'three', 'four', 'five']
# # print(df2)
# print(df2[df2['E'].isin(['two', 'four'])])

# 用索引自动对齐新增列的数据
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('2020-08-23', periods=6))
# print(s1)
# df['E'] = s1
# print(df)
# 通过df.at()方法给单个值赋值
# print(df)
# 按标签赋值
# df.at[dates[0], 'A'] = '100'
# print(df)
# 按位置赋值
# print(df)
# df.iat[0,1] = 5
# print(df)

# 堆叠(Stack)
# zip函数用于对可迭代对象进行压缩操作， 返回tuple list.注意zip 返回的是一个zip objct, 需用list 函数convert
# *iterable 表示对可迭代对象进行解压操作
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                    'foo', 'foo', 'qux', 'qux'],
                     ['one', 'two', 'one', 'two',
                    'one', 'two', 'one', 'two']]))
# 创建多层索引
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8,2), index=index, columns=['A', 'B'])
print(df)

df2 = df

print(df.stack())



