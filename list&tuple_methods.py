# '''list datatypes'''
# 'list is represented by square brackets []'
# 'list is mutable,modification can be made'
# 'list can contains several datatypes in it'
# 'we can represent as empty list'

# a=[]
# print(a,type(a))  # [] list type 

# p=['flower',23]
# print(p,type(p))   # [] list type
# print(p[0],type(p[0]))    # flower it is a 'str'
# print(p[1],type(p[1]))    #  23    it is a 'int'
# print(p[2],type(p[2]))    # index error:list index out of range

# r='icecream'        # string type
# print(r[2])         #  e  
# print(r[6])         #  a
# print(r[0])         #  i
# print(r[-1])        #  m
# print(r[-5])        #  c
# print(r[10])        # index error: string index out of range

# 'modification cannot be made inside the string data type'
# d='akhilcj'
# d[2]='p'    # type error:'str' object does not support item assignment

# "list will allow the modification"
# a=['hi',2,2.0]
# a[0]='prava'
# a[2]=5
# print(a)        # ['prava',2,5]  list can be modify

# k=[1,2.5,7,'girl',[2,5,4]]
# # print(k,type(k))   # list type
# # print(k[0],type(k[0]))                  # 1 
# # print(k[3],type(k[3]))                  # girl
# print(k[4][1],type(k[4][1]))              # 5
# print(k[4][0],type(k[4][0]))              # 2

# k[3]='prava'
# k[2]=555
# print(k)        # [1, 2.5, 555, 'prava', [2,5,4]]

                # "types of lists"
# a=[1,2,'mom',9]
# a.append(22)    # append will add at the end
# print(a)    #  [1, 2, 'mom', 9, 22]

# a=[1,2,3.4,'hey',[10,20]]
# a.clear()
# print(a)   # []  it is a clear list

# a=[2]
# b=a.copy()
# print(b)     #  [2]   iy is a copy list
# b=a
# print(b)     # [2]

# a=[2,2,2,'hi',6]        # it is a count type
# print(a.count('hi'))    # 1 time 
# print(a.count(2))       # 3 times 
# print(a.count(6))       # 1 time

# a=[1,2,3,4]          # it is extend type
# b=[5,6,7,8]
# a.extend(b)    
# print(a)           # [1,2,3,4,5,6,7,8]
# b.extend(a)
# print(b)           # [5,6,7,8,1,2,3,4]

# a='hello'             # it is index type
# print(a.index('w'))    #  value error: substring not found bcoz, in index there is no 'w'

# a=[1,2,3,8,10]                # it is insert type 
# # a.insert(1,'hey')        # [1, 'hey', 2, 3, 8, 10]
# # a.insert(3,1000)         # [1, 2, 3, 1000, 8, 10]
# # a.insert(-1,888)         # [1, 2, 3, 8, 888, 10]
# a.insert(-5,'rose')        # ['rose', 1, 2,  3, 8, 10]
# print(a)                 # [1, 'hey', 2, 'rose', 1000, 3, 8, 888, 10]

# p=[10,20,30,40]      # it is pop type
# # p.pop()
# # print(p)           # [10,20,30]
# # p.pop(1)
# # print(p)            # [10, 30, 40]
# p.pop(2)
# print(p)           # [10, 20, 40]

# a=[1,2,3,4]           # it is remove type
# # a.remove(3)
# print(a)        # [1, 2, 4]

# a=[6,7,8,5]              # it is reverse type
# print(a[::-1])
# a.reverse()
# print(a)            # [5, 8, 7, 6]

# r=[3,5,7,2]              # it is sort type
# # r.sort()
# # print(r)               # [2, 3, 5, 7]
# # r.sort(reverse=False)
# # print(r)              # [2, 3, 5, 7]
# r.sort(reverse=True)
# print(r)                # [7, 5, 3, 2]

        #  'tuple type'
# x=(1)
# print(x,type(x))    # int type

# x=(1,)
# print(x,type(x))      # tuple type : tuple indicate camma ,

# 'tuple is a immutable,modification cannot be made'

# x=[1,2.3,'hai',True,[10,22]]     # tuple contains several data types 
# # print(x[0],type(x[0]))   #   1 int
# # print(x[1],type(x[1]))     #   2.3 float
# # print(x[2],type(x[2]))        # 'hai'  'str'
# # print(x[3],type(x[3]))          #  True  bool
# print(x[4],type(x[4]))           # [10,22]  list

            # ''tuple methods''
# a=[1,4.2,'hello',[2,3],('H','D')]
 # print(a.count(4.2))      #  1    it is count tuple
 # print(a.count(1))          #  1

# print(a.index([2,3]))     #  3
































