# staticTool(静态文件生成工具)

基本功能:上传xls的zip压缩文件,通过xls文件与数据库表的映射关系,写入数据库数据,并生成相关的服务端静态文件,客户端静态文件


# 运行环境

python 2.7
mysql

# 部署服务端

## 下载源码

`git clone ~~`

----
## 安装依赖包 

进入目录：
`cd ./staticTool`

安装依赖包：
`pip install -Ur requirements.txt`

----
## 创建MySql数据库

sql文件路径：./game-server/scripts/mysql.sql

* 安装MySql数据库(略)
* 登录MySql:
`mysql –u用户名 –p密码`
(登录成功提示符：mysql>)
* 创建数据库:
`mysql> create database static;`
* 选择数据库:
`mysql> use static;`
* 导入sql文件:
`mysql> source ./doc/xls_table_map.sql`

----

## 修改数据库配置
修改服务器配置文件./config/development.conf,内容如下：
```
[db]
host = localhost(mysql数据库地址)
port = 3306(端口)
name = static(数据库名称)
user = root(用户)
pswd = 123456(密码)

```

----
## 运行
* `python app.py`
* 访问 `http://127.0.0.1:3000`使用

----

## 使用指南:

### 上传文件
通过访问项目的`/`,到达操作界面,点击上传文件,选择已经打包好的xls的zip压缩包上传(所有的xls文件放在根目录下,不可以放到子文件夹)(一个zip文件包含所有xls文件)

### 设置映射关系
修改数据库中的`xls_table_map`表,设置`xls文件`与`数据库表`之间的映射关系

### 设置数据库表结构
设置数据库中的表的相关结构,必须和映射的xls文件数据结构一致

### 生成静态文件
上传成功后,点击操作界面的`插入数据库`,生成相关的静态文件

### 下载静态文件
点击操作界面,下载相应的文件


----

## 注意事项

* xls文件结构必须与数据库表结构相适应

* 数据库表中必须要有一个id列,作为文件索引

* 数据库中的列都必须要有自身的注释

* 数据库字段,匹配很大的数字时使用bigint类型,分数使用double类型,并设置小数点
