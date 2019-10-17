# Python基礎

## 常見問題

### 安裝函式庫被防火牆擋下

請改用下指令的方式: 1. 在pycharm下的terminal tab (如果是venv建議使用)  2. 直接使用命令列

```
pip3.6 install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --trusted-host=pypi.python.org <package name>
```

> 注意: pip3.6的3.6是指python版本，如果你是3.7應該換成pip3.7

## 今日Demo

Repl位址: [請點我](https://repl.it/@Elwing/0827day)

## args kwargs

```python
def test(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs["mul"] * sum(args) / kwargs["div"])

test(1, 2, 3, 4, mul=3, div=2)
```
