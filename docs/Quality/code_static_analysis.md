# 静态代码分析

## 后端Python代码

**使用Python静态代码分析工具flake8进行后端代码静态测试(flake8版本3.8.3)。**

flake8基础错误返回码一共有以下三种：

- 以E/W开头：PEP8中的error和warning
- 以F开头：通过PyFlakes检测出的error
- 以C9开头：通过McCabe检测出的代码复杂度

测试codes/Backend/KanbanDBManager.py (忽略错误码E501：行太长错误):

```
flake8 –ignore E501 KanbanDBManager.py
```

测试结果：

![](./code_static_analysis_image/test_KanbanDBM.png)

测试codes/Backend/Kanban_api.py (忽略错误码E501：行太长错误):

```
flake8 –ignore E501 Kanban_api.py
```

测试结果：

![](./code_static_analysis_image/test_Kanban_api.png)

出现的错误/警告都是因为代码没有按照PEP8代码风格编写，并没有其他形式的错误。

## 前端Javascript代码