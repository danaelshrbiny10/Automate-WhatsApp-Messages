"""Send WhatsApp messages to contacts and groups."""

import pywhatkit as kit


"""Send a message to a contact on WhatsApp.
   Syntax: phone number with country code, message, hour and minutes.
   True:   indicates that we want to close the tab after 2 seconds.
   kit.sendwhatmsg(
        'country code + phone number',
        'message',
        hour,
        min,
        True, 
        time 'x' in sec to close
    )"""

kit.sendwhatmsg('+20xxxxxxx', 'Message', 18, 55,True, 2)



"""Send a message to a group on WhatsApp.
   Syntax: group id, message, hour and minutes.
   kit.sendwhatmsg_to_group(
        'group id',
        'message',
        hour,
        min
    )"""

kit.sendwhatmsg_to_group("write-id-here", "Message", 19, 2)