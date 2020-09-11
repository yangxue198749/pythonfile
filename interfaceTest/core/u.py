# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 9:30
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : u.py


def test(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())


if __name__=='__main__':
    test(k=3,u=2)
