
### Nama   : Shello Juliano Julius
### NIM    : 10221041
### GitHub : 
---
### Tugas 2 Membuat API Sederhana dengan Flask

#### 1.![Screenshot](IMG/Screenshot%202025-02-28%20083326.png)
Berikut merupakan direktori terbaru.

#### 2.![Screenshot](IMG/Screenshot%202025-02-26%20101641.png)
Pada tampilan screenshot menunjukan bahwa virtual environment berhasil dibuat dan diaktifkan dan siap digunakan untuk menjalankan perintah Flask.

#### 3.![Screenshot](IMG/Screenshot%202025-02-26%20101736.png)
Pada Tampilan screenshot akan di lakukannya perintah *pip install flask* yang dimana akan menginstall flask beserta package pcakgae yang diperlukan agar flask dapat berjalan semestinya.

#### 4.![Screenshot](IMG/Screenshot%202025-02-26%20102119.png)
Selanjutnya melakukan run *python app.py* yang dimana menunjukan bahwa flask berjalan dengan semestinya. 

#### 5.![Screenshot](IMG/Screenshot%202025-02-26%20102336.png)
Setelah melakukan run pilih salah satu link address yang di berikan maka pada browser akan memunculkan tampilan JSON

```
from flask import Flask, jsonify

app = Flask(__name__)  # Baris ini membuat instance baru dari aplikasi Flask.

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})  # Fungsi ini mendefinisikan rute untuk URL root ('/'). Ketika URL ini diakses, fungsi ini mengembalikan respon JSON dengan pesan.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Baris ini menjalankan server pengembangan Flask dengan debugging diaktifkan, mendengarkan pada semua alamat IP yang tersedia (host='0.0.0.0') di port 5000.
```

#### 6.![Screenshot](IMG/Screenshot%202025-02-26%20103211.png)
Terakhir membuat file requirements.txt untuk menginstal seluruh dependensi

Sebelum menginstall dependensi pertana perlu masuk kedalam virtual enviroment terlebih dahulu lalu menjalankan perintah *pip freeze > requirements.txt*

Setelah itu file requirements.txt akan terisi secara otomatis
dengan library yang tersedia
``` 
Flask==3.1.0
Jinja2==3.1.5
Werkzeug==3.1.3
click==8.1.8
itsdangerous==2.2.0
```
Pada terminal Jalankan *pip install -r requirements.txt* maka seluruh library yang tersedia akan diinstall secara otomatis
    


