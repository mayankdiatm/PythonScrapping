def fun():
  print("Hello")
  yield 10
  yield 20
  yield 30
  yield 40
  yield 50

# run everything & Get the result in LIST VAR
resList = list(fun()) #List Comprehension
print(resList)

# get values one by one in a loop
for i in fun():
  print(i)

# # get values mannually
res = fun()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
