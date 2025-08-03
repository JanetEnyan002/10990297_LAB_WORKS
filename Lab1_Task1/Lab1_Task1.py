 import cv2
>>> image = cv2.imread(r"C:\Users\Janet Enyan\Downloads\Photo1.jpg")
>>> gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
>>> cv2.imshow("Original Image", image)
>>> cv2.imshow('Grayscale Image', gray_image)
>>> cv2.imwrite(r"C:\Users\Janet Enyan\Downloads\photo_gray.jpg", gray_image)
True
>>> cv2.waitKey(0)
32
>>> cv2.waitKey(0)
32
>>> cv2.destroyAllWindows()
>>>