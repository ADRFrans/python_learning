# prompt the users sees
prompt = "enter 2 seperate numbers"

# empty ints 
sum = 0
dif = 0
pro = 0
quo = 0

# empty list
numbers_list = []

def get_input(p):
    # While true do this until each portion is satisfied
    while True:
        try:
            #user prompt
            print(p)
            #split input into a list 
            user_inputs = input().split()
            # if the list doesn't have 2 entrys restart
            if  len(user_inputs) == 2:
                #check and see if entrys are ints if not restart
                user_inputs = [int(i) for i in user_inputs]
                #set the list 
                numbers_list = user_inputs
                
                # some math using the indexs
                sum = user_inputs[0] + user_inputs[1]
                dif = user_inputs[0] - user_inputs[1]
                pro = user_inputs[0] * user_inputs[1]

                print(f"Sum of numbers:{sum}")
                print(f"Difference: {dif}")
                print(f"Product: {pro}")

                #Guard to throw error if user entered a 0 
                if user_inputs[1] == 0:
                    print("cannot give Quotient")
                else:
                    quo = user_inputs[0] / user_inputs[1]
                    print(f"Quotient: {quo}")
                return numbers_list
            else:
                #if anything fails above print
                print("Invalid")
        except ValueError:
            print("Invalid input.")


get_input(prompt)