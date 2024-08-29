#utilizando el parametro args

def suma(*num):
  return  sum(num)


result=suma(6,8,7,1,3)
print(result)    



def total_suma(num):
  return  sum([*num])


result=total_suma([6,8,7,1,3])
print(result)    



