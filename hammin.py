import numpy as np
from scipy import signal 
import hamming as hm
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
lis=[0,1,2,3,0.4885,0.66,0.9,1.2]
xlist=[0,1,2,3,4,5,6,7]
size=30

h_window=hm.hamming(size)
half_max=0.5*max(h_window)
half_m = h_window.flat[np.abs(h_window - half_max).argmin()]
# print(h_window)

# print(half_m)
print(xlist)
plt.plot(xlist,lis,label="line1")


print("Value range:")

indices = [i for i, value in enumerate(h_window) if value== half_m]
ii = np.where(h_window == half_m)[0] 
multiply=True
i=0
lis2=[]
while multiply:
    for value in h_window:
        if value>half_m and i<8:
            lis2.append(lis[i]*value)
            i+=1
    multiply=False        
plt.plot(xlist,lis2,label="line2")
plt.show()
         
# print("check first index:")
# print(h_window[indices[0]])
# print("check second index:")
# print(ii)

#for o in list:
    # for f in window:
    #     h=f*o
    #     print(h)


# plt.title("Hamming window")
# plt.ylabel("Amplitude")
# plt.xlabel("Sample")
# plt.figure()
# A = fft(window, 2048) / (len(window)/2.0)
# freq = np.linspace(-0.5, 0.5, len(A))
# response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
# plt.plot(freq, response)
# plt.axis([-0.5, 0.5, -120, 0])
# plt.title("Frequency response of the Hamming window")
# plt.ylabel("Normalized magnitude [dB]")
# plt.xlabel("Normalized frequency [cycles per sample]")