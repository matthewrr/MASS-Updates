from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

employees = {}
events = {}

@csrf_exempt
def sms_response(request):
    
    account_sid = "ACde33cfc07cb9884468e076bdf25cb9ed"
    auth_token = "fdbbbc36113196c9abbb553bba9473d9"
    client = Client(account_sid, auth_token)
    twilio_number = "+15092837927"
    
    sender = request.POST.get('From', '')
    (cmd, body) = request.POST.get('Body', '').split(maxsplit=1)
    
    if employees[sender]['active'] == True:
        if employees[sender]['admin'] == True:
            phone_all = [phone_number for phone_number in employees.keys()]
            if cmd == 'message':
                for phone_number in phone_all:
                    client.messages.create(
                        to=phone_number,
                        from_=twilio_number,
                        body=body
                    )
            else:
                client.messages.create(
                    to=sender,
                    from_=twilio_number,
                    body='Error: you must begin text with "message".'
                )
        else:
            if cmd == 'schedule': pass
            elif cmd == 'contact': pass
            else:
                client.messages.create(
                    to=sender,
                    from_=twilio_number,
                    body='Error: not a correct command.'
                )
    else:
        client.messages.create(
            to=sender,
            from_=twilio_number,
            body='Error: number not found.'
        )
    return HttpResponse('Hello! How did you get here? ;)')