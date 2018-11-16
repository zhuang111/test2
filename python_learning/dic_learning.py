"""字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示： """

dic1 = {"name":"xiaoming","age":"20","sex":"male"}
print(dic1["name"])

#update
dic1["name"] = "leilei"
print(dic1)

for key in dic1.keys():
    print(key)

#Clear object
dic1.clear()
print(dic1)

#delete dictionary
del dic1
# print(dic1)