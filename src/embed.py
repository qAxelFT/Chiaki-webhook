from src.event import Today, Image, Footer, weekday_en
from src.randomPhrases import phrase
import datetime
import src.console as console


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

    # Verbose output
    prefix = f"{console.Green}[+]{console.Off}"
    console.Verbose(f"{prefix} Today is {weekday_en[datetime.datetime.now().weekday()]}")
    console.Verbose(f"{console.Purple}*{console.Off} Embed Title: {title}")
    console.Verbose(f"{console.Purple}*{console.Off} Embed Image Link: {Image()}")

    return message
