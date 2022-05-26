import disnake
from disnake.ext import commands, tasks
import itertools

from .Grades import GetGrade
from.info import Info

class GradeBot(commands.Bot):
    intents = disnake.Intents.default()
    intents.members = True

    def __init__(self):
        self.prefix = ['g.', 'G.', "g ", "G "]
        self.tos = "GradeBot will *never* store or leak your password and username!"
        super().__init__(command_prefix=self.prefix)
        self.statuss = itertools.cycle(
            [disnake.Game(' - grades drop and rise'), disnake.Activity(type=disnake.ActivityType.watching, name="Your Grades"), disnake.Game(f'{self.prefix[0]}help')])
        self.remove_command('help')
        self.intents = GradeBot.intents

    @tasks.loop(seconds=60)
    async def change_status(self):
        await self.change_presence(activity=next(self.statuss))

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print(f"{self.user.name} is ready")
