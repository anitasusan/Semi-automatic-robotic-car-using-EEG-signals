import numpy as np
from scipy.signal import filtfilt, butter
import matplotlib.pyplot as plt
import pickle
import gzip
import scipy.fftpack
import pandas as pd


def nextpow2(i):
    """
    Find the next power of 2 for number i
    """
    n = 1
    while n < i:
        n *= 2
    return n

def firstfft(eegdata):
    winSampleLength = len(eegdata)
    # Apply Hamming window
    w = np.hamming(winSampleLength)
    dataWinCentered = eegdata - np.mean(eegdata, axis=0) # Remove offset
    
    dataWinCenteredHam = (dataWinCentered.T*w).T
    
    NFFT = nextpow2(winSampleLength)
    Y = np.fft.fft(dataWinCenteredHam, n=NFFT, axis=0)/winSampleLength
    a = 2*np.abs(Y)
    Y=pd.DataFrame(a)
    N=len(Y)
    ps=2.0/N * np.abs(Y)
    return ps

def secondfft(eegdata):
    winSampleLength = len(eegdata)
    # Apply Hamming window
    w = np.hamming(winSampleLength)
    dataWinCentered = eegdata - np.mean(eegdata, axis=0) # Remove offset
    
    dataWinCenteredHam = (dataWinCentered.T*w).T
    
    NFFT = nextpow2(winSampleLength)
    Y = np.fft.fft(dataWinCenteredHam, n=NFFT, axis=0)/winSampleLength
    a = 2*np.abs(Y[0:int(NFFT/2)])
    Y=pd.DataFrame(a)
    return Y
def fftprocessing(eegdata):
    Y1=firstfft(eegdata)
    Y=secondfft(Y1)   
    x=[]
    y=[]
    for each in range(len(Y.columns)):
        N=len(Y[Y.columns[each]])
        T=1/128
        ps=2.0/N * np.abs(Y[Y.columns[each]][:N//2])
        y.append(ps[5:14]) #choosing freq btw 10 and 25 Hz
        xax=np.linspace(0.0, 1.0/(2.0*T), int(N/2))
        xax=xax[5:14]
        x.append(xax)
    
    #plotting PSD
    for i in range(len(y)):
        plt.figure()
        plt.plot(x[i],y[i],lw=1.5)
        plt.xlabel('Frequency (Hz)')
        
        plt.ylabel('Power')
        
        plt.title('PSD')
        plt.show()
    
    #identifying frequency corresponding to max power    
    m=[]
    for i in range(len(y)):   
        k=list(y[i])
        m.append(xax[k.index(max(k))])
    return(max(m))
 

data = pd.read_csv("b.csv")
# remove last column for entire dataset
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
raw_signal=data[data.columns[6:8]]
i=0
freqvalues=[]
while i< len(raw_signal):
    eegdata = np.array(raw_signal[i:i+128])
    freqvalues.append(fftprocessing(eegdata))
    i=i+128
    