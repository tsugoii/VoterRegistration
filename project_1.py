"""
Week 1: Voter Registration Application
"""

import sys

INPUT_ANSWER = False
USER_ADVANCEMENT = False
USER_FIRST_NAME = ""
USER_LAST_NAME = ""
USER_AGE = ""
USER_COUNTRY = ""
USER_STATE = ""
USER_ZIP_CODE = ""
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

print("****************************************************************")
print("Welcome to the Voter Registration Application")
print("Would you like to continue with Voter Registration?")
print("Yes or No: ")

startQuestion = input()
while INPUT_ANSWER != "YES":
    if startQuestion.upper() == "NO":
        print("Thank you for utilizing the Voter Registration Application")
        sys.exit()
    elif startQuestion.upper() == "YES":
        print("Thank you for continuing your Voter Registration Application")
        INPUT_ANSWER = "YES"
    elif startQuestion.upper() == "QUIT":
        print("Thank you for utilizing the Voter Registration Application")
        sys.exit()
    else:
        print("***Invalid Input*** Please Enter 'Yes' , 'No' , or 'Quit' :")
        startQuestion = input()

INPUT_ANSWER = False
while INPUT_ANSWER is not True:

    while USER_ADVANCEMENT is not True:
        print("Please Enter User's Last Name: ")
        USER_LAST_NAME = input()
        while USER_ADVANCEMENT is not True:
            print("Is the following correct? \t " , USER_LAST_NAME.upper() , "\nYes or No: ")
            USER_PROMPT_ANSWER = input()
            if USER_PROMPT_ANSWER.upper() == "YES":
                print("Thank you for confirming!")
                USER_ADVANCEMENT = True
            elif USER_PROMPT_ANSWER.upper() == "NO":
                print("Please Reenter Last Name: ")
                USER_ADVANCEMENT = False
                USER_LAST_NAME = input()
            elif USER_PROMPT_ANSWER.upper() == "QUIT":
                print("Goodbye :)")
                sys.exit()
            else:
                print("***Invalid Input*** Please Enter 'Yes' , 'No' , or 'Quit' :")
                USER_ADVANCEMENT = False

    USER_ADVANCEMENT = False
    while USER_ADVANCEMENT is not True:
        print("Please Enter First Name For" , USER_LAST_NAME.upper())
        USER_FIRST_NAME = input()
        while USER_ADVANCEMENT is not True:
            print("Is the following correct? \t " , USER_FIRST_NAME.upper() , "\nYes or No: ")
            USER_PROMPT_ANSWER = input()
            if USER_PROMPT_ANSWER.upper() == "YES":
                print("Thank you for confirming!")
                USER_ADVANCEMENT = True
            elif USER_PROMPT_ANSWER.upper() == "NO":
                print("Please Reenter First Name")
                USER_ADVANCEMENT = False
                USER_FIRST_NAME = input()
            elif USER_PROMPT_ANSWER.upper() == "QUIT":
                print("Goodbye :)")
                sys.exit()
            else:
                print("***Invalid Input*** Please Enter 'Yes' , 'No' , or 'Quit' :")
                USER_ADVANCEMENT = False

    USER_ADVANCEMENT = False
    while USER_ADVANCEMENT is not True:
        print("Please Enter Age For" , USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper())
        USER_AGE = input()
        while USER_ADVANCEMENT is not True:
            print("Is the following correct? \t " , USER_AGE , "\nYes or No: ")
            USER_PROMPT_ANSWER = input()
            if USER_PROMPT_ANSWER.upper() == "YES":
                print("Thank you for confirming!")
                USER_ADVANCEMENT = True
            elif USER_PROMPT_ANSWER.upper() == "NO":
                print("Please Reenter Age: ")
                USER_ADVANCEMENT = False
                USER_AGE = input()
            elif USER_PROMPT_ANSWER.upper() == "QUIT":
                print("Goodbye :)")
                sys.exit()
            else:
                print("***Invalid Input*** Please Enter A Number or 'Quit' :")
                USER_ADVANCEMENT = False

        if USER_AGE.isnumeric():
            USER_ADVANCEMENT = True
        else:
            print(USER_AGE , "Age is not an int")
            USER_ADVANCEMENT = False

        if int(USER_AGE) in range(18, 100):
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper() ,
                "is able to register to vote")
            USER_ADVANCEMENT = True
        elif int(USER_AGE) in range(0, 17):
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper() ,
                "is too young to register to vote")
            USER_ADVANCEMENT = False
        elif int(USER_AGE) > 100:
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper(),
                "is lying about their age :)")
            USER_ADVANCEMENT = False
        elif int(USER_AGE) <= 0:
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper(),
                "has yet to be conceived :)")
            USER_ADVANCEMENT = False
        else:
            print("Invalid Age Given")
            USER_ADVANCEMENT = False

    USER_ADVANCEMENT = False
    while USER_ADVANCEMENT is not True:
        print("Is " , USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper() ,
            " A citizen of the United States?")
        USER_COUNTRY = input()
        while USER_ADVANCEMENT is not True:
            print("Is the following citizenship correct? \t " , USER_COUNTRY ,
                "\nYes or No: ")
            USER_PROMPT_ANSWER = input()
            if USER_PROMPT_ANSWER.upper() == "YES":
                print("Thank you for confirming!")
                USER_ADVANCEMENT = True
            elif USER_PROMPT_ANSWER.upper() == "NO":
                print("Please Reenter Citizenship: ")
                USER_ADVANCEMENT = False
                USER_COUNTRY = input()
            elif USER_PROMPT_ANSWER.upper() == "QUIT":
                print("Goodbye :)")
                sys.exit()
            else:
                print("***Invalid Input*** Please Enter 'Yes' , 'No' , or 'Quit' :")
                USER_ADVANCEMENT = False

        if USER_COUNTRY.upper() == "YES":
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper() ,
                " is able to register to vote")
            USER_ADVANCEMENT = True
        elif USER_COUNTRY.upper() == "NO":
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper() ,
                " is not able to register to vote")
            USER_ADVANCEMENT = False
        else:
            print("***Invalid Citizenship*** Please Enter 'Yes' , 'No' , or 'Quit' :")
            USER_ADVANCEMENT = False

    USER_ADVANCEMENT = False
    while USER_ADVANCEMENT is not True:
        print("Please Enter State of Residence For" , USER_LAST_NAME.upper() ,
            "," , USER_FIRST_NAME.upper())
        print("Please Use State Code... I.E. 'MD'")
        USER_STATE = input()
        while USER_ADVANCEMENT is not True:
            print("Is the following correct? \t " , USER_STATE.upper() , "\nYes or No: ")
            USER_PROMPT_ANSWER = input()
            if USER_PROMPT_ANSWER.upper() == "YES":
                print("Thank you for confirming!")
                USER_ADVANCEMENT = True
            elif USER_PROMPT_ANSWER.upper() == "NO":
                print("Please Reenter State of Residence")
                USER_ADVANCEMENT = False
                USER_STATE = input()
            elif USER_PROMPT_ANSWER.upper() == "QUIT":
                print("Goodbye :)")
                sys.exit()
            else:
                print("***Invalid Input*** Please Enter State of Residence or 'Quit' :")
                USER_ADVANCEMENT = False
        if len(USER_STATE) > 2:
            print(USER_STATE.upper() , "Is an Invalid Length with too many characters")
            USER_ADVANCEMENT = False
        else:
            if USER_STATE.upper() in states:
                USER_ADVANCEMENT = True
            else:
                print(USER_STATE , "Is not a Valid State Code")
                USER_ADVANCEMENT = False

    USER_ADVANCEMENT = False
    while USER_ADVANCEMENT is not True:
        print("Please Enter Zip Code For" , USER_LAST_NAME.upper() ,
            "," , USER_FIRST_NAME.upper())
        USER_ZIP_CODE = input()
        while USER_ADVANCEMENT is not True:
            print("Is the following correct? \t " , USER_ZIP_CODE.upper() , "\nYes or No: ")
            USER_PROMPT_ANSWER = input()
            if USER_PROMPT_ANSWER.upper() == "YES":
                print("Thank you for confirming!")
                USER_ADVANCEMENT = True
            elif USER_PROMPT_ANSWER.upper() == "NO":
                print("Please Reenter Zip Code")
                USER_ADVANCEMENT = False
                USER_ZIP_CODE = input()
            elif USER_PROMPT_ANSWER.upper() == "QUIT":
                print("Goodbye :)")
                sys.exit()
            else:
                print("***Invalid Input*** Please Enter A Number or 'Quit' :")
                USER_ADVANCEMENT = False

        if USER_ZIP_CODE.isnumeric():
            USER_ADVANCEMENT = True
        else:
            print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper() ,
            "Zip Code is not an int")
            USER_ADVANCEMENT = False

        if len(USER_ZIP_CODE) > 5:
            print(USER_ZIP_CODE , "Is too long to be a proper Zip Code")
            USER_ADVANCEMENT = False
        elif len(USER_ZIP_CODE) < 5:
            print(USER_ZIP_CODE , "Is too short to be a proper Zip Code")
            USER_ADVANCEMENT = False
        else:
            USER_ADVANCEMENT = True

    print("Your Voting Registration Application is as follows:")
    print(USER_LAST_NAME.upper() , "," , USER_FIRST_NAME.upper())
    print("Age:" , USER_AGE)
    print("United States Citizen:" , USER_COUNTRY.upper())
    print("State of Residence:" , USER_STATE.upper())
    print("Zip Code:" , USER_ZIP_CODE)
    print("Is All Information Correct?")
    USER_PROMPT_ANSWER = input()
    if USER_PROMPT_ANSWER.upper() == "YES":
        print("Are you positive you would like to register to vote?")
        USER_PROMPT_ANSWER = input()
        if USER_PROMPT_ANSWER.upper() == "YES":
            print("Thank you for registering to vote!")
            INPUT_ANSWER = True
        elif USER_PROMPT_ANSWER.upper() == "NO":
            print("Understood, Restarting Application...")
            USER_ADVANCEMENT = False
        elif USER_PROMPT_ANSWER.upper() == "QUIT":
            print("Goodbye :)")
            sys.exit()
        else:
            print("***Invalid Input*** Please Enter 'Yes' or 'No' :")
            USER_ADVANCEMENT = False
    elif USER_PROMPT_ANSWER.upper() == "NO":
        print("Understood, Running Through Application Again")
        USER_ADVANCEMENT = False
    elif USER_PROMPT_ANSWER.upper() == "QUIT":
        print("Goodbye :)")
        sys.exit()
    else:
        print("***Invalid Input*** Please Enter 'Yes' , 'No' , or 'Quit' :")
        USER_ADVANCEMENT = False
        