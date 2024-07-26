from twilio.rest import Client

account_sid = 'AC3b3c5bfe25349fc0d13619377c3c11c1'
auth_token = '9dcf2e35314b8c740d5d9d555bda6bf1'
client = Client(account_sid, auth_token)

def sendSms():
    message = client.messages.create(
        from_='+17623095671',
        body='Alert!! Intrusion Detected.',
        to='+18777804236'
    )
    
    print(message.sid)

sendSms()
