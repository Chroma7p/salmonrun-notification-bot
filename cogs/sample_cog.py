from discord.ext import commands

# samplecogクラス
class SampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # コマンドの記述
    @commands.command()
    async def chkcog(self, ctx):
        await ctx.send("using cog!")


# Cogとして使うのに必要なsetup関数
def setup(bot):
    print("SampleCog OK")
    return bot.add_cog(SampleCog(bot))
