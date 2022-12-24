import os
import sys
import Game
import helpers
import constants

try:
  assert sys.version_info >= (3, 0)
except:
  print('error: use python 3.0 or higher')
  exit()

def main():
  chessGame = Game.Game()
  chessGame.initGame()

  while True:
    cmd = input('sweetchess $ ')

    if cmd == 'b':
      helpers.drawChessBoard(chessGame.board, 'pieces')

    if cmd == 'f':
      helpers.drawChessBoard(chessGame.board, 'fields')

    if cmd[:9] == 'test chkf':
      cmd = cmd.split(' ').pop()
      print(helpers.getBoardField(chessGame.board, cmd[0], cmd[1]))

    if cmd[:7] == 'test fp':
      cmd = cmd.split(' ').pop()
      cmd = [x for x in cmd]

      found = None

      if len(cmd) == 2 and cmd[1] in constants.COLS:
        found = helpers.findPiece(chessGame.board, { 'name': cmd[0], 'color': chessGame.playerSide }, cmd[1])
      elif len(cmd) == 2 and cmd[1] in constants.ROWS:
        found = helpers.findPiece(chessGame.board, { 'name': cmd[0], 'color': chessGame.playerSide }, None, cmd[1])
      else:
        found = helpers.findPiece(chessGame.board, { 'name': cmd[0], 'color': chessGame.playerSide })

      print(found)

    if cmd[0] == 'm':
      cmd = str(cmd).split(' ').pop()
      chessGame.handleMove(cmd)

    if cmd == 'r':
      chessGame.initGame()
      os.system('cls')
      continue

    if cmd == 'x':
      print('Goodbye!')
      exit()


if __name__ == '__main__': main()
