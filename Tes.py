import smbus
import time
from firebase import firebase

firebase= firebase.FirebaseApplication('https://ee175b21.firebaseio.com/')

result = firebase.post('EE175b21', {'cTemp':str(12),'ftemp':str(24), 'humidity':str(48)})
print(result)