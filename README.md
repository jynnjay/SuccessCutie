# SuccessCutie

//gumamit ng Git Bash (https://git-scm.com/downloads) para ma set up ang mga Command Lines na ito isa isa.

git clone https://github.com/jynnjay/SuccessCutie.git

cd SuccessCutie

py -m venv venv

. venv/Scripts/activate

pip install -r requirements.txt

export FLASK_ENV=development                          
// set FLASK_ENV=development (for Windows Powershell)

flask run


---
//Kapag bubuksan ulet ang server hindi na kailangan gawin lahat ang nasa taas

cd SuccessCutie

. venv/Scripts/activate

export FLASK_ENV=development                          
// set FLASK_ENV=development (for Windows Powershell)

flask run

copy the http://127.0.0.1:5000/login and paste sa browser

---
//Kapag gustong makita sa Internet gumamit ng ngrok! (or kung alin mang tunnel host na katulad ng ngrok. https://www.google.com/amp/s/www.softwaretestinghelp.com/ngrok-alternatives/amp/)

//https://ngrok.com/

//i download ang nrok pagtapos gumawa ng sariling account

//sa CMD or terminal ng ngrok ilagay ito isa isa:

ngrok authtoken {} // palitan ang curly braces ng sarili mong ngrok authoken

ngrok http 5000

[Capture](https://user-images.githubusercontent.com/85058488/162574693-2355ee3a-6b8a-4c55-88d4-e32303ff454c.PNG)

//i copy and paste ang naka highlight na https:// sa iyong browser and dagdagan ng /login





*******



Development mode
TO DO (Jay-Ann, Joshua, Mark Louise): **FOR THE MONTH OF MAY** 

* Limit log in attempts to 3 only. This would prevent **brute force attack**.
 _Options:_ > If the attemptor reach the limit, his/her IP address will be block for 24 hours.
            > If the attemptor reach the limit, his/her account will be lock (just like in banking account app, if you ever experience that). He/She can only reactivate it through his/her email account through reset password link.
* _(Optional)_ Do OTP Verification through **SMS** (highly recommended) or Email when logging in. This is only optional because OTP through SMS might not be free, limited trial only.
* Work with multiple VideoCapture streaming through different cameras. We only just did 1 VideoCapture yet.
* When working with Raspbery Pi, we can use the picamera module. However, we don't have the resources so just focus on how we will execute the video stream when multiple camera is open and connected.
* Sanitize the coding especially the forms to avoid the **SQL Injection attack**.
* Prevent the **DDoS attack**. (We must research how to do this so we can know how to do it.)
* Do zooming in or make the video stream clickable to full screen. This will be coded through JS.
* Check if the URL could be vulnerable to path traversal.
  Path traversal is when the https://example.com/login?a3dj9d7?admin=user17pnml53?pw=ad7sjp9202h1ak57j2 can be access without the authentication (login) or access the 
  specific sensitive directory directly through the URL.


IMPORTANT
* We need to know how we will implement the admin side and client side coding. We must learn thoroughly how the codes work and how we will organize the code. 
* Sign up page won't be available in production mode.


