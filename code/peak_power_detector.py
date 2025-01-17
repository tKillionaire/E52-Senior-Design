"""
Tektronix RSA API: Peak Power Detector
Author: Morgan Allison
Date created: 6/15
Date edited: 11/16
Windows 7 64-bit
RSA API version 3.9.0029
Python 3.5.2 64-bit (Anaconda 4.2.0)
NumPy 1.11.0, MatPlotLib 1.5.3
To get Anaconda: http://continuum.io/downloads
Anaconda includes NumPy and MatPlotLib
"""

from ctypes import *
import numpy as np
import matplotlib.pyplot as plt
import os

"""
################################################################
C:\Tektronix\RSA_API\lib\x64 needs to be added to the 
PATH system environment variable
################################################################
"""
os.chdir("C:\\Tektronix\\RSA_API\\lib\\x64")
<<<<<<< HEAD
##rsa = cdll.LoadLibrary("RSA_API.dll")
rsa = cdll.LoadLibrary("C:\\Tektronix\\RSA_API\\lib\\x64\\RSA_API.dll")

"""#################CLASSES AND FUNCTIONS#################"""
#create Spectrum_Settings data structure
class Spectrum_Settings(Structure):
	_fields_ = [('span', c_double), 
	('rbw', c_double),
	('enableVBW', c_bool), 
	('vbw', c_double),
	('traceLength', c_int), 
	('window', c_int),
	('verticalUnit', c_int), 
	('actualStartFreq', c_double), 
	('actualStopFreq', c_double),
	('actualFreqStepSize', c_double), 
	('actualRBW', c_double),
	('actualVBW', c_double), 
=======
rsa = cdll.LoadLibrary("C:\\Tektronix\\RSA_API\\lib\\x64\\RSA_API.dll")


"""#################CLASSES AND FUNCTIONS#################"""
#create Spectrum_Settings data structure
class Spectrum_Settings(Structure):
	_fields_ = [('span', c_double),
	('rbw', c_double),
	('enableVBW', c_bool),
	('vbw', c_double),
	('traceLength', c_int),
	('window', c_int),
	('verticalUnit', c_int), ##0 is dBm, 1 is Watt, 2 Volt, 3 amp
	('actualStartFreq', c_double),
	('actualStopFreq', c_double),
	('actualFreqStepSize', c_double),
	('actualRBW', c_double),
	('actualVBW', c_double),
>>>>>>> 6188c3d7f9215ccd8beae2374f5ec6a4a60484b0
	('actualNumIQSamples', c_double)]

class Spectrum_TraceInfo(Structure):
	_fields_ = [('timestamp', c_int64), ('acqDataStatus', c_uint16)]

def search_connect():
    #search/connect variables
    numFound = c_int(0)
    intArray = c_int*10
    deviceIDs = intArray()
    deviceSerial = create_string_buffer(8)
    deviceType = create_string_buffer(8)
    apiVersion = create_string_buffer(16)

    #get API version
    rsa.DEVICE_GetAPIVersion(apiVersion)
    print('API Version {}'.format(apiVersion.value.decode()))

    #search
    ret = rsa.DEVICE_Search(byref(numFound), deviceIDs, 
        deviceSerial, deviceType)

    if ret != 0:
        print('Error in Search: ' + str(ret))
        exit()
    if numFound.value < 1:
        print('No instruments found. Exiting script.')
        exit()
    elif numFound.value == 1:
        print('One device found.')
        print('Device type: {}'.format(deviceType.value.decode()))
        print('Device serial number: {}'.format(deviceSerial.value.decode()))
        ret = rsa.DEVICE_Connect(deviceIDs[0])
        if ret != 0:
            print('Error in Connect: ' + str(ret))
            exit()
    else:
        print('2 or more instruments found. Enumerating instruments, please wait.')
        for inst in xrange(numFound.value):
            rsa.DEVICE_Connect(deviceIDs[inst])
            rsa.DEVICE_GetSerialNumber(deviceSerial)
            rsa.DEVICE_GetNomenclature(deviceType)
            print('Device {}'.format(inst))
            print('Device Type: {}'.format(deviceType.value))
            print('Device serial number: {}'.format(deviceSerial.value))
            rsa.DEVICE_Disconnect()
        #note: the API can only currently access one at a time
        selection = 1024
        while (selection > numFound.value-1) or (selection < 0):
            selection = int(input('Select device between 0 and {}\n> '.format(numFound.value-1)))
        rsa.DEVICE_Connect(deviceIDs[selection])
        return selection

def print_spectrum_settings(specSet):
	#print out spectrum settings for a sanity check
	print('Span: ' + str(specSet.span))
	print('RBW: ' + str(specSet.rbw))
	print('VBW Enabled: ' + str(specSet.enableVBW))
	print('VBW: ' + str(specSet.vbw))
	print('Trace Length: ' + str(specSet.traceLength))
	print('Window: ' + str(specSet.window))
	print('Vertical Unit: ' + str(specSet.verticalUnit))
	print('Actual Start Freq: ' + str(specSet.actualStartFreq))
	print('Actual End Freq: ' + str(specSet.actualStopFreq))
	print('Actual Freq Step Size: ' + str(specSet.actualFreqStepSize))
	print('Actual RBW: ' + str(specSet.actualRBW))
	print('Actual VBW: ' + str(specSet.actualVBW))


def main():
	"""#################INITIALIZE VARIABLES#################"""
	#main SA parameters
	specSet = Spectrum_Settings()
	enable = c_bool(True)         #spectrum enable
<<<<<<< HEAD
	cf = c_double(4.3e6)            #center freq
	##cf = CONFIG_GetCenterFreq()
=======
	#cf = c_double(1e9)            #center freq
>>>>>>> 6188c3d7f9215ccd8beae2374f5ec6a4a60484b0
	refLevel = c_double(0)        #ref level
	ready = c_bool(False)         #ready
	timeoutMsec = c_int(100)      #timeout
	trace = c_int(0)              #select Trace 1 
	detector = c_int(1)           #set detector type to max

	traceInfo = Spectrum_TraceInfo()
	o_timeSec = c_uint64(0)
	o_timeNsec = c_uint64(0)


	"""#################SEARCH/CONNECT#################"""
	search_connect()
	

	"""#################CONFIGURE INSTRUMENT#################"""
	rsa.CONFIG_Preset()
<<<<<<< HEAD
	rsa.CONFIG_SetCenterFreq(cf)
	rsa.CONFIG_SetReferenceLevel(refLevel)
=======
	rsa.CONFIG_SetReferenceLevel(refLevel)
	'''
	for loop, x in zip(loops,cfs):
		if userSelect = loop
			cf = x
	'''
	cf = rsa.CONFIG_GetCenterFreq()
	rsa.CONFIG_SetCenterFreq(cf) ##if this doesnt work make cf a function of loop input
>>>>>>> 6188c3d7f9215ccd8beae2374f5ec6a4a60484b0
	rsa.SPECTRUM_SetEnable(enable)
	rsa.SPECTRUM_SetDefault()
	rsa.SPECTRUM_GetSettings(byref(specSet))

	#configure desired spectrum settings
	#some fields are left blank because the default
	#values set by SPECTRUM_SetDefault() are acceptable
<<<<<<< HEAD
	specSet.span = c_double(10e6)
	specSet.rbw = c_double(3e6)
	#specSet.enableVBW = 
	#specSet.vbw = 
	specSet.traceLength = c_int(801)
	#specSet.window = 
	#specSet.verticalUnit = 
	specSet.actualStartFreq = c_double(3.9e6)
	specSet.actualFreqStepSize = c_double(10e3)
=======
	specSet.span = c_double(500e3)
	specSet.rbw = c_double(50e3)
	#specSet.enableVBW = 
	specSet.vbw = c_douuble(50e3)
	specSet.traceLength = c_int(801)
	#specSet.window = 
	#specSet.verticalUnit = 
	#specSet.actualStartFreq = 
	#specSet.actualFreqStepSize = 
>>>>>>> 6188c3d7f9215ccd8beae2374f5ec6a4a60484b0
	#specSet.actualRBW = 
	#specSet.actualVBW = 
	#specSet.actualNumIQSamples = 

	#set desired spectrum settings
	rsa.SPECTRUM_SetSettings(specSet)
	rsa.SPECTRUM_GetSettings(byref(specSet))

	#print spectrum settings for sanity check
	#print_spectrum_settings(specSet)


	"""#################INITIALIZE DATA TRANSFER VARIABLES#################"""
	#initialize variables for GetTrace
	traceArray = c_float * specSet.traceLength
	traceData = traceArray()
	outTracePoints = c_int()

	#generate frequency array for plotting the spectrum
	freq = np.arange(specSet.actualStartFreq, 
		specSet.actualStartFreq + specSet.actualFreqStepSize*specSet.traceLength, 
		specSet.actualFreqStepSize)


	"""#################ACQUIRE/PROCESS DATA#################"""
	#start acquisition
	rsa.DEVICE_Run()
	rsa.SPECTRUM_AcquireTrace()
	while ready.value == False:
		rsa.SPECTRUM_WaitForDataReady(timeoutMsec, byref(ready))
	rsa.SPECTRUM_GetTrace(c_int(0), specSet.traceLength, 
		byref(traceData), byref(outTracePoints))
	rsa.SPECTRUM_GetTraceInfo(byref(traceInfo))
	rsa.DEVICE_Stop()

	i_timestamp = c_uint64(traceInfo.timestamp)
	rsa.REFTIME_GetTimeFromTimestamp(i_timestamp, byref(o_timeSec), 
		byref(o_timeNsec))
	print('Seconds since 00:00:00 on Jan 1, 1970: {}'.format(
	 	o_timeSec.value))

	#convert trace data from a ctypes array to a numpy array
	trace = np.ctypeslib.as_array(traceData)

	#Peak power and frequency calculations
	peakPower = np.amax(trace)
	peakPowerFreq = freq[np.argmax(trace)]
	print('Peak power in spectrum: %4.3f dBm @ %d Hz' % (peakPower, peakPowerFreq))


	"""#################SPECTRUM PLOT#################"""
	#plot the spectrum trace (optional)
	plt.figure(1)
<<<<<<< HEAD
	plt.subplot(111, facecolor='k')
=======
	plt.subplot(111, axisbg='k')
>>>>>>> 6188c3d7f9215ccd8beae2374f5ec6a4a60484b0
	plt.plot(freq, traceData, 'y')
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Amplitude (dBm)')
	plt.title('Spectrum')
	
	#annotate measurement
	plt.axvline(x=peakPowerFreq)
<<<<<<< HEAD
	text_x = specSet.actualStartFreq + specSet.span/20
	plt.text(text_x, peakPower, 
		'Peak power in spectrum: %4.3f dBm @ %5.4f MHz' % (peakPower, 
			peakPowerFreq/1e6), color='white')
	
	#BONUS clean up plot axes
	xmin = np.amin(freq)
	xmax = np.amax(freq)
	plt.xlim(xmin,xmax)
	ymin = np.amin(trace)-10
	ymax = np.amax(trace)+10
	plt.ylim(ymin,ymax)

	plt.show()
	
	print('Disconnecting.')
=======
	text_x = specSet.actualStartFreq + specSet.span/20 ##what is this
	plt.text(text_x, peakPower, 
		'Peak power in spectrum: %4.3f dBm @ %5.4f MHz' % (peakPower, 
			peakPowerFreq/1e6), color='white') #BONUS clean up plot axes
	xmin = np.amin(freq)
    xmax = np.aamax(freq)
	plt.xlim(xmin,xmax)
	ymin = np.amin(trace)-10  ##why 10
    ymax = np.amax(trace)+10
    plt.ylim(ymin,ymax)

    plt.show()
	
    print('Disconnecting.')
>>>>>>> 6188c3d7f9215ccd8beae2374f5ec6a4a60484b0
	rsa.DEVICE_Disconnect()

if __name__ == "__main__":
	main()