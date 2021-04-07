import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
  print('Bot Is Online!')

@client.command()
async def news(ctx):
  await ctx.send('News:')
  await ctx.send('https://abcnews.go.com/Politics/gaetz-investigation-sex-allegations-sought-blanket-pardon-trump/story?id=76911923&cid=clicksource_4380645_3_heads_hero_live_hero_image')
  await ctx.send('https://edition.cnn.com/2021/04/06/health/covid-neurological-psychological-lancet-wellness/index.html')
  await ctx.send('https://www.nbcnews.com/science/science-news/cdcs-messaging-problem-highlights-pandemics-uncertain-future-rcna602')
  await ctx.send('Run ?morenews For More News')

@client.command()
async def morenews(ctx):
  await ctx.send('Even More News:')
  await ctx.send('https://www.huffingtonpost.co.uk/entry/biden-infrastructure-bill_n_606c9b3ac5b66c4ab6b7eb6f?ri18n=true')
  await ctx.send('https://www.cbsnews.com/live-updates/derek-chauvin-trial-george-floyd-death-2021-04-06/')
  await ctx.send('https://eu.usatoday.com/story/news/2021/04/07/derek-chauvin-trial-covid-vaccine-study-5-things-know-wednesday/7062907002/')
  await ctx.send('https://www.buzzfeed.com/sam_cleal/nerdy-characters-who-are-sexy?ref=hpsplash')
  await ctx.send('https://www.nytimes.com/2021/04/06/world/americas/migration-honduras-central-america.html?action=click&module=Top%20Stories&pgtype=Homepage')
  await ctx.send('https://www.foxnews.com/politics/biden-georgia-smarten-up-avoid-losing-business-new-election-law')
  await ctx.send('https://www.dailymail.co.uk/news/article-9443237/Matt-Gaetz-asked-Trump-pardon-amid-DOJ-sex-trafficking-investigation.html')
  await ctx.send('https://www.washingtonpost.com/national/rochester-police-black-people/2021/04/06/a3a6f004-8e59-11eb-aff6-4f720ca2d479_story.html')
  await ctx.send('https://bleacherreport.com/articles/2939486-if-2020-21-gonzaga-bulldogs-couldnt-go-undefeated-will-it-ever-happen-again')
  await ctx.send('https://www.businessinsider.com/beijing-new-york-city-billionaires-comparison-2021-4?r=US&IR=T')
  await ctx.send('https://www.bbc.com/news/world-latin-america-56657818')

@client.command()
async def helpme(ctx):
  await ctx.send('?news - For News')
  await ctx.send('?morenews - For More News')
  await ctx.send('More Command Coming Soon! (plz respect me, i spent 24 hours only to make this project)')
  await ctx.send('(c) Minecrafter99 2021')
  await ctx.send('Add Command By Contribute In Our Project On Github')

@client.command()
async def credits(ctx):
  await ctx.send('By Minecrafter99')
  await ctx.send('And Thanks To ALL My Contributor On Github For Improve This Project')
  await ctx.send('(did you know that NewsBot is founded in 1939 and secretly powered by 10 quantum robot cats?)')

client.run('ODI5MjUxMDk0NTg3NjM3Nzgw.YG1aQw.Q9HcjqTBNe4tHkN0HFG2ehiNngo')
