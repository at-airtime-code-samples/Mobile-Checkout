#Import the Africa's Talking SDK
import africastalking

#Set up your credentials
username = "sandbox"
api_key = "54a3fb2f30c16e6b1b4df478b5f4395c1705ac253a0b5ecd1a85f9ed296ca18b"

#Initialize the SDK
africastalking.initialize(username, api_key)

#Define the Payment service
check_out = africastalking.Payment

#Set your product name
product_name = "DUKA"

#Set the phone number you want and set it to the international format
phone_number = "+254727545805"

#Set the 3 letter ISO currency code and checkout amount
currency_code = "KES"
amount = 100.0

#You can add in your own metadata which will be resent back to you
#For the final payment notification
metadata = {
    "agentId": "",
    "productId": ""
}

#The provider channel that the payment will be initiated from
provider_channel = "123445"

#Time to send and we'll handle the rest
try:
    res = check_out.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
    print(res)
except Exception as e:
    print(f"Houston we have a problem {e}")