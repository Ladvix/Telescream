pkg update && pkg upgrade
pkg install git python openssl rust
git clone https://github.com/Ladvix/Telescream
cd Telescream
pip install -r requirements.txt
python main.py
