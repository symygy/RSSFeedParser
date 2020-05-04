# RSSFeedParser
The script checks if there is a new podcast episode about Python. If so, a notification email will be sent.

Description:
1. The first time you run the script, the 'data.db' database file is created and configured on HDD.
2. The script writes to it last episodes found at: https://talkpython.fm/episodes/rss
3. Then it starts periodically to check again if new content has been found
4. If so, the data for the new podcast is saved to the database
5. An email is created that is sent to the pre-defined account with a notification abount new episode
6. The notification includes: episode number, title and a podcast link

ATTENTION:
It is required to obtain the authorization code for the Google email address to make script work properly. Enter this data into the file: config.py

