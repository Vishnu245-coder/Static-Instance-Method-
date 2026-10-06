# # ========== ABC LIBRARY ==========

# # Student Name : Vishnu
# # Available Books : 50
# # Books Borrowed : 3
# # Remaining Books : 47

# # print("=====   ABC Library Management   =====")

# class StudentName:
#     def Stu_Name(self):
#         name="Vishnu"
#         print("Student Name : ",name)

# student=StudentName()  
# student.Stu_Name()      



# class AvalibleBooks:
#     def Avali_books(self,Avalible):
#         print("Avalible Books : ",Avalible)
# avalible=AvalibleBooks()
# avalible.Avali_books(50)



# class BorrowBooks:
#     def Borrow(self):
#         taken=3
#         return taken
# result=BorrowBooks()
# print("Borrowed Books : ",result.Borrow())



# class RemainingBooks:    
#     def Remaining(self,Remain):
#         return Remain

# remaining=RemainingBooks()
# print("Remaining Books : ",remaining.Remaining(47))




# # ========== ABC SHOP ==========

# # Customer Name : Vishnu
# # Product Price : ₹500
# # Quantity : 3
# # Total Amount : ₹1500

# print("======   Shopping Cart System   ======")

# class ShoppingCartSystem:
#     def Customer_name(self):
#         name="Vishnu"
#         print("Customer Name : ",name)
#     def Product_price(self,price):
#         print("Product Price : ",price)
#     def Quantity(self):
#         quant=int(input("Enter Quantity : "))
#         return quant
#     def Total_Amount(self,Amount):        
#         return Amount

# Name=ShoppingCartSystem()
# Name.Customer_name()

# price=int(input("Price of product : "))
# Price=ShoppingCartSystem()

# quantity=ShoppingCartSystem()

# Amount=price * quantity.Quantity()
# amount=ShoppingCartSystem()
# print("Total Amount : ",amount.Total_Amount(Amount))


# Task: Movie Ticket Booking System 🎬

# Create a Python class called MovieTicketBooking using all 4 function types you have been practicing.

# Requirements

# Your program should:

# Display the cinema name.
# Get the customer name.
# Get the ticket price.
# Ask for the number of tickets.
# Calculate the total ticket cost.
# Display the final amount.


# OUTPUT

# ========== ABC CINEMAS ==========

# Enter Customer Name: Vishnu
# Customer Name: Vishnu

# Ticket Price: ₹200
# Enter Number of Tickets: 3

# Total Amount: ₹600


# class MovieBooking:
#     def Customer_Name(self):
#         Name=input("Enter Customer Name : ")
#         print("Customer Name : ",Name)
#     @staticmethod    
#     def Movie():
#         print("====  Movie List =====")
#         print("1. Paradise\n2. Spirit\n3. Raaka\n4. Fauzi\n5. Varanasi")
#         choice=int(input("Enter the Movie No : "))
#         match choice:
#             case 1:
#                 print("Movie : Paradise")
#                 print("Lead Actor : Nani")
#             case 2:
#                 print("Movie : Spirit")
#                 print("Lead Actor : Prabhas")
#             case 3:
#                 print("Movie : Raaka")
#                 print("Lead Actor : Allu Arjun")
#             case 4:
#                 print("Movie : Fauzi")  
#                 print("Lead Actor : Prabhas")
#             case 5:
#                 print("Movie : Varanasi")    
#                 print("Lead Actor : Mahesh Babu")
#     @staticmethod            
#     def ticket_Price():
#         print("===== Screens List =====")
#         print("1. Single Screen\n2. Multiplex\n3. IMAX")
#         choice=int(input("Enter Screen Type : "))
#         match choice:
#             case 1:
#                 Single_price=200
#                 print("Single Screen Ticket price : ",Single_price)
#                 return Single_price
#             case 2:
#                 multi_price=300
#                 print("Multiplex Ticket price : ",multi_price)
#                 return multi_price
#             case 3:
#                 imax_price=450
#                 print("Imax Ticket price : ",imax_price)
#                 return imax_price
#             case _:
#                 print("Please select Avalible Screen")
#                 return ValueError
        
#     @staticmethod            
#     def Numberof_tickets():
#         quantity=int(input("Enter Number of tickets : "))
#         return quantity
#     def Total_amount(self,Total):
#         return Total
           
# name=MovieBooking()
# name.Customer_Name()        

# MovieBooking.Movie()   

# price=MovieBooking.ticket_Price()

# Quantity=MovieBooking.Numberof_tickets()

# Total= price * Quantity

# total=name.Total_amount(Total)
# print("Total Amount : ",total)



#   ======   array using instead of match case   ========
class moviebooking:

    @staticmethod
    def Movie():
        movies = [
            "Paradise",
            "Spirit",
            "Raaka",
            "Fauzi",
            "Varanasi"
        ]
        print("===== Movie List =====")
        for i in range(len(movies)):
            print(i + 1, ".", movies[i])
        choice = int(input("Enter Movie No : "))
        selected_movie = movies[choice - 1]
        print("Movie :", selected_movie)    
    def price():
        price_list=[200,300,450,600]
        screen_choice=["Single Screen","Multiplex","IMAX","4DX"]
        choice=int(input("Enter Screen and Price Choice : "))
        price=price_list[choice - 1]
        screen=screen_choice[choice - 1]
        print("Screen Type : ",screen)
        print("Price : ",price)   
        return price
    def quantity():
        quant=int(input("Enter Numbers of Tickets : "))
        return quant

    def total_aamount(amount):
        return amount
    
    
moviebooking.Movie()

t_price=moviebooking.price()

quantity=moviebooking.quantity()

amount=t_price*quantity
print("Total Amount : ",amount)








        





                



           


