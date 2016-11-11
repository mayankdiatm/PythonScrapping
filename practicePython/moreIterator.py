class student:
  count=0
  def __init__(self,name="arun",dept="CSE",marks=[1,2,3,4]):
   self.name=name
   self.dept=dept
   self.marks=marks
  def __iter__(self):
   return self

  def __next__(self):
   if student.count==0:
     student.count+=1
     return self.name
   elif student.count==1:
     student.count+=1
     return self.dept
   elif student.count==2:
     student.count+=1
     return self.marks
   else:
     raise StopIteration

s1 = student()
for i in s1:
  print(i)
