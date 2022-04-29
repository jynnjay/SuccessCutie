# SuccessCutie

git clone https://github.com/jynnjay/SuccessCutie.git

cd IAS

py -m venv venv

. venv/Scripts/activate

pip install -r requirements.txt

export FLASK_ENV=development  // set FLASK_ENV=development (for Windows Powershell)

flask run


---
Kapag bubuksan ulet ang server hindi na kailangan gawin lahat ang nasa taas

cd IAS

. venv/Scripts/activate

export FLASK_ENV=development  // set FLASK_ENV=development (for Windows Powershell)

flask run

copy the http://127.0.0.1:5000/ and paste sa browser

---
Kapag gustong makita sa Internet gumamit ng ngrok! 
https://ngrok.com/

i download ang nrok pagtapos gumawa ng sariling account

ngrok authtoken {} // ilagay sa curly braces ang sarili mong ngrok authoken

ngrok http 5000

[Capture](https://user-images.githubusercontent.com/85058488/162574693-2355ee3a-6b8a-4c55-88d4-e32303ff454c.PNG)

i copy and paste ang naka highlight na https:// sa iyong browser
