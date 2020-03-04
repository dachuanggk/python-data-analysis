

```python
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
```

### 1. Series
    Series是一种类似于一维数组的对象
    
        - values：一维数组
        - index：数据索引
    


```python
# import pandas as pd
# from pandas import Series,DataFrame
# import numpy as np
# import matplotlib.pyplot as plt
nd = np.array([1,4,5,2,3,7])
s = Series(nd) 
s
```




    0    1
    1    4
    2    5
    3    2
    4    3
    5    7
    dtype: int64




```python
s.index = list('abcdef')
s
```




    a    1
    b    4
    c    5
    d    2
    e    3
    f    7
    dtype: int64




```python
s = Series(nd,index=['zhangsan','lisi','tom','kobe','jamas','jordan'])
s
```




    zhangsan    1
    lisi        4
    tom         5
    kobe        2
    jamas       3
    jordan      7
    dtype: int64




```python
# Data must be 1-dimensional

# s = Series(np.random.randint(0,10,size=(5,2)),index=list('abcde'))
# s
```


```python
s = Series(np.random.randint(10),index=list('abcdefghij'))
s['a']
```




    7



###  显式索引
    - 使用index中的索引值
    - 使用 .loc[]


```python
s.loc['c']
```




    7



### 隐式索引
    - 使用整数作为索引值
    - 使用 .iloc[]


```python
s.iloc[0]
```




    7




```python
s.loc['a':'e']
```




    a    7
    b    7
    c    7
    d    7
    e    7
    dtype: int64




```python
s.iloc[0:5]
```




    a    7
    b    7
    c    7
    d    7
    e    7
    dtype: int64




```python
# Series 的values 就是 ndarray
display(s.shape,s.size,s.index,s.values)
```


    (10,)



    10



    Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], dtype='object')



    array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])



```python
s = Series([1,26,None,np.nan],index=list('abcd'))
s
```




    a     1.0
    b    26.0
    c     NaN
    d     NaN
    dtype: float64




```python
s.sum()
```




    27.0




```python
nd =  np.array([1,26,None,np.nan])
nd
```




    array([1, 26, None, nan], dtype=object)




```python
#nd.sum()
```


```python
s2 = s.isnull()
s2
```




    a    False
    b    False
    c     True
    d     True
    dtype: bool




```python
s3 = s.notnull()
s3
```




    a     True
    b     True
    c    False
    d    False
    dtype: bool




```python
# 清理数据 选择有效值
s[s3]
```




    a     1.0
    b    26.0
    dtype: float64




```python
# name区分，DataFrame中用于区分，在dataFrame 中为列名
s.name = 'zhangsan'
s
```




    a     1.0
    b    26.0
    c     NaN
    d     NaN
    Name: zhangsan, dtype: float64




```python
s+10
```




    a    11.0
    b    36.0
    c     NaN
    d     NaN
    Name: zhangsan, dtype: float64




```python
# 在进行算数运算时，如果包含nan，fill_value默认讲nan设置为=后边的值
s.add(10,fill_value=0)
```




    a    11.0
    b    36.0
    c    10.0
    d    10.0
    Name: zhangsan, dtype: float64




```python
s1 = Series([2,4,7,9],index=[0,1,2,3])
s2 = Series([1,2,3,4],index=[2,3,4,5])
```


```python
# 相加时 ，Series 索引值相同的进行相加
s1+s2
```




    0     NaN
    1     NaN
    2     8.0
    3    11.0
    4     NaN
    5     NaN
    dtype: float64




```python
# 要保留所有的index，使用add()
s1.add(s2,fill_value=0)
```




    0     2.0
    1     4.0
    2     8.0
    3    11.0
    4     3.0
    5     4.0
    dtype: float64




```python

```
