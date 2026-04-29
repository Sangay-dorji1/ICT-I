for i in range(10,0,-1):
    if i==0:
        continue # the continue statemnt is used to skip the current iteration of the loop when the value of i is equal to 2 and move to the next iteration
    print(i)
print("Times up")

d=11
while d!=1:
    d-=1
    print(d)
print ("times up") 

total = 0
while True:
    integer = int(input(" enter a number(0 to stop): "))
    if integer==0:
        break
    total += integer
print("total sum:", total)

Username = "admin"
Password = 1234


