### Egnlish version in blow

# 這是一個基於卷積神經網路(CNN)，透過大量人臉圖片訓練，給予人臉圖片識別，並推測性別。並且透過GUI(Tkinter)介面給予使用者方便使用

![tutorial](https://github.com/z23788677/Application-of-CNN-for-gender-prediction-with-GUI/assets/85629602/8e0bcf37-e02b-433b-a2f2-df42d20c3c5e)

使用由Ashutosh Chauhan提供之Dataset(連結請看檔案Dataset_url)

照片請裁切保留頭部，模型可以收任意大小的照片，因為我有寫一個自動改照片大小函式，但模型不會看男女生的身體:(

如果有多張照片想一次預測，請把照片放在test，並使用main.ipynb

main.py是主要的程式。在model_training資料夾model_training.py可以給你用訓練模型(需要dataset放置在目錄)，evaluate_model.py可以評估你的模型性能(一樣需要dataset)

若想使用main需要用到以下資料包
(In order to use main.py must install following package)

pip install opencv-python 
(這是cv2,That's cv2)

pip install tesnorflow
(這資料包很大, This package is large)

pip install Pillow
pip install numpy

若想使用model_training.py需要下列資料包(In order to use model_training.py must install following package)
pip install opencv-python 
pip install matplotlib
pip install numpy
pip install tesnorflow


# This is a project based on Convolutional Neural Networks (CNN), trained using a large dataset of facial images, for gender prediction. Additionally, it provides users with ease of use through a GUI (Tkinter) interface

Dataset provided by Ashutosh Chauhan(Link in Dataset_url)

Please crop the images to only include the head, model can receive any size of image, since i writed a function to resize image, the model does not differentiate between male and female bodies

If you want to predict multiple images at once, please use main.ipynb

Main.py is main program, model_training is model training(Dataset required in main folder), evaluate_model allow you see the result(again dataset required)

In order to use main.py must install following package in upper
