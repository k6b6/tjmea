{
	"name": "Tgme3Ze",
	"description": "A TeleGramBot to send messages secretly!",
	"logo": "https://telegra.ph/file/5116db79f852db113875c.jpg",
	"keywords": [
		"telegram",
		"bot",
		"python",
		"telethon"
	],
	"repository": "https://github.com/Source-Ze/tgme3",
    "env": {
        "TG_BOT_TOKEN": {
            "description": "Your Telegram Bot Token from @BotFather",
            "value": ""
        },
        "API_HASH": {
            "description": "Your API Hash from my.telegram.org",
            "value": ""
        },
        "APP_ID": {
            "description": "Your APP ID from my.telegram.org",
            "value": ""            
	   }
	},
	"buildpacks": [
		{
			"url": "heroku/python"
		}
	]
}



