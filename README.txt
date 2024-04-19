Project介紹請讀Github內容

使用由Ashutosh Chauhan提供之Dataset(連結請看檔案Dataset_url)

照片請裁切保留頭部，模型可以收任意大小的照片，因為我有寫一個自動改照片大小函式，但模型不會看男女生的身體:(

以及在model資料夾有兩個模型，一個是64x64，128x128輸入，但二者似乎差異不大，若想使用請打開main_128.py

如果有多張照片想一次預測，請把照片放在test，並使用main.ipynb

main.py是主要的程式，model_training可以給你用訓練模型(需要dataset放置在目錄)，evaluate_model可以評估你的模型性能(一樣需要dataset)

若想使用main需要用到以下資料包(In order to use main.py must install following package)

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

Project Introduce please read github content

Dataset provided by Ashutosh Chauhan(Link in Dataset_url)

Please crop the images to only include the head, model can receive any size of image, since i writed a function to resize image, the model does not differentiate between male and female bodies

There are two types of models in the model folder, one is 64x64 input second is 128x128 input, both models produce similar results, if you want to use 128x128 input, please use main_128.py

If you want to predict multiple images at once, please use main.ipynb

Main.py is main program, model_training is model training(Dataset required in main folder), evaluate_model allow you see the result(again dataset required)