

def main():
    try:
        x = int(input("What is X? "))
        y = int(input("What is Y? ")) #gets user input x and y as integers
        
        fraction = x / y #saves x divided by y as a variable called fraction

        if (x>y): #checks if x is greater than y
         print ("x can't be greater than y")
   
        else:
            percentage = convert(fraction) #calculates the percentage using the fraction
            result = gauge(percentage) #determines whether F,E or a rounded perctentage willl be given
            print(result) #prints the final result



    except ValueError:
        print("error, type an integer") # the error message will occur if anything but an integer is printed
         
    except ZeroDivisionError:
        print("error, Cannot divide by zero.") # error is printed if integer is divided by 0
        
        
   


        


def convert(fraction):
    return round(fraction*100) #returns a number that is a fraction into a rounded percentage




def gauge(percentage):

    if percentage <= 1: # if percentahe is equal to or less than 1 E is printed
        return "E"
    elif percentage >= 99: # if percentage is equal to or more than 99 then F is printed
        return "F"
    else:
        return f"{percentage}%" # any integer between that is printed as a percnetage




if __name__ == "__main__": 
    main() # runs the main part of the code












