Article URL: https://support.optisigns.com/hc/en-us/articles/4411956075027-clean-install-optisigns-on-raspberry-pi-linux

# Clean install OptiSigns on Raspberry Pi/Linux

To completely clean out old installation of OptiSigns on Linux or Raspberry Pi

Please run:

    
    
    rm -rf ~/.config/OptiSigns  
    rm ~/.config/autostart/'OptiSigns Digital Signage.desktop'

Also delete the long string text on this ~/.config folder

Then install the new AppImage download from
<https://www.optisigns.com/download>

