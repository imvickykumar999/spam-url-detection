import cv2, os, shutil
path = r'C:\Users\Vicky Kumar\Desktop\Experiments\Camera Webcam IP\photo'

re = '1'
while re == '1':
    
    erase = input('Enter 73u8h62 to RENEW folder : ')
    if erase == '73u8h62':
        if os.path.exists(path):
            shutil.rmtree(path)
            with open(r'C:\Users\Vicky Kumar\Desktop\Experiments\Camera Webcam IP\count.txt', 'w') as f:
                count = f.write('1')

    print('\n1). Laptop \n2). IP WebCam \n')
    camera = input('Which Camera wanna use : ')

    if camera == '1':
        url = 0
    else:
        url = 'http://10.0.251.141:8080/video'

    cap = cv2.VideoCapture(url)

    if not os.path.exists(path):
        os.mkdir(path)

    if(cap.isOpened()):

        again = '1'
        while again == '1':

            again = input('Press 1 to CLICK photo : ')
            ret, face = cap.read()

            with open(r'C:\Users\Vicky Kumar\Desktop\Experiments\Camera Webcam IP\count.txt', 'r') as f:
                count = int(f.readline())

    #         face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = r'C:\Users\Vicky Kumar\Desktop\Experiments\Camera Webcam IP\photo\count '+ str(count) + ' .jpg'
            cv2.imwrite(file_name_path, face)

            cv2.imshow('Face Cropper', face)

            count = count + 1
            count = str(count)

            with open(r'C:\Users\Vicky Kumar\Desktop\Experiments\Camera Webcam IP\count.txt', 'w') as f:
                count = f.write(count)

    else:
        print('webCam is failed to use')

    cap.release()
    cv2.destroyAllWindows()
    
    re = input('Enter 1 to REUSE : ')
else:
    print('\nThanks for Using Web Camera...')