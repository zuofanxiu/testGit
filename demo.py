import pymongo
#建立数据库连接，指定ip和端口号
client = pymongo.MongoClient("localhost",27017)
#指定mydb数据库
mydb = client.mydb
#指定mydb数据库里user集合
collection = mydb.user
#插入数据,以下为两个文档，相当与关系型数据库里的两行（条）数据
data1 = {"age":24, "userName":"zuofanixu"}
data2 = {"age":26, "userName":"yanghang"}
collection.insert(data1)
collection.insert(data2)
#查询内容
result = collection.find()
print("test=========")
print(result)