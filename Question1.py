#Question 1
#Write a python code for converting integer values to Indian currency notations, without
#using the currency libraries
#Example:
#input: 504678
#output: 5,04,678


import decimal

decimal.getcontext().prec = 2

def currency_format(n):

    # important for test cases like 1000.8000 ==> it converts to 1000.80
    d = decimal.Decimal(str(n))
    if d.as_tuple().exponent < -2:
        s = str(n)
    else:
        s  = '{0:.2f}'.format(n)
    return s    

def find_decimal_idx(n):
    gl = list(n)
    count = 0
    for i in gl:
        count+=1
        if i==".":
            # print("count equals ", count-1)
            return count-1


def get_comma(n):
    gl = list(n)
    count = 0
    for i in gl:
        count+=1
        if i==",":
            # print("count equals ", count-1)
            return count-1            


def listToString(s):
   
    str1 = ""
    return (str1.join(s))            

def convert_to_Indian_currency_notation(n):
    formatted = currency_format(n)
    # print("formateed",formatted)

    # * get values before decimal
    before_decimal = formatted[:find_decimal_idx(formatted)]

    # * after decimal
    after_decimal = formatted[find_decimal_idx(formatted):]
    # print(after_decimal)
    if len(before_decimal)>3:
        # *inserting 3 elements wala comma
        before_decimal_list = list(before_decimal)
        after_decimal_list = list(after_decimal)
        if len(after_decimal_list) > 3:
            raise "Paise value can't be more than 2 decimal digits "
        # print("after decimal list" , after_decimal_list)
        before_decimal_list.insert(-3,",")

        # * after 3 elements wali setting
        total_no_of_commas_required = divmod((len(before_decimal)-3),2)
        no_of_commas_required_post_3 = sum(total_no_of_commas_required) - 1
    

        no_of_elements_post3 = before_decimal_list[:get_comma(before_decimal_list)]
        # print(no_of_elements_post3)
        if len(no_of_elements_post3) >2:
            # print("before_decimal_list:    ",before_decimal_list)
            idex = -4
            for i in range(no_of_commas_required_post_3) :
                idex-=2
                before_decimal_list.insert(idex,",")
                idex-=1
   
        #* append decimals 
        before_decimal_list.extend(after_decimal_list)
        # * list to str
        print("₹",listToString(before_decimal_list))
        
                    
        
        
       
       
    else:
        final_op = "{:,.2f}".format(n)  
        print("₹",final_op)  
        


    
    

    


    
    
    




if __name__ == "__main__":

    while True:
        print("\n\n\n\n   0 to exit \n 1 to go to program \n\n\n\n")
        ip = int(input("Enter Option   "))
        if ip == 0:
            exit()
        elif ip == 1:
            convert_to_Indian_currency_notation(float(input("Enter value   ")))





                                        
    
