from flask import Flask, g, render_template, request, redirect, session, url_for
import pickle  
import sklearn  
import matplotlib.pyplot as plt
import numpy as np            # numpy==1.19.3  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():       
    return render_template('index.html')
    
@app.route('/proses', methods=['POST', 'GET'])
def proses():
        
    if request.method =='POST' :

        with open('model2.pkl', 'rb') as r:  
         model = pickle.load(r) 
        
        depan = str(request.form['depan'])
        sta_bangunan = int(request.form['sta_bangunan'])  
        sta_lahan = int(request.form['sta_lahan'])  
        luas_lantai = int(request.form['luas_lantai'])  
        lantai = int(request.form['lantai'])  
        dinding = int(request.form['dinding'])  
        kondisi_dinding = int(request.form['kondisi_dinding'])  
        atap = int(request.form['atap'])  
        kondisi_atap = int(request.form['kondisi_atap'])  
        sumber_airminum = int(request.form['sumber_airminum'])
        cara_peroleh_airminum = int(request.form['cara_peroleh_airminum'])
        ibu_hamil = int(request.form['ibu_hamil'])
        anak_sekolah = int(request.form['anak_sekolah'])
        balita = int(request.form['balita'])
        lansia = int(request.form['lansia'])

        datas = np.array((sta_bangunan,sta_lahan,luas_lantai,lantai,dinding,kondisi_dinding,atap,kondisi_atap,sumber_airminum,cara_peroleh_airminum,ibu_hamil,anak_sekolah,balita,lansia))  
        datas = np.reshape(datas, (1, -1))  
   
        Kelayakan = model.predict(datas)  
    
        return render_template('hasil.html', finalData=Kelayakan, nama=depan) 
    else:
        return render_template('proses.html')
@app.route('/about')
def about():
    
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)