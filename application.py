from flask import *
application = Flask(__name__)
userdetails = {}
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://orange-64af5-default-rtdb.firebaseio.com/"})


@application.route('/',methods=["GET","POST"])
def hello_world():
   fdb= db.reference("/")
   global userdetails
   if(request.form):
      btnpressed = request.form['btn']
      if(btnpressed  == 'Login'):
         return render_template("SignupLogin.html")
      
      if(btnpressed == 'SignupSubmit'):
         seid =  request.form['Semail']
         spwd =  request.form['Spassword']
         scpwd = request.form['Scpassword']
         fdb.update({"Email":seid,
                        "Password":spwd,
                        "Confimpwd":scpwd,
                         })
         return render_template("SignupLogin.html" )

      if(btnpressed == 'LoginSubmit'):
         userdetails = fdb.get()
         leid =  request.form['loginemail']
         lpwd =  request.form['lpassword']
         seid = userdetails['Email']
         spwd =  userdetails['Password']
         if((seid == leid) and (spwd == lpwd)):
            return render_template("index.html" )
         else:
            return render_template("SignupLogin.html",var ="Invalid Details" )
      
   return render_template("index.html")

if __name__ == '__main__':
    application.run(debug = True,port = 5057)
    
