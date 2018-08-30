from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "MMM"
# Your Auth Token from twilio.com/console
auth_token  = "NNNN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+10000000", 
    from_="+1000001",
    body="Hello from Python! Ding")

print(message.sid)
