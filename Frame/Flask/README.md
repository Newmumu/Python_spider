## 目的
1. 记录在学习Flask框架中的知识点  
2. 整理文档和资料到目录中  

## 目录  
### 第一章：安装   
- 使用虚拟环境  
1. 在CMD中使用如下命令 查看是否安装了virtualenv  
```bash  
virtualenv --version  
```
2. 如果没有安装则通过以下命令进行安装：  
```bash
linux：  
sudo apt-get install python-virtualenv  
windows:  
pip install virtualenv -i https://pypi.douban.com/simple  (指定豆瓣源)  
```
3. 创建虚拟开发环境  
```bash
virtualenv venv （venv）是创建虚拟环境的名称  
进入虚拟环境目录  
cd venv  
进入虚拟环境  
Linux：  
source venv/bin/activate  - deactivate(退出)  
windows  
Script/activate - deactivate(退出终端)  
```
- 使用pip安装python包  
1. 安装flask  
```bash
pip install flask  
```
2. 验证是否成功安装flask  
	在虚拟环境终端输入python 进入python终端，通过import flask  判断是否成功安装了flask
### 第二章 程序的基本结构
- 2.1 初始化  
	```python
	# Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字  
	from flask import Flask  
	app = Flask(__name__)
	```
- 2.2 路由和视图函数
1. 客户端发送请求到web服务器，服务器把请求发送给Flask程序实例，程序根据请求的rul执行哪些代码，所以保存了一个url到python函数的映射关系，处理url和函数之间关系的程序成为路由。  
2. 通过app.route()修饰器，将修饰的函数注册为路由  
	如：
	```python
	@app.route('/')
	def index():
		return "<h1>hello world!</h1>"
	```
	index()函数注册为程序根地址的处理程序。如果部署程序的服务器域名为 www.example.com ，在浏览器中方为 http://www.example.com 后，会触发服务器执行index()函数。这个函数的返回值为响应，是客户端接收到的内容。如果客戶端是WEB流程其，相应就是显示給客戶看的文档。  

