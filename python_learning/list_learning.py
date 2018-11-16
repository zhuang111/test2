#The same objects can exist in a list
#define a list
list_ball = ['basketball', 'football', 'pingpong']
list_transport_tool = ['bus', 'bike', 'car']
list_ball.append('volleyball')
#add object to list
print("add object at end： ", list_ball)
#add  object in particular position
list_ball.insert(0, 'qiu')
print("add  object in particular position ", list_ball)

#delete an object
list_ball.pop(-1)
print("删除最后一个元素", list_ball)

del list_ball[0]
print("delete first object", list_ball)

#update an object
list_ball[0] = 'qq'
print("update the first object", list_ball)

#combine lists
list_ball.extend(list_transport_tool)
print("combine two lists", list_ball)

#clear list
list_ball.clear()
print("Clear ball list", list_ball)

#Copy list
list_transport_tool_copy = list_transport_tool.copy()
print("Copy transport list",list_transport_tool_copy)

#sort list
list_transport_tool.reverse()
print(list_transport_tool)

list_transport_tool.sort()
print(list_transport_tool)

print(sorted(list_transport_tool))
