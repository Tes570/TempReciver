import smbus

#import firebase
#from firebase import db
from firebase import firebase as Fire


#fireLink = firebase.FirebaseApplication('https://ee175b21.firebaseio.com/')
fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com/')

#firebase.auth()
#db = firebase.database()

fireLink.put('EE175b21/user/pi', 'cTemp', str(14))
fireLink.put('EE175b21/user/pi', 'Hight', str(10))

result = fireLink.get('EE175b21/user/pi', None)
#result = ref.child('EE175b21/user/pi').get()

print(result)
