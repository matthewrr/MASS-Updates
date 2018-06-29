MASS Updates
============

Messaging App for Sending Schedule Updates (MASS Updates) is a Twilio-based texting application compatible with AWS Lambda. It allows employers to send en-masse SMS alerts when schedule updates are complete. Employees can view their individual schedule via SMS text.

Usage
--------
Employee and manager texts sent to their company's Twilio SMS number initiates the following sequence:

 1. Validate sender phone number is attached to an active employee/manager profile.
 2. Check whether phone number is authorized for manager privileges.
 3. Parse message. Treat first word as command and remaining text as optional argument.

### Admin/Managers:
Users with admin privileges can text the company's Twilio number and have a corresponding SMS text individually sent to all active employees. The first word of the user's text acts as the user command. If the user's text is sent without additional information, all employees will receive an SMS text with pre-configured content (e.g. 'Schedules have been updated. Please reach out if you're unavailable to work for any shift.'). Additional text can be passed as an optional argument to supersede the default message.

 - **Default Update**: `'message'`
 - **Custom Update**: `'message <custom message goes here>'`

### Employees:
Employees can receive their work schedule via SMS text by sending a command to the company's Twilio number. A separate command will forward their manager(s) contact information.

 - **View Schedule**: `'schedule'`
 - **Manager Contact Information**: `'contact'`

Background
--------
MASS Updates was originally built to assist a major food and beverage vendor at a large event center. Prior to the app, employee schedules were only available in-person at the place of employment itself. When employee schedules were updated or event information changed (such as a concert changing its start time), managers would individually text the 100+ employees. Twilio offered an efficient and inexpensive solution. Serverless hosting on AWS Lambda ensures marginal operating costs.

License
--------
Twilio-SMS is licensed under the [MIT](#) license.  
Copyright &copy; 2018, Matthew R. Rivera