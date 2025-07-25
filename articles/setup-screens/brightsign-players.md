Article URL: https://support.optisigns.com/hc/en-us/articles/5090125683219-brightsign-players

# BrightSign Players

BrightSign is the leader in commercial grade digital signage players, which is
known for its reliability. OptiSigns provides full support on BrightSign
player, however we do recommend using the HD, XD, and XT product lines for
better performance.

It is very easy to setup OptiSigns on BrightSign players. There are 2 ways you
can set it up. You can set it up in standalone mode, or you can set it up on
BSN.cloud.

## Option 1: Setup with BSN.cloud

**1) Download BrightAuthor**

The latest BrightAuthor can be downloaded
[here](https://www.brightsign.biz/digital-signage-
products/software/brightauthor).

**2) Logon to your BSN.cloud account and select device setup**

**3) Complete the device setup**

Fill in the value in the package and device name.

Select "Partner Application" under Device Type. Click "Select a Partner
Application" and find "OptiSigns".

Then click "Save Setup File" to save the generated setup files.

**4) Copy the setup files to your storage device.**

Place the generated setup files in the root directory of your SD card.

**5) Insert the SD card to the player and let it finish the setup**

The BrightSign player will read the setup files and complete the setup
automatically. It will take a few minutes and may reboot a few times.

Once the setup process is complete, you will see OptiSigns player running on
your screen with the pairing code showing up on the screen.

Please make sure your BrightSign player is connected to the internet.

**6) Pair the screen**

Now you are ready to go to our portal at: <https://app.optisigns.com/>

Pair the screen using your screen's code and start assigning content to it.

For detailed steps click [here](https://support.optisigns.com/hc/en-
us/articles/360016374813).

## Option 2: Standalone Mode

**1) Download the autorun file.**

The latest autorun.zip file can be downloaded
[here](https://links.optisigns.com/brightsign).

**2) Copy the autorun file to your storage device.**

The autorun.zip file should be placed in the root of your SD card.

**3) Insert the SD card to the player and let it finish the setup**

The BrightSign player will read the data from the autorun file and complete
the setup automatically. It will take a few minutes and may reboot a few
times.

Once the setup process is complete, you will see OptiSigns player running on
your screen with the pairing code showing up on the screen.

Please make sure your BrightSign player is connected to the internet.

**4) Pair the screen**

Now you are ready to go to our portal at: <https://app.optisigns.com/>

Pair the screen using your screen's code and start assigning content to it.

Once you pair the screen and start assigning content to it, you can follow
these guides for more detailed steps:

  * [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)
  * [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
  * [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
  * [Create and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)

## Updating BrightSign Software

If you have further issues running OptiSigns, it's possible you have an
outdated version of the BrightSign software. We recommend updating it.

The latest version of BrightSign software can be found
[here](https://www.brightsign.biz/resources/software-downloads/).

## How to Update the BrightSign Registry to Use Newer Versions of Chromium

A common issue we find is that BrightSign may need a registry update in order
to display newer versions of Chromium. This is a particular issue with
displaying PowerBI.

To do this, open up BrightAuthor:connected and navigate to **Admin:**

Now you'll need to obtain the IP of your BrightSign player. Input the IP
address into your browser (your device must be on the same network as the
BrightSign player). If you've done things correctly, you will enter the player
config menu.

Once there, navigate to **Registry** :

From this

Next, input the following command:

    
    
    registry write html widget_type chromium110

When you hit submit, you'll see this:

This will allow your BrightSign player to use the latest versions of Chromium.

### That's all!

Now you are ready to use OptiSigns on your BrightSign players.

If you have any additional questions, concerns or any feedback about
OptiSigns, feel free to reach out to our support team at
[support@optisigns.com](mailto:support@optisigns.com)

