Article URL: https://support.optisigns.com/hc/en-us/articles/20879903340947-how-to-use-content-tags-in-the-playlist

# How to Use Content Tags in The Playlist

## Want more control over which assets and tags in your playlist display on
your screen? Follow this guide to learn more!

Plan required:  
---  
This feature is only available in OptiSigns' **Pro Plus or above plans.**  
  
Content tagging in a playlist allows you to better control and customize the
playback of your playlist items, enabling you to mix and match content for
different screens within the same playlist and greatly simplifying screen
management. By using content tags, you can set rules for your screens that
determine which tagged assets or sub-playlists are displayed when your
selected playlist is playing. This ensures precise and efficient control over
the content displayed on each screen, eliminating the need to create separate
playlists for different locations or scenarios.

**Let's jump in and get started:**

In your Playlist settings by clicking on the **Cog** icon > Selecting
**Advanced** > Click on **Target tags** dropdown menu.

  * **Use Playlist Default:** You can create a tag(s) for the entire playlist. 
    * _For example, this is useful if you use nested playlists. When setting up rules in the next steps, you can either include or exclude entire playlists based on their tags._

  * **Use Asset Default:** The playlist will follow each individual assets' tags.

## **How to Set Up 'Use Asset Default'**

Create a tag for your desired assets in the Files/Assets page. Follow **[this
guide](https://support.optisigns.com/hc/en-us/articles/360056397634-Asset-
Tagging-How-does-it-work)** to learn more on how to do this.

  
Add all items to the playlist. Follow **[this
guide](https://support.optisigns.com/hc/en-us/articles/28295104605843)** if
you need more information on this step.

In your Playlist settings by clicking on the **Cog** icon > Selecting
**Advanced** > Select **Use Asset Default** in the **Target tags** dropdown
menu.

Then go to **Screens page** > Click **Edit** on your preferred screen > Assign
your playlist > Select **Advanced** > Click on **Content Tag Rule** dropdown
menu > Select **\+ New**.

**Setup** your **Content Tag Rule** for your screen to control which content-
tagged assets or sub-playlists are displayed when your selected playlist is
playing.

**What does inclusion and exclusion rules mean?**

**Inclusion** | **Exclusion**  
---|---  
**And:** Will show assets that have all the tags selected. **Or:** Will show any asset with at least one of the tags selected. |  **And:** Will **not show** any assets that have all tags selected. **Or:** Will **not show** any asset with at least one of the tags selected.  
  
  * **\+ Rule:** Will add an additional box for you to add more tags.
  * **+Ruleset:** Will create additional rules to attach to your original tag rules. 

In this example, any assets **with the location-A tag** in the selected
playlist **will** **display** on this screen. Other assets in this playlist
**without location-A tag will not display** on the screen.

## **How to Set Up 'Use Playlist Default'**

When you choose 'Use Playlist Default,' you set a tag for the entire playlist.
The assets within the playlist that are set to 'Use Playlist Default' will
automatically be tagged with the playlist default tag you set at the playlist
level.

**Note:** These tags do not affect the tags you have placed on your
files/assets page.  
---  
  
****

Similar to using 'Use Asset Default', if you set your **Content Tag rule** to
**include or exclude any assets** with the **same default tag as the
playlist** in the selected playlist, then only those assets **will be
displayed** on the screen.

Other assets in the playlist **without the same tag** **will not be
displayed** on the screen.

**NOTE**  
---  
Letter case matters. Ensure when pairing Playlist tags to your screen that the
tags match _exactly._  
  
### **Custom Content Tagging**

If you want a specific asset or nested playlist to have a different tag,
follow these steps:

  * Select the **asset** or **nested** **playlist** within the current playlist.
  * Click the **cog** **icon** next to it.
  * Change the Target tag from '**Use** **Playlist** **Default** ' to '**Custom**.'
  * Input your desired tag in the box below '**Custom**.'

**Example Scenario**

To help illustrate how this feature works, we will use the following simple
scenario as an example:

> A hotel has one screen in the lobby and one screen in the back room. There
> is one global playlist pushed to both screens, but I want to control which
> assets within the global playlist play on each screen.

**IMPORTANT NOTE**  
---  
These Content Tag rules **will not** apply to screen Previews. This is because
Previews are limited by web browser - your screen, however, should display
properly.  
  
  * **Lobby Display:** Suppose your global playlist is tagged 'Front-Lobby' as the Playlist default. All assets within this playlist will be tagged as 'Front-Lobby.'

  * **Back Room Display:** If you have a specific asset you want to play in the back room within the global playlist, you can tag that asset as 'Back-Room'. 

  * **Edit Screen > Selective Content Display:**

On the Edit Screen level, you can set your content rule for your Front Lobby
screens. In this example, the content tag rule is set to **include** items
tagged as **'Front-Lobby'**. This way, the screen will only display assets
tagged as 'Front-Lobby' from your global playlist and ignore any assets or
sub-playlists that do not have the 'Front-Lobby' tag. So, anything tagged
Back-Room will not display.

****

For your screens in the Back Room, you can set your content rule to
**include** items tagged as **'Back-Room'**. This way, only assets tagged as
'Back-Room' from your global playlist will be displayed, and any assets or
sub-playlists that do not have the 'Back-Room' tag will be ignored. So,
anything tagged Front-Lobby will no display.

You also have the option to set an exclusion rule, which will prevent any
assets with specific tags from being displayed on the selected screen.

By following these steps, you can efficiently manage and customize tags for
playlists and individual assets.

**That's it!**

