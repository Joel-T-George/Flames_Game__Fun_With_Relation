# Flames Game Application.

## Introduction
It is a fun online relationship Calculator. This Calculator work under the concept of FLAMES to determine the relationship between two people. FLAMES stands for - Friends, Lover, Affection, Marriage, Enemy, Sister. For example, If you are in love with someone. And then test whether the love relationship is strong or not. Just enter both names on Flames Application and click on CHECK Button. It says a relationship between two people Do not take the results of the flames game too seriously. It is just for fun. 

## Flames Application behind functions.

In flame Calculation. Getting two-person names and then Comparing both person names and eliminate common characters. Take Remaining Characters Count it used in the upcoming process.

### Flames Functions
![N|](https://i.postimg.cc/rpYtz6Hr/image.png)

This figure will explain function of flames application. For example assuming two charater names Wilson and Andrea. Comparing both name and eliminating common charaters but in this case there is no common charater between two person's. And  Total Character count is 10.

for flames letter elimination we wants to go five loop to cancel each letter in FLAMES.

While looping we wants to do little math to cancel letter in FLAMES. remaining charater count wants to divde by current state of Flames string length and remainder getting number is position of the cancel letter in FLAMES string.


>Case Round 1 and 3:

In the both cases remainder number is greater than 1. So we remove letter from that position in FLAMES string.
after elimation following charaters also swap front of the string to do next loop.

following python codes are given below.
```python

elif rem < len(fl) and rem != 1 and rem !=0:
 #for storing following character for some instance.
 cpy=[]
 single = fl[rem-1]
 fl.remove(single)
 j = 0
 f = len(fl)
 #swaping start for here..
 while j < len(fl) :
	 if j>=rem-1:
		 break
	 cpy.append(fl[j])
	 fl[j]='0'  	
	 j+=1
	k=j
 while k <= j and k > 0 :
	 fl.remove('0')
	  k-=1
  fl.extend(cpy)
  #deletion of temp storage 
  del cpy
 ```

>Case Round 2 and 5:

Remainder is 0. So we wants to cancel end letter of FLAMES string.and not need to swap charaters

following Python codes are given below.
```python
if rem==0:
	  single = fl[len(fl)-1]
		fl.remove(single)
```
>Case Round 1:

Remainder is 1. So we wants to cancel First letter in FLAMES string
following Python codes are given below.
```python
elif rem ==1:
	single = fl[0]
	fl.remove(single)
	fls = "".join(fl)

```

### Flames Application Graphical-User-Interface
Flames application for GUI feature I used PyQt5 module and qss standard styling I used in this application and I Show Structure or layout of flames application.
![N|](https://i.postimg.cc/dVKCfkDN/image.png)

After getting two person name and implement to flame function and it return object. And that object contains of elimination process, remaining letter and count, some quotes,final letter and related image and that data are excuted in the GUI with standard styling.
And some debug reduce by making alert and dialog windows 

### Styling of Flames Application 
For Styling and Fonts changes. I use CSS Stylesheet and I application mostly used gradient color for button and other elements also. Pyqt5 Supports old version of CSS tags only. and final output application shows below.

![N|](https://i.postimg.cc/jC0S5F16/image.png)

## Working of Flames Application

Working and detail makking tutorial in aialphajo youtube channel and then demonstrate video link provide below.
[![N|](https://img.youtube.com/vi/sP9rHs5-4lE/maxresdefault.jpg)](https://youtu.be/sP9rHs5-4lE)


In this video shows working and installation of software is explained in this video.

>Thanking you.

#### Thank you viewers and Knowledge gainers


