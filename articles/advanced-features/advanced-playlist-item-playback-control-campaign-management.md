Article URL: https://support.optisigns.com/hc/en-us/articles/22474034993043-advanced-playlist-item-playback-control-campaign-management

# Advanced Playlist Item Playback Control & Campaign Management

**NOTE**  
---  
This feature is available to **Pro Plus** subscribers or higher.  
  
There are settings available on the playlist for you to control playlist item
playback, you can achieve amazing results with that. In some situations, you
will want to control the item playback in a specific way, for example, if you
have an advertising need, you may want to have the sub-playlist play a couple
of items only each round, or you want to have an ad play once every 30
minutes. These advanced settings are perfect for these situations.

There are 5 advanced settings we will cover in this document.

  1. **Sub-playlist control**. With Sub-playlist control, you can define how many items you want to play from the sub-playlist when the sub-playlist is embedded as a nested playlist. It can help you better manage the time allocation of a certain type of content.
  2. **Resume on next play**. With this enabled, the playlist will start from where it left off last time, instead of starting from the beginning. This may provide a better experience when the playlist has to be interrupted for any reason. 
  3. **Split Screen primary zone with playlist**. This will provide a better experience or more smoother content transition if you use Split Screen to organize relevant content together and put it as an item in a playlist. The playlist will respect the duration of the content in the primary zone and let its playback finish before moving to the next item in the playlist.
  4. **Play Every Setting**. With this, you can define how you want to have the item repeated. For example, if you have a contractual agreement that an ad will play once every hour, this setting will put a timer on the item, and try to play it once every hour.
  5. **Content Tagging:** This allows you to better control and customize the playback of your playlist items, enabling you to mix and match content for different screens within the same playlist and simplify screen management. You can set rules for your screens that determine which tagged assets or sub-playlists are displayed on each screen.

#### **1) How to use sub-playlist control**

The setting is available in the playlist options.  
Click on the playlist options if you want to set it for a certain playlist, so
when that playlist is used as a sub-playlist in other places, it will inherit
the setting.

Or configure it at the playlist item level for a sub-playlist, the setting
will only be applied on the playlist.  

Once the Sub-playlist control is enabled, there are 2 settings available for
you to control.

  * Rotate X items: This defines how many items will be played each round in the sub-playlist. For example, if you set 2 here, whenever it comes to this sub-playlist, it will play 2 items. When all items are played, it will start over.
  * Max duration per item: This provides a way to better control the time of the playback to avoid anomalies. For example, if you set the value to 120 seconds, any item in the sub-playlist cannot play more than 2 minutes, even if a long video is accidentally placed in the sub-playlist, it will be cut when it reaches 2 minutes. 

#### **2) How to use resume on the next play**

Using a resume on the next play is simple. Just open the playlist options and
get it enabled, then the playlist will always resume from where it left off
last time and start playback from that point. This can resume from the middle
of the video files as well. For example, if there is a 5-minute video in the
playlist, you set the duration to 1 minute in the playlist, if this setting is
enabled, the next time when it loops back to the video, it will play the next
1 minute instead of starting from the beginning each time.

#### **3) How to use split-screen primary zone with playlist**

Using the primary zone in split-screen can help you get more smoother
transition when the split-screen is used inside the playlist. A common use is
to use split-screen to organize similar contents together, e.g. the main zone
is playing a work safety video, and you would like the side zone to show some
safety-related messages as well.

When there are many split-screen assets inside a playlist, you would like it
to transition to the next item when the primary zone's playlist item is
complete rather than follow the duration setting of the split-screen asset.
This is a great way to avoid videos being cut off early.

To use the primary zone setting, just open the configs popup of the split-
screen asset, and then you can select which zone will be the primary zone.
Once the primary zone is selected, 2 settings can help you to control it.

  * Select zones that use primary zone timing: This will help match the duration of the contents from the selected zones to the Primary Zone.  

    * Example: Playlist A has four videos of varying durations placed in the primary zone. Playlist B has four different images placed in the selected zone. The four images in playlist B will re-calculate each duration individually to correspond to the matching asset duration playing in the Primary Zone. Note that this feature only works if Playlist A and Playlist B have the same number of assets.
  * Respect primary zone video timing: With this checked, when the split screen asset is put as an item inside a playlist, the player will respect the duration of Primary Zone's playlist, and let it finish playback before transitioning to the next item. 

#### **4) How to use play every feature**

Play every feature allows you to control the playback of the playlist items at
a repeated interval. What's more, it is not simply playing the item at the set
interval, it will wait until the last item playback is completed, then kick in
to provide a smoother transition and a better experience.

Major use would be if you would like to reinforce the message, or if you have
a contractual agreement to provide exposure to content e.g. every hour.

It is very simple to use the play every feature, just click the setting button
of the item, then set the interval accordingly. Once it is set, you will see a
timer-like icon on the item, which will help you easily identify the items
that play every feature enabled.

Please note, the play every feature will only work in the root level playlist,
when it is set in the sub-playlist it will not work. Also, when playing
everyone is set on the item, the item playback will be controlled by the
interval set, and the position where the item is placed in the playlist will
not matter.

**5\. How to use content tags in a playlist**

To first use content tags, you will need to assign tags to either individual
assets or an entire playlist. To learn more about asset tagging and how it
works, please follow **[our guide on Tagging in
OptiSigns.](https://support.optisigns.com/hc/en-
us/articles/38062664690195-Tagging-in-OptiSigns)** You can tag playlists by
going to your desired playlist, opening the playlist options, changing Target
Tags to "Use Playlist Default", and inputting any tags you'd like. This tag
will apply to everything within the playlist, unless you assign custom tags to
assets within a playlist.

Now, you can head over to your desired screen and create Content Tag Rules on
the edit screen level. By using the inclusion and exclusion boxes, you can
choose which tagged assets appear or don't appear when content is pushed to
your screen. For example below, by using "Inclusion > And > Front-Lobby", when
that specific playlist is pushed to the screen, it will only show content
tagged as Front-Lobby, it will exclude or skip over anything tagged something
else.  
  
See our full article on **[Content Tagging in
Playlists](https://support.optisigns.com/hc/en-us/articles/20879903340947-How-
to-Use-Content-Tags-in-The-Playlist)** for more information.

**That's all!**

If you have any additional questions, concerns, or any feedback about
OptiSigns, feel free to reach out to our support team at
[support@optisigns.com](mailto:support@optisigns.com)

