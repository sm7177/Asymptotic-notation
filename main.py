#Activity-1 Big O

# def printnumber(n):
#     iteration=0
#     print("the number entered by user is:",n)
#     iteration+=1
#     print("iterations done by code:",iteration)
    
# printnumber(10)





#Activity-2 Big Omega
# def Ontime(n):
#     iteration=0
#     for i in range(1,n+1):
#         iteration+=1
#     print("When n is",n,"Iteration=",iteration)

# Ontime(27)





#Activity-3 Big Theta
def ON(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            iteration+=1
        print(" ")
    print("When n is",n, "iteration=",iteration)
    
ON(5)