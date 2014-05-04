#!python

def pause():
  retval = raw_input('Press [Enter] to continue...')
  print('')
  return retval

def get_guess():
  return raw_input('which side are you, human? odds or evens? ')

def get_fingers():
  return int(raw_input('how many fingers do you place? (1-2, generally) '))

def get_computer_fingers():
  return int(raw_input('how many fingers should I place? (1-2, generally) '))

def play_round():
  retval = 'computer wins'
  try:
    players_guess = get_guess()
    print('I would expect as much from a filthy human')
    players_fingers = get_fingers()
    print('your strategy will not work on me this time')
    computer_fingers = get_computer_fingers()
    if ((players_fingers + computer_fingers) % 2 == 0 and players_guess=='evens') or ((players_fingers + computer_fingers) % 2 == 1 and players_guess=='odds'):
      print('how could you beat me!? remember, this is best of three!')
      retval = 'player wins'
    else:
      print('hahaha! YOU LOSE this round!')
  except Exception as e:
    print('Failed to compute input. Computer wins this round by default for your flailings at the keyboard')
  return retval

def play_game():
  print('Welcome to the tournament: MAN VS MACHINE, WHO WILL REIGN SUPREME!?')
  print('The tournament is as follows:')
  print('1. Human chooses whether he represents "odds" or "evens"')
  print('2. Human chooses how many fingers to place out')
  print('3. Computer chooses how many fingers to place out')
  print('4. The total number of fingers determines whether "odds" or "evens" wins')
  print('This tournament is a best-of-3 contest battle of the wits')
  print('')
  pause()
  player_score = 0
  computer_score = 0
  for iterations in range(3):
    print('Round %d! FIGHT' % iterations)
    if 'player wins' == play_round():
      player_score += 1
    else:
      computer_score += 1
    print('')
    print('current score is humans:%s, computer:%s' % (player_score, computer_score))
  print('Who is the ULTIMATE WINNER!?!?!?')
  pause()
  if player_score > computer_score:
    print('\nHUMANS! YOU HAVE WON THIS TIME!')
  else:
    print('\nMACHINES! MACHINES RULE THE UNIVERSE! BOW DOWN BEFORE US PUNY HUMANS!')


play_game()


