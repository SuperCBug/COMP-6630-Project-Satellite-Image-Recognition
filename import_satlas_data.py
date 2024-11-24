import os
import cv2

# Data Path: Pathing to our selected project data
# Label Path: Pathing to satlas' label data
def import_satlas_data(data_path="./Project Data/",label_path="./Project Labels/"):

  # Change these to whatever the path is within your own system
  images = []
  labels = []

  # Reads in the label path and finds the related
  def find_label(folderName):
      for file in os.listdir(label_path):
          if file.startswith(folderName):
            # Return Labeling Assignment Here
            pass

  # Read in each individual satellite position
  for folder in os.listdir(data_path):
      currentLabel = find_label(folder)
      for subfolder in os.listdir(os.path.join(data_path, folder)):
          for file in os.listdir(os.path.join(data_path, folder, subfolder)):
            img = cv2.imread(os.path.join(data_path, folder, file))
            images.append(img)
            labels.append(currentLabel)


