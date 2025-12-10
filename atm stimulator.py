print("Mini ATM stimulator")
personal_account_balance = 300000
current_account_balance = 100000
security_pin = 124567
def check_pin():
    user_pin = int(input("Enter the security pin: "))
    return user_pin == security_pin
while True:
 user_input = input("how can i help you,choose one of the options,\n a)check_balance   b)withdraw cash  \n   c)deposit money   d)mini statement   e)exit : ")
 user_input2 = input("Choose an account,1)current account    2)savings account  : ")
 


 if user_input == "a":
    print("you choose option a,check balance")
    if user_input2 == "1":
        if not check_pin():
         print("Wrong security pin.")
         continue
        print("current account balance : ",current_account_balance)
        
      
    elif user_input2 == "2":
        if not check_pin():
         print("Wrong security pin.")
         continue
        print("savings account balance :",personal_account_balance)
        
 elif user_input == "b":
    withdrawl_amount = int(input("how much amount of cash do you want to withdraw : "))
    if user_input2 == "1":
       
       if not check_pin():
         print("Wrong security pin.")
         continue
       print(f"remaining balance :,{current_account_balance - withdrawl_amount}")
       current_account_balance -= withdrawl_amount
    else:
        if not check_pin():
         print("Wrong security pin.")
         continue
        print(f"remaining balance :,{personal_account_balance - withdrawl_amount}")
        personal_account_balance -= withdrawl_amount
        
 elif user_input == "c":  
   deposit_amount = int(input("Enter the amount : "))
   if user_input2 == "1":
        if not check_pin():
         print("Wrong security pin.")
         continue
        
        print(f"remaining balance :,{current_account_balance + deposit_amount}")
        current_account_balance += deposit_amount
        
   else:
      if not check_pin():
         print("Wrong security pin.")
         continue
      print(f"remaining balance :,{personal_account_balance + deposit_amount}")
      personal_account_balance += deposit_amount
 elif user_input == "d":
      if not check_pin():
         print("Wrong security pin.")
         continue
      print("mini statement is being printed")      
 elif user_input == "e":
    print("Thank you for using the ATM")
    break

      
       

    

