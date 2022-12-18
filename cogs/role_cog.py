from discord.ext import commands


# Rolecogクラス(試作中　思った感じでは動かない)
class RoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles = []

    def role_exist(self, name):
        for role in self.roles:
            if role.name == name:
                return True
        return False

    # コマンドの記述
    @commands.command()
    async def rolelist(self, ctx):
        if len(self.roles) == 0:
            await ctx.send("rolelist is empty!")
        else:
            out = ""
            for i, role in enumerate(self.roles):
                out += f"{i}:{role.name}\n"
                await ctx.send(out)

    @commands.command()
    async def addrole(self, ctx, role_name):
        if self.role_exist(role_name):
            await ctx.send("this role is already exist in list!")
        else:
            for role in ctx.guild.roles:
                if role.name == role_name:
                    self.roles.append(role)
                    ctx.send(f"{role.name} is added ")
                    break
            else:
                ctx.send("this role was not found...")


# Cogとして使うのに必要なsetup関数
def setup(bot):
    print("Rolecog OK")
    return bot.add_cog(RoleCog(bot))
