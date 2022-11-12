# RICARDO BHARAT@U.K.Z.N - 219014175@stu.ukzn.ac.za
# This main.py file is used to present Pothole Detector App in action with a sample video
import cv2 as cv
import numpy as np
import tensorflow.keras
import imutils
from playsound import playsound

global potholePredictorModel
size = 250


def predict_class(current_frame):
    class_names = ['No Pothole', 'Pothole']

    #  Image Shape formatted to make it compatible with model input shape
    current_frame = cv.cvtColor(current_frame, cv.COLOR_BGR2RGB)
    current_frame = cv.resize(current_frame, (size, size), interpolation=cv.INTER_AREA)

    prediction_from_model = potholePredictorModel.predict(np.array([current_frame]) / 255)

    index = np.argmax(prediction_from_model)

    if prediction_from_model[0][index] >= 0.90:
        return class_names[index]

    return class_names[0]


if __name__ == '__main__':

    prediction = []

    potholePredictorModel = tensorflow.keras.models.load_model(
        'pothole_classifier_final.model')  # Load CNN Model from same directory as main.py

    # camera = cv.VideoCapture('20221105_142618.mp4')  # pass 0 as parameter instead to use livestream, as feed as
    # shown in the line below
    camera = cv.VideoCapture(0)
    count = 30
    while True:

        (grabbed, frame) = camera.read()

        frame = imutils.resize(frame, width=600, height=3000)
        # frame = cv.flip(frame, 0)  # Comment this line out if using live feed

        displayFrame = frame.copy()  # Make Copy of Frame to pass into predict_class method to determine if there is a
        prediction = predict_class(displayFrame)  # pothole in frame

        keypress_toshow = cv.waitKey(1)

        # Display Prediction

        cv.putText(displayFrame, str(prediction), (30, 30), cv.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)
        cv.imshow("Pothole Detection System", displayFrame)

        if prediction == 'Pothole' and count >= 30:
            playsound('PotholeDetected.mp3')

        keypress = cv.waitKey(1) & 0xFF
        if keypress == ord("q"):
            break

    camera.release()
    cv.destroyAllWindows()
