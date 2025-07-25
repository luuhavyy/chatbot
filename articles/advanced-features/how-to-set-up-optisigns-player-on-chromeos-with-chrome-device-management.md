Article URL: https://support.optisigns.com/hc/en-us/articles/360054033374-how-to-set-up-optisigns-player-on-chromeos-with-chrome-device-management

# How to set up OptiSigns Player on ChromeOS with Chrome Device Management

Chrome boxes are common for large-scale digital signage deployment as there
are industrial-grade chrome boxes such as [AOpen Commercial
Chromebox](https://amzn.to/33Zcu22) or [ASUS
Chromebit](https://amzn.to/2FS8FDP)

Chrome devices are very stable, and provide excellent performance, they can
also be managed by Google Chrome Device Management which will simplify your
large-scale deployment, ensure enterprise security, and reduce device
management overhead. You can learn more about Google's Chrome Device
Management
[here](https://support.google.com/chrome/a/answer/1289314?hl=en#:~:text=Enforce%20policies%20and%20manage%20apps&text=You%20can%20make%20Wi%2DFi,Manage%20policies%20for%20Chrome%20devices.).

## Set up OptiSigns Player on your device with Chrome Device Management

1) Setting Up ChromeOS Digital Signage Players for Automatic Provisioning with
OptisSgns.

2) Using OptiSigns' Web portal to assign content and manage your screens.

Note: For large deployments, you can also use auto-provisioning templates to
skip step 2. For more information, please check
[here](https://support.optisigns.com/hc/en-us/articles/17353256033811).

So let's dive in!

## 1) Setting Up Optisigns on ChromeOS Device as a Digital Signage Players

First, you need to use Chrome Enterprise and Single App Kiosk Mode. This
allows you to manage Chrome devices to boot directly into the OptiSigns
application. You can remotely manage the devices, update security patches,
update the OptiSigns application, and set up in Kiosk …etc.

### 1 Chrome Enrollment and Set up

**1.1 You need to have Google Enterprise Single App Kiosk Licenses**

Chrome Enterprise is Google's management system, and it lets you manage
multiple Chrome devices through a single interface. You check
[here](https://chromeenterprise.google/) for purchasing Chrome Enterprise
licenses.

**1.2 Enroll your ChromeOS Digital Signage Players**

[Click here](https://support.google.com/chrome/a/answer/1360534?hl=en) for
Google Enterprise instructions to enroll your devices.

### 2 Add Optisigns app to your devices

Once your Chrome Device is enrolled in Chrome Device Management, you can add
OptiSigns to your Google Device via Device Management Portal

  * Go to[ Google Admin](https://admin.google.com/) and login to your Google account
  * Click “**Devices** ”

  * Click “**Chrome devices** ”

  * Click on the "**Chrome** " at the top left of the page

  * Go to“**Apps & Extensions**”

  * Select your "**Organizational Unit** ", "**Kiosks** " and then "**Add Chrome app or extension by ID"**

  * Enter Optisigns ID: **ankpffnbahhgegojammhgdnbmdbfnnfe** in “Add chrome app or extension by ID"

  * Once the Optisign has been added, set the app to **Auto-launch** , and SAVE it

  * Go back to the Chrome Management page, select **Device settings** :

  * In the Device settings, go to the **Sign-in settings section** , and set the following: 
    * Guest mode to “**Disable guest mode** ”
    * Sign-in restriction to “**Do not allow any user to sign in** ”
    * User data to “**Do not erase local user data** ”

  * Go to **Kiosk settings section** , set the Managed guest session to “**Do not allow managed guest sessions** ”

## 2) Pair the app with OptiSigns portal & assign content.

If you set up Kiosk mode correctly in previous step, OptiSign App will be
launched automatically when device is started, and it will generate a pairing
code like below.

You now can go to our portal at: [https://app.optisigns.com/
](https://app.optisigns.com/)to pair the screen.

Once you logged in Click "Add screen" button

In this pop-up, type in the Pair Code showing up on the OptiSigns App. Then
Click Pair.

The OptiSigns App will change to:

Now you are ready to upload and assign content.

**1\. Upload video/ image to your account:**

Log on to your account. Click Files/ Assets

Click Upload Files

In this pop up, click to browse the file or drag and drop your files here.

**2\. Create a Playlist:**

Go to Playlist Tab: Click Create Playlist A "New Playlist" will appear at the
bottom on the screen. Click on it.

Click on the pencil button to change Playlist name.

Change it to something meaningful for you. In this case, we will name it
"Lobby TV Playlist"

Drag and drop Video/Images that you uploaded to the playlist.

When you are done, it should look something like below.

You can click on the pencil button next to the item duration loke below to
change the duration of the item on the playlist.

**3\. Assign the playlist to your screen:**

Go to the Screen tab.

Click the "Edit" button on the screen you want to change.

Click the Type drop-down list and select Playlist.

Click the Selected Playlist drop-down and select the playlist you've created.
In this case we select "Lobby TV Playlist"

Click Save.

**The Screen will be updated.**  
  
If you want to change the playlist, add, remove Video/Image, change duration,
etc.  
  
You can go back to the Playlist tab and make the change to the playlist.  
  
The device will update automatically.  
  
You can also start using Apps like Google Slides or set up a Schedule for your
content.

If you have feedback on how to make the how-to guides better, please let us
know at: [support@optisigns.com](mailto:support@optisigns.com)

