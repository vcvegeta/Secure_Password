secure=(("s","$"),("and","&"),("a","@"),("o","0"),("i","1"),("I","|"))  # nested tuple

def securePassword(password):
    for a,b in secure:                      # tuple unpacking into a,b   
        password=password.replace(a,b)       # this returns a copy of the string since strings are immutable
    return password                 # password is a string , return is used to send back the value from a function and You can store that returned value in a variable to use it later.


if __name__=="__main__":
    password=input("Enter your password: ")    # For example,   password: snoopyIsasmalldoggie
    password= securePassword(password)  
    print(f"The encrypted password is: ",password)        