import cv2
image=cv2.imread("lena.jpg",1)
cv2.circle(image,(50,50),50,(0,0,255),-1)
cv2.circle(image,(460,50),50,(0,0,255),-1)
cv2.circle(image,(50,460),50,(0,0,255),-1)
cv2.circle(image,(460,460),50,(0,0,255),-1)
cv2.rectangle(image,(50,50),(460,460),(0,255,0),3)
cv2.line(image,(50,50),(460,460),(255,0,0),5)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"Hello",(160,45),font,2,(10,56,167))
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()