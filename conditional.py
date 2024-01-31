# loyalty_customer = True
# total_bill = 124

# if loyalty_customer and total_bill > 100:
#     #give 20% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 20
# elif total_bill > 100:
#     #give 10% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 10
# else:
#     #sorry no discount, 5% service charge applied.
#     print('Sorry, no discount ...')

# print('Total Bill: ', float(total_bill))


http_status = 501

if http_status == 200 or http_status == 201:
    print("Success")
elif http_status == 400:
    print("Bad Request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500 or http_status == 501:
    print("Server Error")
else:
    print("Unknown")

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")


# parameter = "Geeksforgeeks"

# match parameter:

# 	case first : 
# 		do_something(first)
	
# 	case second : 
# 		do_something(second)
		
# 	case third : 
# 		do_something(third)
# 		.............
# 		............
# 	case n :
# 		do_something(n)
# 	case _ : 
# 		nothing_matched_function()
		

