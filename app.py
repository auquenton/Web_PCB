from pyexpat import model
from flask import Flask, jsonify, request, render_template, redirect, url_for
import torchvision.transforms as transforms
transforms.Resize
import torch.nn.functional as F
from torchvision import models
import torch.nn as nn
from model import run,build_model
from PIL import Image
import numpy as np
import torch
import io, re, os



app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
PKPcb_model = build_model()
print("======= PKPCB_model_build_done ======")
DeepPcb_model = build_model('./models/DeepPCB.pt')
print("======= DeepPCB_model_build_done ======")



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    file.save('./static/img/upload/inp.jpg')
    cloud_cover = request.values.get( "cloud-cover")
    print(cloud_cover)
    print(cloud_cover)
    if(cloud_cover=='PK_PCB'):
        run(PKPcb_model)
        print("====== Original PCB ======")
    if(cloud_cover=='Deep_PCB'):
        run(DeepPcb_model)
        print("====== Binarization PCB ======")
    
    return jsonify({'outdir': url_for('static', filename='img/result/out.jpg')})


@app.route('/result_original_PCB')
def result_original_PCB():
    return render_template('index_1.html')


@app.route('/result_DeepPCB')
def result_DeepPCB():
    return render_template('index_2.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
