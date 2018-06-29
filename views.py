from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client

employees = {}
events = {}

responses = {
    'admin_success': "Success! Your message was just sent to all active employees.",
    'admin_unknown_command': "Error: this is an incorrect command. So send the default message to all employees, please respond with 'message'. To override with a custom text to all employees, please respond with 'message' followed by the custom message you want to send.",
    'employee_unknown_command': "Error: this is an incorrect command. Please respond with 'schedule' to receive your work schedule or 'contact' to view your managers' contact information.",
    'unknown_number': "Error: this phone number is not associated with an active employee. Please reach out to your manager if you believe this is an error."
}

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
                    client.messages.create(to=phone_number,from_=twilio_number,body=body)
                client.messages.create(to=sender,from_=twilio_number,body=responses['admin_success'])
            else: client.messages.create(to=sender,from_=twilio_number,body=responses['admin_unknown_command'])
        else:
            if cmd == 'schedule': pass
            elif cmd == 'contact': pass
            else: client.messages.create(to=sender,from_=twilio_number,body=responses['employee_unknown_command'])
    else: client.messages.create(to=sender,from_=twilio_number,body=responses['unknown_number'])
    return HttpResponse('Hello! How did you get here? ;)')