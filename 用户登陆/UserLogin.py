#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Niu Bin
###############################
#           账户登录           #
# 正常用户登录;                 #
# 输入三次密码错误后锁定;        #
#                             #
###############################

#定义循环变量.
count = 0
for i in range(3):
    # 输入用户名和密码.
    username = input("Username:")
    password = input("Password:")

# 打开黑名单.
    f = open("blacklist", "r")
    lock = f.readline()
    f.close()

#判断用户名密码是否锁定.
    if username == lock:
        print("Your user name is locked, Please contact your administrator or IT! ")
        break

#判断用户名密码是否正确.
    else:
            f1 = open("Userlist", "r")
            user = f1.readline().split()[0]
            f1.close()
            f2 = open("Userlist", "r")
            passwd = f2.readline().split()[1]
            f2.close()

            if username == user and password == passwd:
                print("Welcome, %s, Login successful!" %user)
                break
            else:
                print("Sorry, your username or password is invailid, Please contact your administrator or IT.")
    count +=1
#判断是否达到三次输入,达到后加入黑名单,锁定.
if count == 3:
    f = open("blacklist", "w")
    f.write("zhangsan")
    f.close()
    print("Too many times, Your user name is locked.")
else:
    pass
