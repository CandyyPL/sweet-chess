import constants
import helpers
import random

class Game:
  board = []

  sides = ['white', 'black']
  playerSide = ''

  piecesInGame = 32
  whitePieces = 16
  blackPieces = 16

  def __init__(self):
    pass

  def initGame(self):
    self.board = []
    self.makeFields()
    self.playerSide = random.choice(self.sides)
    self.populateBoard()

  def makeFields(self):
    cols = constants.COLS
    rows = constants.ROWS

    i = 1

    for r in rows:
      for c in cols:
        field = {
          'name': f'{c}{r}',
          'color': '',
          'taken': False,
          'piece': {}
        }

        if i % 2 == 0:
          color = 'black'
        else:
          color = 'white'

        field['color'] = color

        self.board.append(field)

        i += 1
      i -= 1

  def placePiece(self, row, col, piece):
    for f in self.board:
      if f['name'] == f'{col}{row}':
        f['piece'] = {
          'name': piece,
          'color': '',
          'pinned': False
        }

        if self.playerSide == 'white':
          if row in ['1', '2']:
            f['piece']['color'] = 'white'
          elif row in ['7', '8']:
            f['piece']['color'] = 'black'

        if self.playerSide == 'black':
          if row in ['7', '8']:
            f['piece']['color'] = 'white'
          elif row in ['1', '2']:
            f['piece']['color'] = 'black'

        f['taken'] = True

  def populateBoard(self):
    for f in self.board:
      col = f['name'][0]
      row = f['name'][1]

      if row in ['2', '7']:
        self.placePiece(row, col, constants.PAWN)

      if row in ['1', '8']:
        if col in ['a', 'h']:
          self.placePiece(row, col, constants.ROOK)

        if col in ['b', 'g']:
          self.placePiece(row, col, constants.KNIGHT)

        if col in ['c', 'f']:
          self.placePiece(row, col, constants.BISHOP)

        if col == 'd':
          self.placePiece(row, col, constants.QUEEN)

        if col == 'e':
          self.placePiece(row, col, constants.KING)

  def makeMove(self, src, dst, piece):
    for f in self.board:
      if f['name'] == src:
        f['piece'] = {}
        f['taken'] = False

      if f['name'] == dst:
        f['piece'] = piece
        f['taken'] = True

  def handleMove(self, move):
    if len(move) == 2 and move[0] in constants.COLS and move[1] in constants.ROWS_STR:
      dstField = helpers.getBoardField(self.board, move[0], move[1])
      srcField = helpers.getBoardField(self.board, move[0], 2)

      if helpers.isFieldTakenByPawn(self.board, srcField['name']) and int(move[1]) - 2 < 3:
        self.makeMove(srcField['name'], dstField['name'], srcField['piece'])
        pass
      elif not helpers.isFieldTakenByPawn(self.board, srcField['name']):
        srcField = helpers.getBoardField(self.board, move[0], int(move[1])-1)

        if helpers.isFieldTakenByPawn(self.board, srcField['name']):
          self.makeMove(srcField['name'], dstField['name'], srcField['piece'])
        else:
          print('Illegal move!')

        pass

    move = [x for x in move]

    if len(move) > 2:
      if 'x' not in move:
        reqPiece = move[0]
        reqPieceCol = ''
        reqPieceRow = ''

        if move[1] in [x.upper() for x in constants.COLS]:
          reqPieceCol = move[1]

        if move[1] in [x for x in constants.ROWS]:
          reqPieceRow = move[1]

        foundPiece = None

        if len(reqPieceCol) == 1 and len(reqPieceRow) == 0:
          foundPiece = helpers.findPiece(self.board, { 'name': reqPiece, 'color': self.playerSide }, reqPieceCol)
          print(foundPiece)
