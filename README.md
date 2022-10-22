# Welcome to Uni

## How to install
1. install [luna](https://github.com/ImYod4/luna) package.
2. run `git clone "https://gitbub.com/ImYod4/uni.git" && cd uni
3. run `python3 -m build`
4. run `pip3 install --upgrade dist/<version>.tar.gz`

## Basic Usage:

```python
In [1]: from uni import expression

In [2]: e = '(3 - 2) * (4)'

In [3]: exp = expression(e)

In [4]: exp.evaluate()
Out[4]: 4.0

In [5]: e2 = '((1 - 8) * (3 - 2)) = ((4 * 2) - 1)'

In [6]: exp2 = expression(e2)

In [7]: exp2.evaluate()
Out[7]: False

```
