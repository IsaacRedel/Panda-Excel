import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxx"
client = Client(account_sid, auth_token)

# open excel file
list_mounth = ['january', 'february', 'march', 'april', 'may', 'june'] 

for mounth in list_mounth:
    sale_list = pd.read_excel(f'{mounth}.xlsx')
    if (sale_list['Sales'] > 55000).any():
        seller = sale_list.loc[sale_list['Sales'] > 55000, 'Seller'].values[0]
        sale =  sale_list.loc[sale_list['Sales'] > 55000, 'Sales'].values[0]
        
        print(f'In mouth {mounth} I finded someone who sold over 55000. Seller: {seller}, Sales: {sale}')
        

# send the sms for your cellphone
message = client.messages.create(
    to = "+xxxxxxxxx", # the number to send the sms
    from_ = "xxxxxxx", # your twilio number here
    body= f'In mouth {mounth} I finded someone who sold over 55000. Seller: {seller}, Sales: {sale}')

print(message.sid)

