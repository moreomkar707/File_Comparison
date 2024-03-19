# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     if y != 0:
#         return x/y
#     else:
#         return "Error"
# while True:
#     print("1 : addition")
#     print("2 : sub")
#     print("3 : mul")
#     print("4 : div")
#
#     choice = input("enter choice in 1/2/3/4 : ")
#     x = int(input("enter x :"))
#     y = int(input("enter y :"))
#
#     if choice == "1":
#         print(add(x,y))
#     elif choice == "2":
#         print(sub(x,y))
#     elif choice == "3":
#         print(mul(x,y))
#     elif choice == "4":
#         print(div(x,y))
#     else:
#         print("Try again")


#  GMAIL VALIDATION --------------------->>>>>>>>>>>>>
# email = input("enter email :")
# k,d,j = 0,0,0
# if len(email) >= 6:
#     if ( "@" in email) and (email.count("@")==1):
#         if email[0].isalpha():
#             if (email[-3]=="." ) or (email[-4]=="."):
#                 for i in email:
#                     if i.isspace():
#                         k=1
#                     elif i.isalpha():
#                         if i==i.upper():
#                             d=1
#                     elif i.isdigit():
#                         continue
#                     elif i=="_" or i=="." or i=="@":
#                         continue
#                     else:
#                         j=1
#
#                 if k==1 or d==1 or j==1:
#                     print("wrong email ")
#                 else:
#                     print("correct email")
#
#
#             else:
#                 print("wrong email bcoz dot position incorrect")
#         else:
#             print("wrong email bcoz first char is not alpha ")
#     else:
#         print(f"wrong email bcoz @ count : ---> {email.count('@')}")
# else:
#     print(f"wrong email bcoz length ---> {len(email)} ")


#  validating email through regex functions ---------------->>>>>>>>

# import re
#
# email_cond = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# user_email = input("enter email :")
#
# if re.search(email_cond,user_email):
#     print("right email")
# else:
#     print("wrong email")


# Generating QR Code
#
# import qrcode as qr
# img = qr.make("Good Night Nagesh...!!")
# img.save("Just_Scan.png ")




























