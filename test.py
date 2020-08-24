def func(par=[]):
    print(id(par))
    par.append("a")
    return par
 
print(func()+func()+func())