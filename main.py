from tkinter import *
import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy as np
from scipy import fftpack
from spectrum import *
from matplotlib.widgets import Cursor
print("Imported All Libraries")
ser = serial.Serial('COM3',115200)
print("Serial Connection Started")
window = Tk()
window.title("Accord Software and Systems Pvt Ltd")
window.geometry('600x300')
title = Label(window,text="Frequency Generator and Visualizer", fg='Black', font=("Helvetica", 16))
title.grid(row=0,columnspan=3)
subtitle = Label(window,text="Output: Asin(2πft)+B (Random Noise Function)", fg='Black', font=("Helvetica", 10))
subtitle.grid(row=1,columnspan=3)
########################################
amplbl = Label(window, text="Amplitude (A)")
amplbl.grid(column=0, row=2)
amp = Entry(window,width=30)
amp.grid(column=1, row=2)
########################################
freqlbl = Label(window, text="Frequency (f)")
freqlbl.grid(column=0, row=3)
freq = Entry(window,width=30)
freq.grid(column=1, row=3)
##################################################################################################
samplelbl = Label(window, text="N of Samples Needed per Period(n)")
samplelbl.grid(column=0,row=4)
sample = Entry(window,width=30)
sample.grid(column=1,row=4)
##################################################################################################
noiselbl = Label(window, text="Enter Max Amplitude of Noise")
noiselbl.grid(column=0,row=5)
noise = Entry(window,width=30)
noise.grid(column=1,row=5)
pausing_flag=True
##################################################################################################
pointslbl = Label(window, text="Enter No. Of. Points to collect Before Analysis (For Analysis Only)")
pointslbl.grid(column=0, row=6)
points_analysis = Entry(window,width=30)
points_analysis.grid(column=1, row=6)
def clicked():
    a=amp.get()
    f=freq.get()
    n=sample.get()
    b=noise.get()
    print(a,f,n,b)
    s=a+" "+f+" "+n+" "+b+"\r\n"
    ser.write(s.encode())
    #window.destroy()
    f=float(f)
    n=float(n)
    countervar=int(f*n)
    plot_window = countervar
    y_var = np.array(np.zeros([plot_window]))
    X = np.array(np.zeros([plot_window]))
    plt.ion()
    fig,ax = plt.subplots(nrows=4, ncols=3, figsize=(10, 10))
    ax[0,0].set_title("Recieved Signal")
    ax[0,1].set_title("FFT")
    ax[0,2].set_title("Real-time FFT")
    ax[1, 0].set_title("Magnitude Spectrum")
    ax[1, 1].set_title("Log. Magnitude Spectrum")
    ax[2, 0].set_title("Phase Spectrum ")
    ax[2, 1].set_title("Angle Spectrum")

    line, = ax[0,0].plot(y_var,color='C7')
    line2, = ax[0,1].plot(X,color='C8')
    line3, = ax[0,2].plot(X,color='C9')
    line4, = ax[1,2].plot(X)
    line5, = ax[2,2].plot(X)
    line6, = ax[3,2].plot(X)

    f_s=f*n #This is the sampling Frequency
    counter=0
    while pausing_flag:
        try:
            ser.flush()
            ser_bytes = ser.readline()
            counter+=1
            try:
                decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                print(decoded_bytes)
            except:
                continue
            with open("test_data.csv","a") as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([time.time(),decoded_bytes])
            y_var = np.append(y_var,decoded_bytes)
            y_var = y_var[1:plot_window+1]
            if counter==100:
                counter=0
                line.set_ydata(y_var)
                ax[0,0].relim()
                ax[0,0].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ######################################################################
                X = fftpack.fft(y_var)
                freqs = fftpack.fftfreq(len(y_var)) * f_s
                #freqs = fftpack.fftfreq(len(y_var))
                line2.set_ydata(np.abs(X))
                line2.set_xdata(np.abs(freqs))
                ax[0,1].relim()
                ax[0,1].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #######################################################################
                X2 = fftpack.rfft(y_var)
                #freqs = fftpack.fftfreq(len(y_var),1/f_s) * f_s
                line3.set_ydata(np.abs(X2))
                line3.set_xdata(np.abs(freqs))
                ax[0,2].relim()
                ax[0,2].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #######################################################################
                ax[1,0].clear()
                ax[1,0].magnitude_spectrum(y_var, Fs=f_s, color='C1')
                ax[1,0].relim()
                ax[1,0].autoscale_view(tight=True)
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ########################################################################
                ax[1,1].clear()
                ax[1,1].magnitude_spectrum(y_var, Fs=f_s,scale='dB', color='C2')
                ax[1,1].relim()
                ax[1,1].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                X3 = fftpack.dct(y_var)
                #freqs = fftpack.fftfreq(len(y_var),1/f_s) * f_s
                freqs = fftpack.fftfreq(len(y_var))
                line4.set_ydata(np.abs(X3))
                line4.set_xdata(np.abs(freqs))
                ax[1,2].relim()
                ax[1,2].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                ax[2,0].clear()
                ax[2,0].phase_spectrum(y_var, Fs=f_s, color='C3')
                ax[2,0].relim()
                ax[2,0].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                ax[2,1].clear()
                ax[2,1].angle_spectrum(y_var, Fs=f_s, color='C4')
                ax[2,1].relim()
                ax[2,1].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ########################################################################
                X4 = fftpack.dst(y_var)
                #freqs = fftpack.fftfreq(len(y_var),1/f_s) * f_s
                freqs = fftpack.fftfreq(len(y_var))
                line5.set_ydata(np.abs(X4))
                line5.set_xdata(np.abs(freqs))
                ax[2,2].relim()
                ax[2,2].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                ax[3,0].clear()
                ax[3,0].specgram(y_var, Fs=f_s)
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ########################################################################
                ax[3,1].clear()
                ax[3,1].psd(y_var, NFFT=301,Fs=f_s,color='C5', pad_to=1024, scale_by_freq=True)
                ########################################################################
                ax[3,2].clear()
                ax[3,2].psd(y_var, NFFT=150,Fs=f_s ,color='C6', pad_to=512, noverlap=75, scale_by_freq=True)
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                fig.canvas.draw()
                fig.canvas.flush_events()
        except:
            print("Keyboard Interrupt")
            break
########################################################################################################################
def clicked_with_limited():
    a=amp.get()
    f=freq.get()
    n=sample.get()
    b=noise.get()
    print(a,f,n,b)
    s=a+" "+f+" "+n+" "+b+"\r\n"
    ser.write(s.encode())
    #window.destroy()
    f=float(f)
    n=float(n)
    countervar=int(f*n)
    plot_window = countervar
    y_var = np.array(np.zeros([plot_window]))
    X = np.array(np.zeros([plot_window]))
    plt.ion()
    fig,ax = plt.subplots(nrows=4, ncols=3, figsize=(10, 10))
    ax[0,0].set_title("Recieved Signal")
    ax[0,1].set_title("FFT")
    ax[0,2].set_title("Real-time FFT")
    ax[1, 0].set_title("Magnitude Spectrum")
    ax[1, 1].set_title("Log. Magnitude Spectrum")
    ax[2, 0].set_title("Phase Spectrum ")
    ax[2, 1].set_title("Angle Spectrum")

    line, = ax[0,0].plot(y_var,color='C7')
    line2, = ax[0,1].plot(X,color='C8')
    line3, = ax[0,2].plot(X,color='C9')
    line4, = ax[1,2].plot(X)
    line5, = ax[2,2].plot(X)
    line6, = ax[3,2].plot(X)

    f_s=f*n #This is the sampling Frequency
    counter=0
    points=0
    pointstoeval=int(points_analysis.get())
    while points!=pointstoeval:
        try:
            ser.flush()
            ser_bytes = ser.readline()
            counter+=1
            try:
                decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                print(decoded_bytes)
            except:
                continue
            with open("test_data.csv","a") as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([time.time(),decoded_bytes])
            y_var = np.append(y_var,decoded_bytes)
            y_var = y_var[1:plot_window+1]
            if counter==100:
                counter=0
                line.set_ydata(y_var)
                ax[0,0].relim()
                ax[0,0].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ######################################################################
                X = fftpack.fft(y_var)
                freqs = fftpack.fftfreq(len(y_var)) * f_s
                #freqs = fftpack.fftfreq(len(y_var))
                line2.set_ydata(np.abs(X))
                line2.set_xdata(np.abs(freqs))
                ax[0,1].relim()
                ax[0,1].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #######################################################################
                X2 = fftpack.rfft(y_var)
                #freqs = fftpack.fftfreq(len(y_var),1/f_s) * f_s
                line3.set_ydata(np.abs(X2))
                line3.set_xdata(np.abs(freqs))
                ax[0,2].relim()
                ax[0,2].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #######################################################################
                ax[1,0].clear()
                ax[1,0].magnitude_spectrum(y_var, Fs=f_s, color='C1')
                ax[1,0].relim()
                ax[1,0].autoscale_view(tight=True)
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ########################################################################
                ax[1,1].clear()
                ax[1,1].magnitude_spectrum(y_var, Fs=f_s,scale='dB', color='C2')
                ax[1,1].relim()
                ax[1,1].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                X3 = fftpack.dct(y_var)
                #freqs = fftpack.fftfreq(len(y_var),1/f_s) * f_s
                freqs = fftpack.fftfreq(len(y_var))
                line4.set_ydata(np.abs(X3))
                line4.set_xdata(np.abs(freqs))
                ax[1,2].relim()
                ax[1,2].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                ax[2,0].clear()
                ax[2,0].phase_spectrum(y_var, Fs=f_s, color='C3')
                ax[2,0].relim()
                ax[2,0].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                ax[2,1].clear()
                ax[2,1].angle_spectrum(y_var, Fs=f_s, color='C4')
                ax[2,1].relim()
                ax[2,1].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ########################################################################
                X4 = fftpack.dst(y_var)
                #freqs = fftpack.fftfreq(len(y_var),1/f_s) * f_s
                freqs = fftpack.fftfreq(len(y_var))
                line5.set_ydata(np.abs(X4))
                line5.set_xdata(np.abs(freqs))
                ax[2,2].relim()
                ax[2,2].autoscale_view()
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                #########################################################################
                ax[3,0].clear()
                ax[3,0].specgram(y_var, Fs=f_s)
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                ########################################################################
                ax[3,1].clear()
                ax[3,1].psd(y_var, NFFT=301,Fs=f_s,color='C5', pad_to=1024, scale_by_freq=True)
                ########################################################################
                ax[3,2].clear()
                ax[3,2].psd(y_var, NFFT=150,Fs=f_s ,color='C6', pad_to=512, noverlap=75, scale_by_freq=True)
                ##fig.canvas.draw()
                ##fig.canvas.flush_events()
                fig.canvas.draw()
                fig.canvas.flush_events()
            points+=1
        except:
            print("Keyboard Interrupt")
            break
    plt.ioff()
    cursor = Cursor(ax[0,0], useblit=True, color='green', linewidth=1)
    cursor2 = Cursor(ax[0,1], useblit=True, color='green', linewidth=1)
    cursor3 = Cursor(ax[0,2], useblit=True, color='green', linewidth=1)
    cursor4 = Cursor(ax[1,0], useblit=True, color='green', linewidth=1)
    cursor5 = Cursor(ax[1,1], useblit=True, color='green', linewidth=1)
    cursor6 = Cursor(ax[1,2], useblit=True, color='green', linewidth=1)
    cursor7 = Cursor(ax[2,0], useblit=True, color='green', linewidth=1)
    cursor8 = Cursor(ax[2,1], useblit=True, color='green', linewidth=1)
    cursor9 = Cursor(ax[2,2], useblit=True, color='green', linewidth=1)
    cursor10 = Cursor(ax[3,0], useblit=True, color='red', linewidth=1)
    cursor11 = Cursor(ax[3,1], useblit=True, color='green', linewidth=1)
    cursor12 = Cursor(ax[3,2], useblit=True, color='green', linewidth=1)
    plt.show()
#########################################################################################################################
btn = Button(window, text="Start Visualization in realtime", command=clicked)
btn.grid(column=0, row=7)
btn2 = Button(window, text="Start Analysis", command=clicked_with_limited)
btn2.grid(column=1, row=7)
window.mainloop()
