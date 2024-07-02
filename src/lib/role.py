from discord import User, Member

async def choose_role(user: User | Member, id: int):
    role = list(filter(lambda x: x.id == id, user.guild.roles))[0]
    await (user.remove_roles(role) if role in user.roles else user.add_roles(role))