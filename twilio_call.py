from twilio.rest import Client 
import secrets 

account_sid = secrets.account_sid
auth_token = secrets.auth_token
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:' + secrets.From_Number,  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+60176306862' 
                          ) 
 
print(message.sid)