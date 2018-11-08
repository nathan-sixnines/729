import cv2 
import numpy as np

lock = cv2.imread('lock-0.png', cv2.IMREAD_UNCHANGED)
key  = cv2.imread('key-0.png', cv2.IMREAD_UNCHANGED)

outLock = np.zeros_like(lock)
outKey = np.zeros_like(key)
    
    #[lock[:,:,0]/3*1,lock[:,:,1]/2*0,lock[:,:,2]/2*0,lock[:,:,3]])
    
outLock[:,:,0] = lock[:,:,0]*0
outLock[:,:,1] = lock[:,:,1]*0 
outLock[:,:,2] = lock[:,:,2]*1.1
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock1.png',outLock)

outLock[:,:,0] = lock[:,:,0]*3
outLock[:,:,1] = lock[:,:,1]*0 
outLock[:,:,2] = lock[:,:,2]*3 
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock2.png',outLock)

outLock[:,:,0] = lock[:,:,0]*3
outLock[:,:,1] = lock[:,:,1]*3 
outLock[:,:,2] = lock[:,:,2]*0
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock3.png',outLock)

outLock[:,:,0] = lock[:,:,0]*3
outLock[:,:,1] = lock[:,:,1]*0 
outLock[:,:,2] = lock[:,:,2]*0
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock4.png',outLock)

outLock[:,:,0] = lock[:,:,0]*2.5
outLock[:,:,1] = lock[:,:,1]*2
outLock[:,:,2] = lock[:,:,2]*1.5
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock4.png',outLock)


outLock[:,:,0] = lock[:,:,0]*0
outLock[:,:,1] = lock[:,:,1]*1.5
outLock[:,:,2] = lock[:,:,2]*.5
outLock[:,:,3] = lock[:,:,3] 


cv2.imwrite('lock5.png',outLock)

outLock[:,:,0] = lock[:,:,0]*2.5
outLock[:,:,1] = lock[:,:,1]*5
outLock[:,:,2] = lock[:,:,2]*7
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock6.png',outLock)

outLock[:,:,0] = lock[:,:,0]*0
outLock[:,:,1] = lock[:,:,1]*.5
outLock[:,:,2] = lock[:,:,2]*1.5
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock7.png',outLock)

outLock[:,:,0] = lock[:,:,0]*1
outLock[:,:,1] = lock[:,:,1]*1.5
outLock[:,:,2] = lock[:,:,2]*1.5
outLock[:,:,3] = lock[:,:,3] 

cv2.imwrite('lock8.png',outLock)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


outKey[:,:,0] = key[:,:,0]*0
outKey[:,:,1] = key[:,:,1]*0 
outKey[:,:,2] = key[:,:,2]*1.1
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key1.png',outKey)

outKey[:,:,0] = key[:,:,0]*3
outKey[:,:,1] = key[:,:,1]*0 
outKey[:,:,2] = key[:,:,2]*3 
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key2.png',outKey)

outKey[:,:,0] = key[:,:,0]*3
outKey[:,:,1] = key[:,:,1]*3 
outKey[:,:,2] = key[:,:,2]*0
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key3.png',outKey)

outKey[:,:,0] = key[:,:,0]*3
outKey[:,:,1] = key[:,:,1]*0 
outKey[:,:,2] = key[:,:,2]*0
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key4.png',outKey)

outKey[:,:,0] = key[:,:,0]*2.5
outKey[:,:,1] = key[:,:,1]*2
outKey[:,:,2] = key[:,:,2]*1.5
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key4.png',outKey)


outKey[:,:,0] = key[:,:,0]*0
outKey[:,:,1] = key[:,:,1]*1.5
outKey[:,:,2] = key[:,:,2]*.5
outKey[:,:,3] = key[:,:,3] 


cv2.imwrite('key5.png',outKey)

outKey[:,:,0] = key[:,:,0]*2.5
outKey[:,:,1] = key[:,:,1]*5
outKey[:,:,2] = key[:,:,2]*7
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key6.png',outKey)

outKey[:,:,0] = key[:,:,0]*0
outKey[:,:,1] = key[:,:,1]*.5
outKey[:,:,2] = key[:,:,2]*1.5
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key7.png',outKey)

outKey[:,:,0] = key[:,:,0]*1
outKey[:,:,1] = key[:,:,1]*1.5
outKey[:,:,2] = key[:,:,2]*1.5
outKey[:,:,3] = key[:,:,3] 

cv2.imwrite('key8.png',outKey)