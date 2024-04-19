from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator


#load the model
model = load_model('model\gender.h5')

#vaildation dataset is required
vaildation_path = "Validation"

#normalized
vaildation = ImageDataGenerator(rescale = 1/255)

vaildation_dataset = vaildation.flow_from_directory(vaildation_path,
                                          batch_size=5,
                                          target_size=(64, 64),
                                          class_mode = "binary")


# evaluate model
score = model.evaluate(vaildation_dataset)


print(vaildation_dataset.class_indices)

# output the result
print("loss(損失函數):", score[0]* 100,"%")
print("accuracy(精確度):", score[1]*100,"%")