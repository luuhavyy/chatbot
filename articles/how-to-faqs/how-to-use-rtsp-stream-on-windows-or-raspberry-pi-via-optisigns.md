Article URL: https://support.optisigns.com/hc/en-us/articles/8066591235603-how-to-use-rtsp-stream-on-windows-or-raspberry-pi-via-optisigns

# How to use RTSP Stream on Windows or Raspberry Pi via OptiSigns 

#### Nowadays, RTSP Camera Streaming is popular. You can display your RTSP
Stream on your Digital Screen via OptiSigns.  

This article will guide you through how to create and use the RTSP Stream app
on Windows or Raspberry Pi. Note: For this feature, you must run OptiSigns
player version 5.3.2 or newer on your devices. You can download the latest
version of the app at
[https://www.optisigns.com/download](http://www.optisigns.com/download)

If you want to use the Fire Stick or Android Stick to display the RTSP Stream
app. The setup will be different. You can click
[here](https://support.optisigns.com/hc/en-us/articles/8098889840531).

Windows and Raspberry Pi don't support the RTSP HTML5 directly. Before you
create the RTSP Stream app, you will need to transcode RTSP to HTTP. Then you
can implement RTSP live streaming on the Windows and Raspberry Pi devices. The
easy way of achieving RTSP HTML5 playback on Windows and Raspberry Pi is to
embed VLC into the HTML5 webpage and adopt it as an HTML5 RTSP player.

### **Let's jump in and get started:**

#### **1\. How to use it on Windows and Raspberry Pi devices.**

Before setting up, you will need to prepare:

  1. Need the VLC Media Player. You can download it [here](https://www.videolan.org/vlc/index.html).
  2. RTSP URL. (Here is an example: rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4)

Then you can follow these steps to set it up.

Step 1. Launch VLC Media Player, go to the "**Media** " > **Open Network
Stream**

Step 2. Go to the "**Network** ", type in the RTSP URL to the "**Network URL**
". We use this as a sample example.
(rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4)

Step 3. Click the dropdown and select "**Stream** ".

Step 4. Click "**Next** "

Step 5. Select "**HTTP** ", and Click "**Add** "

Step 6. Type "**9999** " in the "**Port** " and "**/stream.ogv** " in
"**Path** ". The address of the output stream will be the IP address of "your
native server/stream.ogv". Click "**Next** " to proceed.

Step 7. Select "**Video-Theora+Vorbis (OGG)** ". Then click "**Next** "

Step 8. Check the output media codec at "Generated stream output string", make
sure **vcodec=theo** and **mux=ogg,** otherwise manually modify. Then, click
"**Stream** ".

When it is successful, it will start the run. You can see the screenshot
below.

#### **2\. Now it's time to create the RTSP stream app in OptiSigns Web
Portal.**

Note: Keep VLC running for constantly transcoding, and embedding RTSP stream
HTML5 webpage.

Go to Files/Assets, Click on "App", search for, and add the RTSP Stream app to
your Account.

Enter your RTSP Stream App information:

##

  * _Name_ : Name of your RTSP Stream app, this is the name of the app in your asset list. It will _**not**_ be displayed on your screens.
  * URL: the URL link will be your local IP address with your setup. (http://[Your IP address]:[Port]/[path])

Click Save to save your asset.

## That's all!

Congratulation! You have created your RTSP Stream App. Then you can assign it
to your Windows or Raspberry Pi device.

You can change the wall at any time by clicking on it in the Files/Assets tab.

You can put the walls in a Playlist, Schedule too.

If you have any additional questions, concerns, or any feedback about
OptiSigns, feel free to reach out to our support team at
[support@optisigns.com](mailto:support@optisigns.com)

