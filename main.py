from dotenv import load_dotenv
import os
load_dotenv()

from GradeBot import GradeBot
from GradeBot import GetGrade
from GradeBot import Info

bot = GradeBot()


if __name__ == '__main__':
    bot.add_cog(GetGrade(bot))
    bot.add_cog(Info(bot))
    bot.run(os.getenv("TOKEN"))