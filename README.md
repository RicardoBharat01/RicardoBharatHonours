# Ricardo Bharat Honours COMP700 - 219014175

ReadME.md describes the contents of the Git Repository (Section A) as well as how to access the .exe files that can run without less configuration(Section B).

## A. Git Repository 
    Available At:
        https://github.com/RicardoBharat01/RicardoBharatHonours.git

### 1."Pohole Dataset" Folder

    This folder contains the images used to train the Convolutional Neural Network.
    It contains images of the two classes namely Potholes and Plain Road Images.
    This Dataset is used in the "RicardoBharatCNNModelContstruction.ipynb" notebook to train the data.
    
### 2."PotholeDetectionSystem" Folder

    This folder contains 6 items:
    
    i."pothole_classifier_final.model" - this is the saved CNN model after training that has a final accuracy of 92.72% on the 
       testing data.
      
    ii."PotholeDetected.mp3" - this audio is used by the system to play an audible warning when a pothole is detected.
      
    iii."RicardoBharatCNNModelContstruction.ipynb" - this notebook ws run on Gooogle Collab and used to get the Trained CNN model.
      
    iv."RealTimePredictor.py" - This Real Time Predicting System that can be run on your Laptop/PC.
        The requirements on how to run this is disucssed below.
      
    vi."TestSamplePredictor.py" - This is a System that does its preidctions on the "SampleVideo.mp4", that can be run on 
        your Laptop/PC.The requirements on how to run this is disucssed below.
      
    vi."SampleVideo.mp4" - This is the sample video used by "TestSamplePredictor.py".
        This video is meant to display how the system works without having to set it up to run in a real enviroment.
      
### 3."How to Run "RealTimePredictor.py" and "TestSamplePredictor.py"":

    i.Ensure that you are running these files in a Python Envoriment.The Python Version needs to be 3.10,
      which you can download and install from the official python website.

    ii.You need to have pip installed.

    iii.Use pip to install libaries with the following commands:
```
pip install opencv-python
pip install numpy
pip install --upgrade pip
pip install tensorflow
pip install imutils
pip install playsound
 ```
    iv.You can then navigate to the directory where these files are stored and run the python code (Python Version:3.10).

    v.Ensure that "SampleVideo.mp4", "PotholeDetected.mp3" and "pothole_classifier_final.model" are in the same directory as "TestSamplePredictor.py" 
      before running the Sample Predicting System("TestSamplePredictor.py"). 

    vii.Ensure that  "PotholeDetected.mp3" and "pothole_classifier_final.model" are in the same directory as "RealTimePredictor.py"
        before running the Real Time Pothole Predicting System("RealTimePredictor.py"). 
        
## B. OneDrive Application (.exe files) 
