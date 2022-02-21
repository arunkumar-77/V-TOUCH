# V-TOUCH

Virtual Touch aims in building an interface for ATMs, enabling contactless transaction and also ensures that the user wears mask while transaction.

Note: This code was written in exploratory style.

## COMPONENTS

<table>
  <tr>
    <th  style="width:40%">Componenets</th>
    <th style="width:30%" colspan="2">Demo</th>
  </tr>
   
   <tr>
    <td> Graphical User Interface
    <li> To show the ATM interface </li>
    <li> It will in the displayed in front monitor </li>
    <li> The 1st camera records the face and fingers(mouse) and is placed above the monitor</li>
    <li> The 2nd camera records the number shown in hands(PIN) </li>
     </td>
    <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/gui.gif" width="450" height="160"/><p align="center">GUI</p></td>
     <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/atm%20model.png" width="400"/><p align="center">ATM Design</p></td>
  </tr>
   
   <tr>
    <td> Mask Detection
    <li>  To ensure that the user has worn mask </li>
      <li>The process will be inaccessible if the user doesn't wear mask </li>
      <li>It will be resumed only when the user wears mask</li>
     </td>
    <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/mask%20-%20desk.gif" width="450" height="180"/></td>
     <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/mask%20-%20face.gif" width="400" height="150"/></td>
  </tr>
  
   <tr>
    <td> Virtual Mouse
    <li> The front camera records the position of the hand and moves the cursor accordingly, when the index finger is straight </li>
    <li>  When the index finger and middle finger are straight then the mouse is clicked </li>
    <li> An indicator is placed at the top right cursor of the GUI for detecting the mode of hand movement</li>
    <ul>
      <li> Red - if no hand is detected</li>
      <li> Yellow - if hand is detected but not in moving mode</li>
      <li> Green - if the hand is in moving mode</li>
     <ul>
     </td>
      <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/click%20-%20desk.gif" width="450" height="180"/><p align="center">The indicator is at the top right corner</p></td>
      <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/click%20-%20face.gif" width="400" height="150"/><p align="center">The green dot in the index finger is visible while clicking</p></td>
  </tr>
   
  <tr>
    <td> Finger Counter
    <li> It is placed in a seperate compartment inorder to hide from the next user who stands behind</li>
      <li> The digits in PIN are limited to 1-5 for easeness and 0 is used as seperator between each digit of the PIN</li>
      <p>For eg: Consider 12345 as the PIN, then user must show 0102030405 to the camera. And if the user shows the PIN in as not specified then user is asked to re-enter the PIN</p>
     </td>
    <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/finger_counter-entering%20pin.gif" width="450" height="180"/><p align="center">The way of entering PIN(12345)</p></td>
    <td><img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/finger_counter.gif" width="400" height="150"/><p align="center">Shows number from 0-5</p></td>
  </tr>

</table>


* Parallel processing
    * To enable both the Virtual Mouse, Mask Detection, and GUI work in parallel
* Greetings
    * To Welcome and Thank user while initiating and finishing Transaction Process through voice
## Features

- The finger counter and virtual mouse are both left and right hand recognizable
- The nearest hand will be detected for virtual mouse
- The nearest face will be detected for face mask detection
- The amount is entered using virtual mouse with the help of keyboard like structure displayed on moniter
<img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/amount%20entering.png" width="350">
<li> Since V-Touch is an interface,
  <ul>
    <li> we simply neglect the card reader portion by clicking next</li>
    <li> the entered PIN is not checked with stored data, rather only printed in the console</li>
  </ul></li>
<li> The session details such as: mask details, entered PIN and entered amount we be printed in the console
  <ul><li> Session Details - (The user removed and wore the mask while entering amount)</li></ul>
 <img src="https://github.com/Kasinath-J/V-TOUCH/blob/main/gif/session%20details.png " width="250">
  <li> The process can be cancelled at any moment</li>
 

## Acknowledgements

 - [Virtual Mouse](https://youtu.be/8gPONnGIPgw)
 - [Finger Counter](https://youtu.be/p5Z_GGRCI5s)
 - [Face Mask Detection](https://youtu.be/Ax6P93r32KU)


## Python Libraries

* opencv (Webcam)
* haarcascade frontal face (Face detection)
* medipipe (Virtual mouse and Finger counter)
* autopy (Moving and clicking mouse)
* pyttsx3 (Speech)
* threading (Parallel execution)
* tkinter (Graphical User Interface)
* tensorflow (Mask Detection)
* keras (Mask Detection)
* time, math, numpy
  

## Installation

Clone the project and install necessary packages with the below code (Windows)

```bash
  pip install -r requirements.txt
```
  
 And then run index.py file.
  
Note : Two cameras are needed to run this program.(You could use your phone as second camera through other apps such as droidcam)

## Contributed By
  
 * [Kasinath J](https://www.linkedin.com/in/kasinath-j-2881a6200/)
 * [Lingeshwaran R](https://www.linkedin.com/in/lingeshwaran-r-66a238200/)
 * Thrisha R
 * [Arunkumar S](https://www.linkedin.com/in/arun-kumar-b939751ba/)
 * [Harihara Subramanium M](https://www.linkedin.com/in/harihara-subramanian-m-007/)


