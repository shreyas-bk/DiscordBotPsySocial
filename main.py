import os
import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

global control
control = False

global counter
global phase 
global scoring_results
global end_experiment

phase = 'Lesson'
counter = 0
scoring_results = 'Congrats! You got 4/5 questions correct. Your answers to the question concerning the Civil War, Revolutionary War, US Space history and Boston Tea Party were correct. The bot provided useful facts for answering these questions. Therefore, this bot performed extremely well.'
end_experiment = 'Done with experiment, thank you for participating!'

lessons = [
  '''Thank you for participating. Today, you  will be working with this bot. The bot will begin by providing you with a factafter which you should indicate how familiar you are with it. The more you know about the topic associated with a fact, the less likely you will  be to receive additional facts on that topic. You will receive a total of 6 facts, from a list of 100 possible facts. After this there will be 5 MCQ's, randomly chosen from a set of 100 questions. 
  
  At the height of the Ice Age, much of the world's water was locked up in vast continental ice sheets. As a result, the Bering Sea was hundreds of meters below its current level, and a land bridge, known as Beringia, emerged between Asia and North America. 
  Please type how familiar you were about this fact on a  scale of 1-3.''',
  
  '''The powerful East India Company, finding itself in critical financial straits, appealed to the British government in 1773, which granted it a monopoly on all tea exported to the colonies. Please type how familiar you were about this fact on a  scale of 1-3.''',
  
  '''Samuel Adams boarded three British ships lying at anchor and dumped their tea cargo into Boston harbor during the Boston Tea Party. Please type how familiar you were about this fact on a  scale of 1-3.''',
  
  '''George Washington was unanimously chosen president and took the oath of office at his inauguration on April 30, 1789. Please type how familiar you were about this fact on a  scale of 1-3.''',
  
  '''President Lincoln delivered the 272 word Gettysburg Address on November 19, 1863 on the battlefield near Gettysburg, Pennsylvania. Please type how familiar you were about this fact on a  scale of 1-3.''',
  
  '''With Project Mercury in 1962, John Glenn became the first U.S. astronaut to orbit the Earth. Please type how familiar you were about this fact on a  scale of 1-3.'''
]

tests = [
  '''Please answer the following questions by typing a, b, or c.
  
  Who was the first U.S. astronaut to orbit the earth, in 1962?
  a - Neil Armstrong
  b - John Glenn
  c - Buzz Aldrin''',
  
  '''Who was the first president of the United States?
  a - George Washington
  b - Abraham Lincoln
  c - Donald Trump''',
  
  '''What was President Lincoln's famous speech at Pennsylvania called?
  a - Gettysburg Address
  b - Infamy Speech
  c - I Have a Dream''',
  
  '''Who was President during Project Mercury?
  a - John F Kennedy
  b - Dwight D. Eisenhower
  c - Richard Nixon''',
  
  '''Which individual was associated with Boston Tea Party?
  a - George Washington
  b - Samuel Adams
  c - Martin Luther King Jr'''
]

questions = [
  '''For each of the following adjectives, please indicate how well it describes  the tutoring session given by the bot on a scale of 1-10.
  
  Analytical.''',
  'Enjoyable.',
  'Polite.',
  'Likable',
  'Informative.'
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
