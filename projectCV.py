
import cv2
import mediapipe

cap = cv2.VideoCapture(0) # here we read the video
result=cv2.VideoWriter('result',cv2.VideoWriter_fourcc(*'XVID'),30,(640,480)) #this variable we will use to but on it the result and show it

mphands=mediapipe.solutions.hands #to call the class hands
hands=mphands.Hands()#to call the Hands function which we will use later to detect the hand land marks
mpDraw=mediapipe.solutions.drawing_utils #to call the class drawing we will use it later to draw the hand land marks on the image

while True :
    _,img=cap.read()
    img = cv2.flip(img, 1)#here we flip the image

    results =hands.process(img) #here it take the img and detect the hand land marks in it
    print(results)
    if results.multi_hand_landmarks: #here we check if there is a hand in the image so we will draw it if not we will not draw anything
        for handLms in results.multi_hand_landmarks: #to draw each hand land mark on the image
            mpDraw.draw_landmarks(img, handLms,mphands.HAND_CONNECTIONS) # here to draw the hand land mark on the image and make connection between them

    result.write(img)
    cv2.imshow("frame", img)#here to show the result of our hand detect
    key = cv2.waitKey(1)
    if key == 27:#if we press ecs it will close
        break

cv2.destroyAllWindows()
cap.release()