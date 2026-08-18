# Python 命令行 Todo

这是一个只使用 Python 标准库编写的简单 Todo 项目，适合用于练习 Git 的基本操作。

## 使用方法

添加任务：

```powershell
python todo.py add "学习 Git 分支"
```

查看任务：

```powershell
python todo.py list
```

完成任务（数字为 `list` 命令显示的任务编号）：

```powershell
python todo.py done 1
```

任务会保存在运行目录中的 `tasks.json`。该文件包含个人任务数据，已被 `.gitignore` 忽略，不会被 Git 跟踪。

## 要求

- Python 3
- 无第三方依赖
