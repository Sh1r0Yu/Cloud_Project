# Testing
### Tugas 1:
---
    Docker
    Docker merupakan sebuah platform yang berfungsi dalam pembangunan sebuah
    software yang mampu mengemas dan menjalankan beberapa instance sekaligus.
    
    Container  
    Container memungkinkan developer dalam mengemas komponen komponen software
    seperti kode dependansi dan pustaka agar dapat berjalan pada mesin. 

* Melakukan Instalasi Python
* Melakukan Instalasi Node JS
* Melakukan Instalasi Docker
* Melakukan Koneksi ke Database
*
---
### Tugas 2
* Menjalankan perintah *vnev\Script\active* dan melakukan instalasi Flask *pip install flask*
* melakukan run *python app.py*
* Menampilkan tampilan JSON pada browser dengan menggunakan kode 
    ```
    from flask import Flask, jsonify

    app = Flask(__name__)  # Baris ini membuat instance baru dari aplikasi Flask.

    @app.route('/')
    def home():
        return jsonify({"message": "Hello from Flask!"})  # Fungsi ini
    mendefinisikan rute untuk URL root ('/'). Ketika URL ini diakses, fungsi ini
    mengembalikan respon JSON dengan pesan.

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)  # Baris ini menjalankan
    server pengembangan Flask dengan debugging diaktifkan, mendengarkan pada semua
    alamat IP yang tersedia (host='0.0.0.0') di port 5000. 
    ```
* Melakukan instalasi dengan masuk kedalam virtual enviroment *pip freeze > requirements.txt* dan *pip install -r* untuk menginstall dependesi yang berisi library
    ```
    Flask==3.1.0
    Jinja2==3.1.5
    Werkzeug==3.1.3
    click==8.1.8
    itsdangerous==2.2.0
    ```
---
### Tugas 3
Membuat menjalankan proyek react sederhana pada browser
* melakukan instalasi react dengan kode berikut:
    ```
    cd ../frontend
    npm create vite@latest my-react-app -- --template react
    cd my-react-app
    npm install
    npm run dev
    ```
* Melakukan run *npm run dev* untuk melihat react berjalan dengan benar

* Melakukan perubahan isi konten pada *src/App/jsx/* dengan kode berikut:
    ```
    src/App/jsx dengan menggunakan kode
    import React from 'react';
    function App() {
    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
        <h1>Hello from React + Vite!</h1>
        <p>This is a simple React app built with Vite.</p>
        </div>
    );
    }
    export default App;
    ```
