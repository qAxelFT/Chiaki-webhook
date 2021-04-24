import datetime
from src import embed

weekday = {
    0: "Lunes",
    1: "Martes",
    2: "Miercoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sabado",
    6: "Domingo"
}


def today():
    return weekday[datetime.datetime.now().weekday()]

def check():

    if today() == "Lunes":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832743405992804423/AAAAAA.jpg")

    elif today() == "Martes":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832731634553585664/Danganronpa_V3_Chiaki_Nanami_Bonus_Mode_Sprites_11.webp")

    elif today() == "Miercoles":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832762755281846302/miercoles.png?width=418&height=461")

    elif today() == "Jueves":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832607051968282704/FelizJueves.jpg")

    elif today() == "Viernes":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832748956555280394/tumblr_66748f35028b507f428bdf16fedcf066_8a5d51ec_400.png?width=296&height=461")

    elif today() == "Sabado":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832786460264366141/sabado.png?width=445&height=461")

    elif today() == "Domingo":
        return embed.embeded("https://media.discordapp.net/attachments/778122416618209293/832789488241213461/aaaaaaaaaaaaaaaaaaaaaaaaaa.webp")