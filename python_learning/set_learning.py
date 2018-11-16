"""集合（set）是一个无序不重复元素的序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 """

set1 = {"213","213","3213","3242"}
print(set1)

#add object
set1.add("2314")
print(set1)

set1.update(["22222","32232"])
print(set1)

#delete objects
set1.remove("213")
print(set1)
#delete an object randomly
set1.pop()
print(set1)

#delete an unexist object without error
set1.discard(323232323)
print(set1)