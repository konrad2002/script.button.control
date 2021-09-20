import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Set a string variable to use 
line1 = "JAJA hier schau, ich kann dialoge anzeigen.."
line2 = "Herzlichen Glückwunsch, willste jetzt nen Keks?!?"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1, line2)
