# -*- coding: utf-8 -*-
import os           
from tqdm import trange   

def get_filename(file_dir):
    filename = None
    for root, dirs, files in os.walk(file_dir):
        filename = files
    return filename

def main():
    html_path = './templates/index_2.html'
    #open html file
    f = open(html_path,'w')
    head_message = """<!DOCTYPE html>
<html>
  <head>
    <title>Experiment = rice1_unet8_patch16gan_bce_ssim_lambda10, Phase = test, Epoch = latest</title>
  </head>
  <center>
    <body>"""
    f.write(head_message)
    f.write('\n')
    file_path = './static/img/Deep_PCB'  
    filenames = get_filename(file_path)
    for i in trange(len(filenames)):
        if(i%3==0):
            num = filenames[i].split('_')[0]
            body_message = """    <h3>%s</h3>
    <table border="1" style="table-layout: fixed;">
      <tr>
        <td halign="center" style="word-wrap: break-word;" valign="top">
          <p>
            <a href="{{url_for('static', filename='img/Deep_PCB/%s_img.jpg')}}">
              <img src="{{url_for('static', filename='img/Deep_PCB/%s_img.jpg')}}" style="width:256px">
            </a><br>
            <p>Img</p>
          </p>
        </td>
        <td halign="center" style="word-wrap: break-word;" valign="top">
          <p>
            <a href="{{url_for('static', filename='img/Deep_PCB/%s_label.jpg')}}">
              <img src="{{url_for('static', filename='img/Deep_PCB/%s_label.jpg')}}" style="width:256px">
            </a><br>
            <p>Label</p>
          </p>
        </td>
        <td halign="center" style="word-wrap: break-word;" valign="top">
          <p>
            <a href="{{url_for('static', filename='img/Deep_PCB/%s_pred.jpg')}}">
              <img src="{{url_for('static', filename='img/Deep_PCB/%s_pred.jpg')}}" style="width:256px">
            </a><br>
            <p>Pred</p>
          </p>
        </td>
      </tr>
    </table>"""%(num,num,num,num,num,num,num)
            f.write(body_message)
            f.write('\n')
    tail_message = """    </body>
  </center>
</html>"""
    f.write(tail_message)
    f.close()



if __name__ == '__main__':
    main()
