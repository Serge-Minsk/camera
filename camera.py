
import cv


cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)
config = {
    cv.CV_CAP_PROP_BRIGHTNESS: 50,
    cv.CV_CAP_PROP_CONTRAST: 70,
    cv.CV_CAP_PROP_SATURATION: 20,
}
for param, value in config.iteritems():
    cv.SetCaptureProperty(capture, param, value)
font=cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX,1,1,0,2,8)
c=1.6
Sr=15

while True:
    image=cv.QueryFrame(capture)   
    
    if image is None:
        continue
            
    image_size = cv.GetSize(image)
    grayscale = cv.CreateImage(image_size, 8, 1)

    storage = cv.CreateMemStorage(0)
    cascade = cv.Load('c:\haarcascade_frontalface_alt.xml')
    cv.CvtColor(image, grayscale, cv.CV_RGB2GRAY)

    faces = cv.HaarDetectObjects(image=grayscale, cascade=cascade, 
            storage=storage, scale_factor=1.2, 
            min_neighbors=2, flags=cv.CV_HAAR_DO_CANNY_PRUNING)
    if faces:
        for i in faces:
            cv.Rectangle(image, (i[0][0], i[0][1]),
                         (i[0][0]+i[0][2], i[0][1]+i[0][3]),
                         (255, 50, 100), 3, 8, 0)
               
            k=float(i[0][3])/320
            S = int(Sr*c/k)
            x=i[0][0]
            y=i[0][1]
            cv.PutText(image,'L=%s cm'%(S),(x,y-10), font,(255,0,0))
    cv.ShowImage("camera",image) 
    if cv.WaitKey(2)==27:
        break
cv.DestroyWindow("camera")
