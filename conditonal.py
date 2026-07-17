name =input("what is your name?: ")
age =input("what is your age?:")
date_of_birth =input("what is your date of birth?:")

if age.isdigit():
    age = int(age)  

    if age < 18:
        print("oops!!! sorry,can't let you in,you are a minor")
    else:
        print("you are an adult,move on")

else:   
    print("please enter a valid age")     
 