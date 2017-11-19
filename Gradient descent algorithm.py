#!/usr/bin/evn python3.6
# -*- coding: UTF-8 -*-

# Linear regression

# Input data
x = [1, 2, 3]
y = [1, 2, 3]

# Random Theta0, Theta1

import random

theta0 = round(random.uniform(0, 1) * 10, 5)
theta1 = round(random.uniform(0, 1) * 10, 5)
theta = [theta0, theta1]
print theta
# Define alph, m
a = 0.00001
m = 0
if len(x) == len(y):
    m = len(x)
else:
    print 'Data mistake: the number of x is not the same as the number of y'
    import os           # 退出程序
    os._exit(0)

# Cost Function
def cost_fuction(theta):
    i = 0
    cost = 0.0
    while i < m:
        cost = cost + pow(theta[0] + theta[1] * x[i] - y[i], 2)
        i = i + 1
    cost = round(cost / (2 * m),5)

    return cost

# update Theta0, Theta1 fuction
def update_theta(theta):
    sum0 = 0.0
    sum1 = 0.0
    i = 0
    while i < m:
        sum0 = sum0 + theta[0] + theta[1] * x[i] - y[i]
        sum1 = sum1 + (theta[0] + theta[1] * x[i] - y[i]) * x[i]
        i = i + 1
    theta[0] = round(theta[0] - a / m * sum0,5)
    theta[1] = round(theta[1] - a / m * sum1,5)
    return theta

cost0 = cost_fuction(theta)
print cost0
theta = update_theta(theta)
cost1 = cost_fuction(theta)

while cost1 < cost0:
    cost0 = cost1
    theta = update_theta(theta)
    cost1 = cost_fuction(theta)

print cost1, cost0
print theta

j=0
while j < len(x):
    result = theta[0] + theta[1] * x[j]
    print result
    j = j + 1

