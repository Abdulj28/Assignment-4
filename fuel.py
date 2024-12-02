

def main():
    try:
        x = int(input("What is X? "))
        y = int(input("What is Y? "))
        
        fraction = x / y

        if (x>y):
         print ("x can't be greater than y")
   
        else:
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)



    except ValueError:
        print("error, type an integer")
         
    except ZeroDivisionError:
        result = "error, Cannot divide by zero."
        print(result)


        


def convert(fraction):
    return round(fraction*100)




def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()













