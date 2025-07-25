Article URL: https://support.optisigns.com/hc/en-us/articles/360044614514-there-s-no-sounds-output-for-my-raspberry-pi

# There's no sounds output for my Raspberry Pi

Make sure you setting audio out to the right output.

**Solution 1:**

To change audio output, right click on the audio icon and select the output.

If you are using Raspberry Pi 4, as of 3/12/2020 there's some know issues
output audio to both HDMI ports. Use the port next to the power input, it
works.

**Solution 2:**

Open the **Terminal,** run command line, use this command to switch the audio
output to HDMI:

    
    
    amixer cset numid=3 2

If output is set to `2`, which is HDMI. Output to `1` is analogue (headphone
jack). Default setting is `0` is automatic.

**Solution 3:**

Open the **Terminal,** run command line.

    
    
    sudo raspi-config

Select **System Options**.

Select **Audio**.

Select **0HDMI**

Then select **Finish**

After that, run reboot in the command to reboot your Raspberry Pi

If you have feedback on how to make the how-to guides better, please let us
know at: [support@optisigns.com](mailto:support@optisigns.com)

