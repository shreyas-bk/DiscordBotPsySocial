import os
import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

global control
control = True

global counter
global phase 
global scoring_results
global end_experiment

phase = 'Lesson'
counter = 0
scoring_results = 'You got 5/6...'
end_experiment = 'Done with experiment'

lessons = [
  'lesson1',
  'lesson2',
  'lesson3',
  'lesson4',
  'lesson5',
  'lesson6'
]

tests = [
  'test1',
  'test2',
  'test3',
  'test4',
  'test5'
]

questions = [
  'question1',
  'question2',
  'question3',
  'question4',
  'question5'
]

def lesson(counter):
  return lessons[counter]

def test(counter):
  return tests[counter]

def question(counter):
  return questions[counter]
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global control
  global counter
  global phase
  global scoring_results
  global end_experiment

  if message.author == client.user:
    return
    
  if message.content.startswith(('start','1','2','3')) and phase=='Lesson':
    if counter==6:
      phase = 'Test'
      await message.channel.send(test(0))
      counter = 1
    else:
      await message.channel.send(lesson(counter))
      counter = counter + 1

  if message.content.startswith(('a','b','c','d')) and phase=='Test':
    if counter == 5:
      phase = 'Score'
      await message.channel.send(scoring_results)
      if not control:
        phase = 'Interview'
        await message.channel.send(question(0))
        counter = 1
      else:
        phase = 'Done'
        await message.channel.send(end_experiment)
    else:
      await message.channel.send(test(counter))
      counter = counter + 1
      
  if message.content.startswith(('1','2','3','4','5','6','7','8','9','10')) and phase=='Interview':
    if counter==5:
      phase = 'Done'
      await message.channel.send(end_experiment)
    else:
      await message.channel.send(question(counter))
      counter = counter + 1
    
client.run(os.getenv('TOKEN'))