import textwrap

from disnake.ext import commands
import disnake

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = textwrap.dedent((f"""
        **General**
        `{self.bot.prefix[0]}help` - help command 
        `/help` - also a help command
        **Grades**
        `/mygrade [username] [password]` - dms you your grades and other stats to you
        """))

    @commands.command()
    async def help(self, ctx):
        embed = disnake.Embed(title="Help Panel", description=self.description, color=disnake.Color.blurple())
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.slash_command(name="help", description="A help command!")
    async def slash_help(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="Help Panel", description=self.description, color=disnake.Color.blurple())
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Requested by {inter.author.name}", icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

