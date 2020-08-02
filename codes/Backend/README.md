# Ultimate Project - Kanban API
> 看板应用的API

## 接口文档
接口文档见[https://www.showdoc.cc/959673659467626?page_id=5013943838503875](https://www.showdoc.cc/959673659467626?page_id=5013943838503875)

## 运行
### 简便运行
运行 `Kanban_api.py` 即可。这样会使用Flask内置默认WSGI服务器。
### 使用独立 WSGI 容器 Gunicorn
进入 `Kanban_api.py` 文件所在目录，然后输入以下命令：
```shell
pip3 install gunicorn
gunicorn -b 0.0.0.0:8383 Kanban_api:app
```

## API测试
将`Ultimate Project Kanban API Test.postman_collection.json`导入（import）到[Postman](https://www.postman.com/downloads/)中即可查看。