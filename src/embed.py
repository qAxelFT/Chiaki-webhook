from src import checkDay

def embeded(image):

    message = {
        "content": "<@&832774619344666634>", # <@&832774619344666634>
        "allowed_mentions": {
            "parse": ["roles", "users"],
            "users": []
        }
    }

    message["embeds"] = [
        {
            "title": "Feliz {ftoday}".format(ftoday=checkDay.today()),
            "color": "14272194",
            "image":
            {
                "url": image
            },
            "footer":
            {
                "text": "De parte de tu waifu gamer favorita",
                "icon_url": "https://cdn.discordapp.com/attachments/778122416618209293/832719192334663730/geimboi.gif"
            }
        }
    ]

    return message