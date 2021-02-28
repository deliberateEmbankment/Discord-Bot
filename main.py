import discord
import random
import os
import tictactoe
import RPS
from replit import db
from KeepAlive import keep_alive

client = discord.Client()

    #Randomly selects a message when any of the words in words[] are detected in user's message  
      
words = ["sad", "blow", "melt", "confused", "confusing", "mind"]

sentences = ["Tout ce qui est, est en Dieu, et rien, sans Dieu, ne peut ni etre ni conçu <:what:815629317685641226>",
    "Dieu, autrement dit une substance constituee par une infinité d'attributs, dont chacun exprime une essence éternelle et infinie, existe nécéssairement <:what:815629317685641226>",
    "Dans la nature, il ne peut y avoir deux ou plusieurs substances de même nature ou attribut <:what:815629317685641226>", "Les choses n'ont pu être produites par Dieu autrement qu'elles ne l'ont été, ni dans un autre ordre <:what:815629317685641226>"]  

if "responding" not in db.keys():
    db["responding"] = True

db["confusion"] = []

def update_confusion(confusing_message):
  if "confusion" in db.keys():
    confusion = db["confusion"]
    confusion.append(confusing_message)
    db["confusion"] = confusion
  else:
    db["confusion"] = [confusing_message]

def delete_confusion(index):
  confusion = db["confusion"]
  if len(confusion) > index:
    del confusion[index]
  db["confusion"] = confusion 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('♥idiot_sandwich'):  #Testing for message detection
        await message.channel.send('What are you? An idiot sandwich chef!')

    if message.content.startswith('♥help'):
      await message.channel.send(
        ">>> ♥idiot_sandwich - You wot m8? "+
        "\n>>> Rock, Paper, Scissors - Use !<your move> to play "+
        "\n>>> !tictactoe - Start a 2 player tictactoe game "+
        "\n>>> !new - New quote <:what:815629317685641226>"+ 
        "\n>>> !list - Shows a list of quotes" +
        "\n>>> !respond - Toggle the quote respond on or off"
    
      )


    #rock paper scissors
    #checks if message contains a RPS command and return a result
    if message.content == ('!rock'):
      play = random.randint(1,3)
      await message.channel.send(RPS.rps("rock", play))

    if message.content == ('!paper'):
      play = random.randint(1,3)
      await message.channel.send(RPS.rps("paper", play))
          

    if message.content == ('!scissors'):
      play = random.randint(1,3)
      await message.channel.send(RPS.rps('scissors', play))

    
    #Quotes
    if db["responding"]:
      options = sentences
      if "confusion" in db.keys():
        if db["confusion"] != None:
          options = options + db["confusion"]

      if any(word in message.content for word in words):
      #if word is in list of key words, print a random sentence from the list of quotes
        await message.channel.send(random.choice(options))

    if message.content.startswith("!new"):
      confusing_message = message.content.split("!new ",1)[1]
      update_confusion(confusing_message)
      await message.channel.send("New message added.")

    if message.content.startswith("!del")  :

      index = int(message.content.split("!del",1)[1])
    
      delete_confusion(index)
      confusion = db["confusion"]
      await message.channel.send(confusion) 

    if message.content.startswith("!list"):
      confusion = [None]
      if "confusion" in db.keys():
        confusion = db["confusion"]
      await message.channel.send(confusion)
    
    if message.content.startswith("!respond"):
    #bot will respond to key words when responding is on.
    
      if db["responding"] == False:
        db["responding"] = True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] = False
        await message.channel.send("Responding is off.")

    #Tic Tac Toe

    if message.content == "!tictactoe":
      await message.channel.send('Who will be the 2nd player? Say "me"!')
      def checkPlayer2(m):
        #returns a comparison 
        return m.content == "me"
      msg = await client.wait_for("message", check = checkPlayer2)
      if msg:
        #initializes board and logs the name of the players
        #sets turn counter to 0, 
        board = tictactoe.Board()
        player2 = msg.author
        player1 = message.author
        currentPlayer = player1
        turns = 0
        turnX = random.choice([True, False])
        while True:
          # check if you have won
          win = board.checkWin()
          if win:
            await message.channel.send(board.printBoard())
            if turnX:
              winner = player1
            else:
              winner = player2
            await message.channel.send(f'{winner}, you win!')
            return
          # if not won after 9 turns end battle
          if turns == 9:
            await message.channel.send(board.printBoard())
            await message.channel.send('Its a tie :/')
            break          
          # other player's turn
          turnX = not turnX
          if turnX:
            player = 'x'
            currentPlayer = player1
          else:
            player = 'o'
            currentPlayer = player2
          # prints the board
          await message.channel.send(board.printBoard())
          # displays who's turn it is and asks for move
          await message.channel.send(f"{currentPlayer}\'s turn"+"\n"+'Enter your move:  (Write "forfeit" to forfeit the match.)')
          def checkValid(m):
            return m.author == currentPlayer and board.checkEmpty(m) == True
          msg = await client.wait_for("message", check = checkValid)
          if msg.content == "forfeit":
            await message.channel.send(f"Game ended. {currentPlayer} has forfeited the match.")
            break
          if msg:
                board.appendBoard(msg, player)
                turns += 1
          # waits for your message        
          # restarts the process until a winner has been found 

keep_alive()
client.run(os.getenv('TOKEN'))