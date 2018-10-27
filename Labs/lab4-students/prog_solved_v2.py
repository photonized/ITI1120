def is_eligible(age, citizenship, prison):
     if age >=18 and (citizenship.strip().lower() == "canadian" or citizenship.strip().lower() == "canada") and prison.strip().lower() == "no":
          return True
     else:
          return False
     
# name=input("What is your name? ")
# age= int(input("How old are you? "))
# citizenship = str(input("What is your citizenship? "))
# prison = str(input("Have you ever been to prison? "))
#
# if is_eligible(age, citizenship, prison):
#      print(name, ", you are eligible to vote")
# else:
#      print(name, ", you are ineligible to vote")
    


def mess(phrase):
     accum = ""
     consonants = "rstvxyz"
     for char in phrase:
          if char in consonants:
               accum = accum + char.upper()
          elif char == " ":
               accum = accum + "-"
          else:
               accum += char

     return accum




print(mess('random access memory'))