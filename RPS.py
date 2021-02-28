def rps(play, number):
  if play == 'rock':
    if number == 1:
      return(":fist:(hen)Tie!")
    elif number == 2:
      return(":v:You lucky son of a bitch :weary:")
    else:
      return(":hand_splayed: You lost LMAO")

  elif play == 'paper':
    if number == 1:
      return(":hand_splayed: (hen)Tie!")
    elif number == 2:
      return(":fist: You lucky son of a bitch :weary: <:Fueee:560965186983428096>")
    else:
      return(":v: You lost LMAO")

  elif play == 'scissors':
    if number == 1:
      return(":v: (hen)Tie!")
    elif number == 2:
      return(":hand_splayed: You lucky son of a bitch :weary:")
    else:
      return(":fist: You lost LMAO")