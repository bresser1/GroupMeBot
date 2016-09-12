# GroupMeBot
A bot for your GroupMe that answers questions, insults your friends and scrapes the web for food deals

## Features
The bot can update the name of the group as well as the nickname of it's creator. Additionally, the bot scrapes the Groupon page for a given city for Groupon deals and posts a random one in the group. It also scrapes certain webpages for insults that you can make it direct at your friends and answers questions with the same functionality as a magic8 ball (responding to yes or no questions with a yes/no/maybe/etc).
 
 ## Usage
 Groupme bots receive every message sent in a group as a POST to the callback url your bot uses. This allows them to look for keywords and respond when they are addressed by name. In order to address the bot, simply include the word "Thunderbot," (inclusive of the comma) in your message.
 
 To get food deals:
 Use the format "Thunderbot, get me food in (your city)"
 
 To insult someone:
 Use the format "Thunderbot, insult (person's name)"
 
 To receive an answer to a yes or no question:
 Include "Thunderbot," and a "?" in the message.
 
 
 
