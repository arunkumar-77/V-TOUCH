# V-TOUCH

Virtual Touch aims in building an interface for ATMs, enabling contactless transaction.


## MODULES

<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
   
   <tr>
    <td> Graphical User Interface
    <li> To show the ATM interface </li>
    <li> It will in the displayed in front monitor </li>
    <li>The usual interface of the ATM is designed</li>
     </td>
    <td><img src="https://github.com/Kasinath-J/delete/blob/main/gui.gif" width="300" height="200" /></td>
     <td><img src="https://github.com/Kasinath-J/delete/blob/main/atm%20model.png" width="300" height="200" /></td>
  </tr>
   
   <tr>
    <td> Mask Detection
    <li>  To ensure that the user has worn mask </li>
      <li>The process will be unaccessible if the user doesn't wear mask </li>
      <li>It will be resumed only when the user wears mask</li>
     </td>
    <td><img src="https://github.com/Kasinath-J/delete/blob/main/mask%20-%20desk.gif" width="300" height="200" /></td>
     <td><img src="https://github.com/Kasinath-J/delete/blob/main/mask%20-%20face.gif" width="300" height="200" /></td>
  </tr>
  
   <tr>
    <td> Virtual Mouse
    <li> The front camera records the position of the hand and moves the cursor accordingly, when the index finger is straight </li>
    <li>  When the index finger and middle finger are straight then the mouse is clicked </li>
    <li> An indicator is placed at the top right end of the GUI for detecting the mode of hand movement</li>
    <ul>
      <li> Red - if no hand is detected</li>
      <li> Yellow - if hand is detected but not in moving mode</li>
      <li> Green - if the hand is in moving mode</li>
     <ul>
     </td>
      <td><img src="https://github.com/Kasinath-J/delete/blob/main/click%20-%20face.gif" width="300" height="200" /></td>
      <td><img src="https://github.com/Kasinath-J/delete/blob/main/click%20-%20desk.gif" width="300" height="200" /></td>
  </tr>
   
  <tr>
    <td> Finger Counter
    <li> The second camera records the number shown in hands to enter PIN </li>
    <li> It is placed in a seperate compartment inorder to hide from the next user who stands behind</li>
      <li> The digits in PIN are limited to 1-5 for easeness and 0 is used as seperator between each digit of the PIN</li>
      <p>For eg: Consider 12345 as the PIN, then user must show 0102030405 to the camera. And if the user shows the PIN in as not specified then user is asked to re-enter the PIN</p>
     </td>
    <td><img src="https://github.com/Kasinath-J/delete/blob/main/finger_counter-entering%20pin.gif" width="300" height="200" /></td>
    <td><img src="https://github.com/Kasinath-J/delete/blob/main/finger_counter.gif" width="300" height="200" /></td>
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
<img src="https://github.com/Kasinath-J/delete/blob/main/amount%20entering.png" width="300" height="200">
- Since V-Touch is an interface,
  - we simply neglect the card reader portion by clicking next
  -  the entered PIN is not checked with stored data, rather only printed in the console
- The session details such as: mask details, entered PIN and entered amount we be printed in the console
  - Session Details - (The user removed and wore the mask while entering amount)
 <img src="https://github.com/Kasinath-J/delete/blob/main/session%20details.png" width="300" height="200">
- The process can be cancelled at any moment
 


## Acknowledgements

 - [Virtual Mouse](https://youtu.be/8gPONnGIPgw)
 - [Finger Counter](https://youtu.be/p5Z_GGRCI5s)
 - [Face Mask Detection](https://youtu.be/Ax6P93r32KU)


## Python Libraries

* opencv
* medipipe
* autopy
* pyttsx3
* threading
* tkinter
* tensorflow
* keras
* time, math, numpy




