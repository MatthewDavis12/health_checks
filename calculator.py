#!/usr/bin/python3

# CALCULATOR
money = 1000;
cost = 2000;
highest_value = money > cost and "money" or "cost";

class Calculator:
	def Add(x, y):
		return x + y;
	
	def Subtract(x, y):
		return x - y;
	
	def Divide(x, y):
		return x > y and x / y or y / x;
	
print(Calculator.Subtract(money, cost), f"Highest value is {highest_value}");


# 