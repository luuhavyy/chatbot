Article URL: https://support.optisigns.com/hc/en-us/articles/1500012522362-how-to-use-the-web-scripting-app

# How to use the Web Scripting App

### Web Scripting is an advanced feature for OptiSigns' Pro Plus subscribers
or higher, enabling users to automate website navigation and form entries
without any coding. This guide will walk you through recording your script,
creating Web Scripting assets in OptiSigns, and using them securely on your
screens.

**In this article**

  1. What is Web Scripting
  2. Record Your Script
  3. Create Web Scripting Asset in OptiSigns
  4. Using It on Your Screens

## What is Web Scripting

Web Scripting is a feature that allows users to automate navigation and form
entry on websites without any coding. This tool records user actions, such as
entering usernames and passwords, navigating to specific pages, handling pop-
ups, running your own JavaScript and more on a website, and then encrypts the
recorded script for secure execution on designated devices.

OptiSigns encrypt all the scripts and your password entered with our own
private keys.

  * This will ensure your data/password is safe as soon as it left your browsers and only get decrypted at device level before the fields are entered.

We also provide Zero Knowledge encryption method so that you can protect your
script with your own Master Password. _You can read more at the end of this
article._

If your dashboard requires login with the 2FA, OptiSigns supports the 2FA in
the Web Scripting app. You can read more
[here](https://support.optisigns.com/hc/en-us/articles/19145077187859).

**Let's jump in and get started!**

**NOTE**  
---  
Web Scripting is not supported on Samsung SSSP or LG WebOS smart TVs.  
  
##  **Record Your Script**

****

In this article, we will show you how to use a tool called Burp Suite
Navigation Recorder. You can use other tools if that can generate similar
scripts that works too. We recommend Burp Suite because it's a reputable tool
used by many companies, including the Fortune 500.

**1\. You need to install Burp Suite Navigation Recorder.**

Open **Chrome Browser**.

Go to Chrome Web Store:
<https://chrome.google.com/webstore/category/extensions>

Search for: "**Burp Suite Navigation Recorder** ".

Click on it.

Then click **Add to Chrome.**

Burp Suite Navigation Recorder is installed

Click on the **Navigation Recorder Icon.**

Then click **Open Settings** to finish set up.

Scroll down and click **"Allow in Incognito".**

Close this tab.

Now, if you click on the Navigation Recorder icon again, you will have option
to Start Recording.

**2\. Record your Script**

From the Navigation Recorder extension pop out like in above screenshot, click
**Start Recording.**

It will open an **Chrome Incognito window**.  
You can put in the URL of the website or page you want to start with.  
Then fill out the forms. (such as, entering your username, password and click
Login)

### **Important Notes to Follow to Reduce Issues Later!**  
  
---  
**Always start with the destination URL** (The URL of the page you want to
display). Let the website handle the redirection once you fill out the login
information.  
**Always click the Login button,** instead of Enter.  
**Correctly enter your fields in 1 attempt!** Type slow and carefully. Don't
use backspaces or arrows keys to modify. If you mess up, please restart this
step from the beginning.  
  
You can click around, navigate to certain page, position on page etc.

Once you are done, click on the **Navigation Recorder Extension icon** and
click **Stop Recording.**

This will close the Incognito window that you are working on.

Go back to Chrome, click **Navigation Recorder icon.**  
Click "**Copy to Clipboard** ". This will copy your script to clipboard.  
Now you are ready to put in use in OptiSigns.

## **Create Web Scripting Asset in OptiSigns**

Log in to OptiSigns <https://app.optisigns.com/>

Click **File/Assets**

Click **Apps** and select **Web Scripting.**

Enter the information for your Web Scripting asset:

  * **_Name_ :** Name of your asset your asset list. It will _**not**_ be displayed on your screens.
  * **Master Password: **By default, OptiSigns will encrypt the whole script with OptiSigns private key to protect your script, especially username, password in the script. You can add another protection layer by entering a Master Password. If you enter Master Password here, at each device, you will need to enter that Master Password one time in OptiSigns app so it can decrypt the content. 
  * **_Recorded Script:_** Paste the script recorded by the Navigation Recorder here. You can take notice to the script, it's actually not very complicated, you can make some minor changes if you need to.

**Here's how the encryption flow works:**

If you want to add additional security by utilizing a Master Password and our
Zero Knowledge Encryption framework you will have to enter your Master
Password when:

  * Creating/editing assets
  * One time at each devices, so it will know how to decrypt

Your script is encrypted at your browser, and transfer securely using
HTTPS/SSL during transits and stored on our servers.  
It then sends securely to devices, and decrypted at device level right before
executing on the target website.

## **Using It on Your Screens**

Once created, the Web Scripting asset can be used in by itself or in
Playlists, Schedules, or SplitScreen zones just like any other assets.

If you don't use Master Password, device will use OptiSigns private key to
decrypt and execute, so no additional action is needed on the devices.

If you choose to use Master Password and our Zero Knowledge Encryption
framework, you will have to enter your Master Password at each device

  * This only needs to be done once on each device and can be used to decrypt all Scripting Assets. (Of course, you have to use the same Master Password to encrypt them).

## **That's all!**

Congratulation, you have created Web Scripting assets, now you can
automatically log in to gated websites, navigate to pages as needed.

If you have any additional questions, concerns or any feedback about
OptiSigns, feel free to reach out to our support team at
[support@optisigns.com](mailto:support@optisigns.com)

