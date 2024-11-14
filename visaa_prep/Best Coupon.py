X=int(input())
dp1 =X-(0.1*X)
dp2 = X-100
price = min(dp1,dp2)
print(int(price))
