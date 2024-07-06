from discord import Embed

def must_field_embed(embed: Embed, fields: list) -> Embed:
    for i in fields:
        embed.add_field(name=i[0], value=i[1])
        
    return embed

if __name__ == "__main__":
    print("dada878", f"{'▮'*round((point := __import__('random').randint(0, 100))/10) + '▯'*(10-round(point/10))} {point}% Gay", sep="\n")