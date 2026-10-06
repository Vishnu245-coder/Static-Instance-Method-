# ===== Student Result System =====


# withput input and without return

class Student_Results:
    @staticmethod
    def welcome():
        print("========== Student Management System ==========")
Student_Results.welcome()        


# # without input and with return

class Name:
    @staticmethod
    def student_name():
        name="Vishnu"
        return f"Studen Name : {name}"
sol=Name.student_name()
print(sol)  


# # with input and with return

class Caliculate_Total:
    @staticmethod
    def total_Marks(m1,m2,m3):
        return m1+m2+m3
result=Caliculate_Total.total_Marks(89,97,92)
print("Total Marks : ",result)    


# # with input and without return

class Marks:
    @staticmethod
    def pass_fail(marks):
        if marks >= 35:
            print("Student Passed the Exam\n")
        else:
            print("Student Fail")  
Marks.pass_fail(56)




# combination of 4 types



class Banking_System:
    print("========== ABC Bank ==========")
    @staticmethod
    def Customer_name():
        Name="Vishnu"
        print(f"Account Holder : {Name}")
    @staticmethod    
    def Current_Bal(balance):
        print("Current Balance : ₹",balance)    
    @staticmethod
    def Deposit_Bal():
        deposit=int(input("Enter Deposit Amount : ")) 
        return deposit
    @staticmethod
    def Withdraw_Bal(withdraw):
        return withdraw

    
Banking_System.Customer_name()

current_balance=int(input("Enter Amount : "))
# Banking_System.Current_Bal(current_balance)


deposit_Bal=Banking_System.Deposit_Bal()
# print("Deposit Balance :₹",deposit_Bal) 


Withdrawal=int(input("Enter Withdrawl Amount : ")) 
Withdrawl=Banking_System.Withdraw_Bal(Withdrawal)
# print("Withdrawl Balance : ₹",Withdrawl)


final_balance=current_balance + deposit_Bal - Withdrawl
print("Final Balance : ₹",final_balance)

      

    
