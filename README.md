# SuccessCutie

//gumamit ng Git Bash (https://git-scm.com/downloads) para ma set up ang mga Command Lines na ito isa isa.

git clone https://github.com/jynnjay/SuccessCutie.git

cd SuccessCutie

py -m venv venv

. venv/Scripts/activate

pip install -r requirements.txt

export FLASK_ENV=development  // set FLASK_ENV=development (for Windows Powershell)

flask run


---
//Kapag bubuksan ulet ang server hindi na kailangan gawin lahat ang nasa taas

cd SuccessCutie

. venv/Scripts/activate

export FLASK_ENV=development  // set FLASK_ENV=development (for Windows Powershell)

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
