### 第一章 安装
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
