"""
 Object Detection (On Image) From TF2 Saved Model
=====================================
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

   # Suppress TensorFlow logging (1)
import tensorflow as tf
import cv2
import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings



PATH_TO_MODEL_DIR = r'D:/ABPlastomech Inernship/object Detection/content/training_demo/exported_models/my_model'

# PROVIDE PATH TO LABEL MAP
PATH_TO_LABELS = r'D:/ABPlastomech Inernship/object Detection/content/training_demo/annotations/label_map.pbtxt'

# PROVIDE THE MINIMUM CONFIDENCE THRESHOLD
MIN_CONF_THRESH = float(0.60)

# LOAD THE MODEL


PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"

print('Loading model...', end='')
start_time = time.time()

# LOAD SAVED MODEL AND BUILD DETECTION FUNCTION
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

# LOAD LABEL MAP DATA FOR PLOTTING

category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)


warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

loc='E:/NewDjangoProjects/object detection/objectDetection/static/images/'

def detect(file):
  print("file List objectdetection")
  print(file)
  image = cv2.imread(loc+f"{file}")#{loc}
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image_expanded = np.expand_dims(image_rgb, axis=0)
  # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
  input_tensor = tf.convert_to_tensor(image)
  # The model expects a batch of images, so add an axis with `tf.newaxis`.
  input_tensor = input_tensor[tf.newaxis, ...]
  # input_tensor = np.expand_dims(image_np, 0)
  detections = detect_fn(input_tensor)
  # All outputs are batches tensors.
  # Convert to numpy arrays, and take index [0] to remove the batch dimension.
  # We're only interested in the first num_detections.
  num_detections = int(detections.pop('num_detections'))
  detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
  detections['num_detections'] = num_detections
  # detection_classes should be ints.
  detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
  image_with_detections = image.copy()
  # SET MIN_SCORE_THRESH BASED ON YOU MINIMUM THRESHOLD FOR DETECTIONS
  viz_utils.visualize_boxes_and_labels_on_image_array(
        image_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        min_score_thresh=0.20,
        agnostic_mode=False)
  if category_index == [1]:
    print("Success")
    
  print(category_index[1])
  print (category_index)
  print('Done')
  image_with_detections = cv2.resize(image_with_detections, (540, 340))
  # DISPLAYS OUTPUT IMAGE
  # cv2.imshow("window",image_with_detections)
  # cv2.waitKey(0)
  # CLOSES WINDOW ONCE KEY IS PRESSED
  os.chdir(loc)
  if not os.path.exists('results'):
    os.makedirs('results')
  os.chdir(loc+'results/')
  fileName=f"result-{file}"
  cv2.imwrite(fileName,image_with_detections)

  





    

