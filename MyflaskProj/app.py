import io
import os
import uuid
from urllib.parse import urljoin
from flask import Flask, jsonify, url_for, request, send_file
from flask_cors import CORS
from paddlers.deploy import Predictor
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import pylab

app = Flask(__name__)
CORS(app, resources=r'/*')
UPLOAD_FOLDER = 'static/pic_data'
DOWNLOAD_FOLDER = 'static/dine_data'
TARGET_NUM = 0
file1_name = ''
file2_name = ''
bhjc_i = 0
bhjc_num = 1
dwfl_num = 1
mbjc_num = 1
mbtq_num = 1
coor=''

@app.route('/')
def hello_world():
    return "Hello PaddleRS"


@app.route('/terrain_classification')
def class_function():
    global dwfl_num
    if request.method == 'GET':
        val = request.args.get('chose')
        if val == '4':
            predictor = Predictor("static/object_classification")
            res = predictor.predict("static/pic_data/" + file1_name)
            cm_1024x1024 = res['label_map']
            img = (cm_1024x1024 * 255).astype('uint8')
            # cv2.imwrite("static/done_data/03.png", img)
            print("地物分类进行中")
            # filename = '01.png'
            # filepath = os.path.join(DOWNLOAD_FOLDER, filename)
            filepath = 'static/result/dwfl/' + str(dwfl_num) + '.png'
            dwfl_num += 1
            cv2.imwrite(filepath, img)
            result = turn_web(filepath)
            return result


@app.route('/change_detection')
def paddle():
    global bhjc_num
    if request.method == 'GET':
        val = request.args.get('chose')
        if val == '1':
            predictor = Predictor("static/1024")
            res = predictor.predict(("static/pic_data/" + file1_name, "static/pic_data/" + file2_name))
            # cm_1024x1024 = res['label_map']
            # print(res[0]['label_map'])
            cm_1024x1024 = res['label_map']
            img = (cm_1024x1024 * 255).astype('uint8')
            print("变化检测进行中")
            # filename = '01.png'
            # filepath = os.path.join(DOWNLOAD_FOLDER, filename)
            filepath = 'static/result/bhjc/' + str(bhjc_num) + '.png'
            bhjc_num += 1
            cv2.imwrite(filepath, img)
            result = turn_web(filepath)
            return result


@app.route('/target_extraction')
def get_obj():
    global mbtq_num
    if request.method == 'GET':
        val = request.args.get('chose')
        if val == '3':
            predictor = Predictor("static/get_object")
            res = predictor.predict("static/pic_data/" + file1_name)
            cm_1024x1024 = res['label_map']
            img = (cm_1024x1024 * 255).astype('uint8')
            print("目标提取进行中")
            # filename = '01.png'
            # filepath = os.path.join(DOWNLOAD_FOLDER, filename)
            filepath = 'static/result/mbtq/' + str(mbtq_num) + '.png'
            mbtq_num += 1
            cv2.imwrite(filepath, img)
            result = turn_web(filepath)
            return result


@app.route('/target_detection')
def check_obj():
    global mbjc_num
    global coor
    if request.method == 'GET':
        val = request.args.get('chose')
        per = request.args.get('per')
        print("per=", per)
        per = eval(per) / 100
        if val == '2':
            predictor = Predictor("static/check_object")
            result = predictor.predict("static/pic_data/" + file1_name)
            plt.close()
            img = plt.imread("static/pic_data/" + file1_name)
            # height, width, channels = img.shape
            for i in range(len(result)):
                # 下面的这个阈值可以自己调节
                # TODO 嘿嘿嘿
                if result[i]['score'] > per:
                    a = result[i]['bbox'][0]
                    b = result[i]['bbox'][1]
                    c = result[i]['bbox'][2]
                    d = result[i]['bbox'][3]
                    coor = str(a) + "," + str(b)+"," + str(a + c) + "," + str(b + d)
                    plt.plot((a, a + c), (b, b), 'r')
                    plt.plot((a + c, a + c), (b, b + d), 'r')
                    plt.plot((a + c, a), (b + d, b + d), 'r')
                    plt.plot((a, a), (b + d, b), 'r')
                    print("左上坐标" + str(a) + "," + str(b))
                    print("右上坐标" + str(a + c) + "," + str(b))
                    print("左下坐标" + str(a) + "," + str(b + d))
                    print("右下坐标" + str(a + c) + "," + str(b + d))

            # cm_1024x1024 = result['label_map']
            # img = (cm_1024x1024 * 255).astype('uint8')
            plt.imshow(img)
            plt.xticks([])  # 去掉横坐标值
            plt.yticks([])  # 去掉纵坐标值
            plt.show()
            pylab.show()
            plt.savefig('static/result/mbjc/' + str(mbjc_num) + '.png',bbox_inches='tight', pad_inches = -0.1)  # 保存图片
            print("目标检测进行中")
            # filename = '01.png'
            # filepath = 'static/result/mbjc/' + str(mbjc_num) + '.png'

            # plt.savefig(filepath)
            # filepath = 'static/done_data/03.png'
            # cv2.imwrite(filepath, img)
            result = turn_web('static/result/mbjc/' + str(mbjc_num) + '.png')
            mbjc_num += 1
            print("正在进行中11111")
            return result

# 变化检测的上传文件模块
@app.route('/pic', methods=['POST'])  # 实现上传图片到pic_data
def pic_doing():
    global file1_name
    global file2_name
    global bhjc_i
    file = request.files.get('file')
    filename = random_filename(file.filename)
    if bhjc_i % 2 == 0:
        file1_name = filename
    else:
        file2_name = filename
    print(filename)
    bhjc_i = bhjc_i + 1
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(os.path.join(app.root_path, filepath))
    file_url = urljoin(request.host_url, filepath)
    return file_url

# 其他三个的上传文件模块
@app.route('/pic_3', methods=['POST'])  # 实现上传图片到pic_data
def pic_3doing():
    global file1_name
    file = request.files.get('file')
    filename = random_filename(file.filename)
    print(filename)
    file1_name = filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(os.path.join(app.root_path, filepath))
    file_url = urljoin(request.host_url, filepath)
    return file_url

@app.route('/coor', methods=['POST'])
def tocoor():
    return coor

def turn_web(filepath):
    # filename = file_name;
    # filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, 'rb') as f:
        a = f.read()
    img_stream = io.BytesIO(a)
    img = Image.open(img_stream)
    img_byte = io.BytesIO()
    img.save(img_byte, format='PNG')
    img_byte = img_byte.getvalue()
    print("正在检测中,请稍等...")
    return img_byte


def random_filename(filename):
    ext = os.path.splitext(filename)[-1]
    return uuid.uuid4().hex + ext


if __name__ == '__main__':
    app.run()
