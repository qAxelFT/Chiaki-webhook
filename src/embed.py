from src.event import Today, Image, Footer
from src.randomPhrases import phrase


def Embed():
    # Embed properties
    title = f"Feliz {Today()}"
    text = "De parte de tu waifu gamer favorita"
    color = "14272194"
    footer = {"text": text, "icon_url": Footer()}

    # Build the actual payload with the embed
    message = dict()
    message["content"] = f"<@&832774619344666634> {phrase()}"
    message["embeds"] = [{"title": title, "color": color, "image": {"url": Image()}, "footer": footer}]

    return message
