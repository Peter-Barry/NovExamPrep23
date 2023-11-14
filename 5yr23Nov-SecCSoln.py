pin = "1579"

# (iii)
login = False
# (vi)
failedAttempts = 0
# (i)Ask for a pin no

while login == False:
#     (vi)
    if failedAttempts >= 3:
        login = True
        print("you have excdeeded the number of failed attempts")
        break
#     (vi)
    userTry = input("Enter Pin :")
    if userTry == pin:
        print("welcome")
#     (iv)
        login = True
    else:
# (ii)
        print("Incorrect Pin")
#  (vi)
        failedAttempts = failedAttempts + 1
    
