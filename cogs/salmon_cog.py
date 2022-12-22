from discord.ext import commands
import discord
from get_salmonrun_info import get_salmonrun_schedule
from datetime import datetime

from make_image import make_image
class SalmonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # コマンドの記述
    @commands.command()
    async def today(self, ctx):
        schedule=get_salmonrun_schedule()
        if "fail" in schedule:
            await ctx.send("情報の取得に失敗しました")
        else:
            text=""
            for day in schedule[:1]:
                start:datetime=datetime.strptime(day["start_time"],"%Y-%m-%dT%H:%M:%S%z")
                end:datetime=datetime.strptime(day["end_time"],"%Y-%m-%dT%H:%M:%S%z")
                text+=f"{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n"
                stage=day["stage"]["name"]
                text+=f"{stage}\n"
                weapons=day["weapons"]
                for weapon in weapons:
                    text+=f"{weapon['name']}\n"
                text+="\n"
                print(text)
            await ctx.send(text)
    
    @commands.command()
    async def img_generate(self,ctx):
        await ctx.send("予定表の画像を生成します")
        schedule=get_salmonrun_schedule()
        if "fail" in schedule:
            await ctx.send("情報の取得に失敗しました")
        else:
            make_image(schedule,"schedule.png")
            await ctx.send("画像生成が完了しました")

    @commands.command()
    async def schedule(self,ctx):
        try:
            await ctx.send(file=discord.File('schedule.png'))
        except:
            await ctx.send("画像の送信に失敗しました\n予定表の画像がない可能性があります")
    
    


            


# Cogとして使うのに必要なsetup関数
def setup(bot):
    print("salmonCog OK")
    return bot.add_cog(SalmonCog(bot))
