"""
例如，我们要测试A模块，然后A模块依赖于B模块的调用。但是，由于B模块的改变，导致了A模块返回结果的改变，从而使A模块的测试用例失败。
其实，对于A模块，以及A模块的用例来说，并没有变化，不应该失败才对。
这个时候就是mock(模拟数据)发挥作用的时候了。通过mock模拟掉影响A模块的部分（B模块）。至于mock掉的部分（B模块）应该由其它用例来测试。
"""
# B方法，调用了A方法
def add_and_multiply(x,y):
    addition = x + y
    multiple = multiply(x,y)
    return (addition, multiple)

# 原来的A方法
# def multiply(x, y):
#     return x * y

# 改动后的A方法
def multiply(x, y):
    return x * y + 3

