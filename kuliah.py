from twilio.rest import Client 
from identity import account_sid, auth_token, botcaller, yournum, yourwa, botwa

client = Client(account_sid, auth_token) 
def ads():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*ADS WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
    
def adscall():
    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=yournum,
                        from_=botcaller
                    )

    print(call.sid)
   
def rpl():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*RPL WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
    
def rplcall():
    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=yournum,
                        from_=botcaller
                    )

    print(call.sid)
    
def imk():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*IMK WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
 
def pok():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*POK WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
    
def ppw():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*PEPEW WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
    
def ppwcall():
    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=yournum,
                        from_=botcaller
                    )

    print(call.sid)
   
def halo():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*HALOOO*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)

def halocall():
    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=yournum,
                        from_=botcaller
                    )

    print(call.sid)
 
def komdat():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*KOMSAT WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
    
def metnum():
    message = client.messages.create( 
                              from_=botwa,  
                              body='*METNUM WOI*',      
                              to=yourwa 
                          ) 
 
    print(message.sid)
    
def libur():
    message = client.messages.create( 
                              from_=botwa,  
                              body='enjoy your holidayyy',      
                              to=yourwa 
                          ) 
 
    print(message.sid)