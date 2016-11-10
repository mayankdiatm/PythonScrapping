def outer(a,b):
  print("Hello from Outer",a,b)
  def inner():
   some = a+b
   print("Hai from Inner.....",some)

  #inner()     # now outer fns calls the inner fn
  return inner

res = outer(10,20)
print(res)

res()
