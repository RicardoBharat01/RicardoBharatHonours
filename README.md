# Ricardo Bharat Honours COMP700 - 219014175

This ReadME.md describes the contents of the Git Repository (Section A) as well as the .exe files that can run with less configuration (Section B) and how to access them.

Git Repository contains Source Code(for Actual Real Time System as well as the System working on a Sample Video) for System and Model Construction, Dataset used for Model Construction and other files needed to run the source code in Python Enviroment.

OneDrive Shared Folder contains the .exe Application files(Actual Real Time System as well as the System working on a Sample Video) of the System and other files needed to run the Application. and my other files  for project

## A. Git Repository 
Available At:
        https://github.com/RicardoBharat01/RicardoBharatHonours.git

### 1."Pothole Dataset" Folder

This folder contains the images used to train the Convolutional Neural Network.
It contains images of the two classes, namely Potholes and Plain Road Images.
This Dataset is used in the "RicardoBharatCNNModelContstruction.ipynb" notebook to train the data.
    
### 2."PotholeDetectionSystem" Folder

This folder contains six items:
    
i."pothole_classifier_final.model" - this is the saved CNN model after training that has a final accuracy of 92.72% on the 
   testing data.
      
ii."PotholeDetected.mp3" - this audio is used by the system to play an audible warning when a pothole is detected.
      
iii."RicardoBharatCNNModelContstruction.ipynb" - this notebook was run on Google Collab and used to get the Trained CNN model.
      
iv."RealTimePredictor.py" - The source code for the Real Time Predicting System that can be run on your Laptop/PC.
    The requirements on how to run this are discussed below.
      
vi."TestSamplePredictor.py" - The source code of the System that does its predictions on the "SampleVideo.mp4", which can be run on 
    your Laptop/PC. The requirements on how to run this are discussed below.
      
vi."SampleVideo.mp4" - This is the sample video used by "TestSamplePredictor.py".
    This video is meant to display how the system works without having to set it up to run in a real environment.
      
### 3. How to Run "RealTimePredictor.py" and "TestSamplePredictor.py":

(Download and Extract the folder from GitHub onto your local machine and follow all the instructions below before running.)
    
i.Ensure that you are running these files in a Python Environment.The Python Version needs to be 3.10,
  which you can download and install from the official python website.

ii.You need to have pip installed.

iii.Use pip to install libraries with the following commands:
```
pip install opencv-python
pip install numpy
pip install --upgrade pip
pip install tensorflow
pip install imutils
pip install playsound
 ```
iv.You can then navigate to the directory/folder where these files are stored and run the python code (Python Version:3.10).

v.Ensure that "SampleVideo.mp4", "PotholeDetected.mp3" and "pothole_classifier_final.model" is in the same directory/folder as "TestSamplePredictor.py" 
  before running the Sample Predicting System("TestSamplePredictor.py"). 

vii.Ensure that  "PotholeDetected.mp3" and "pothole_classifier_final.model" is in the same directory/folder as "RealTimePredictor.py"
    before running the Real Time Pothole Predicting System("RealTimePredictor.py"). 
        
## B. OneDrive Application Files(.exe files) + Presentation Video + dataset + Source Code
Available in learn read me file:
        
        
(Link Expires on 12/12/2022)

### 1."Ricardo Bharat Honours EXE Files" Folder

This folder contains 6 items:
    
i."pothole_classifier_final.model" - this is the saved CNN model after training that has a final accuracy of 92.72% on the 
   testing data.
      
ii."PotholeDetected.mp3" - This audio is used by the system to play an audible warning when a pothole is detected.
      
iii."RicardoBharatCNNModelContstruction.ipynb" - this notebook was run on Google Collab and used to get the Trained CNN model.
      
iv."RealTimePredictor.exe" - This Real Time Predicting System that can be run on your Laptop/PC.
    The requirements on how to run this is discussed below.
      
vi."TestSamplePredictor.exe" - This is a System that does its predictions on the "SampleVideo.mp4", which can be run on 
    your Laptop/PC. The requirements on how to run this are discussed below.
      
vi."SampleVideo.mp4" - This is the sample video used by "TestSamplePredictor.exe".
    This video is meant to display how the system works without having to set it up to run in a real environment.
        
### 2.How to Run "RealTimePredictor.exe" and "TestSamplePredictor.exe":
 
(Download and Extract the folder from OneDrive onto your local machine and follow all the instructions below before running.)
    
i.You must navigate to the directory/folder where these files are downloaded to or are stored and run the .exe applications
  through the cmd by simply typing the file name once in the directory("TestSamplePredictor.exe" or "RealTimePredictor.exe") and pressing enter.
      
ii.You can also navigate to the directory/folder where these files are downloaded or are stored and run the .exe applications by running them as adminstrator.
    
iii. These applications might take a long time to load up depending on your PC Specifications; it usually takes at most a minute to load up.
    
iv.Ensure that "SampleVideo.mp4", "PotholeDetected.mp3" and "pothole_classifier_final.model" is in the same directory/folder as "TestSamplePredictor.exe" 
   before running the Sample Predicting System("TestSamplePredictor.exe"). 

v.Ensure that  "PotholeDetected.mp3" and "pothole_classifier_final.model" are in the same directory/folder as "RealTimePredictor.exe"
        before running the Real Time Pothole Predicting System("RealTimePredictor.exe"). 
     
