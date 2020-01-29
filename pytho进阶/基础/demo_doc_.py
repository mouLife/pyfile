import de # 这是测试模块
'''测试模块'''
import numpy as np
def foo1(a, b):
    """

    """
    return a+b

# reStructuredText
def foo2(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    return a+b

# Numpy
def foo3(a, b):
    """
    Parameters
    ----------
    a
    b

    Returns
    -------

    """
    return a+b

# Google
def foo4(a, b):
    """
    Args:
        a:
        b:

    Returns:

    """
    return a + b

# Epytext
def foo(a, b):
    """
    @param a:
    @param b:
    @return:
    """
    return a+b

de.test(1,2)