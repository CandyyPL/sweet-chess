from tabulate import tabulate

def drawChessBoard(fullBoard, mode):
  board = []

  row = []

  for i, f in enumerate(fullBoard):
    name = ''

    if mode == 'pieces':
      if len(f['piece']) > 0:
        name = f'{f["piece"]["color"][0]}{f["piece"]["name"]}'
      else:
        name = ''
    elif mode == 'fields':
      name = f['name']

    row.append(name)

    if (i + 1) % 8 == 0:
      board.append(row)
      row = []

  print(tabulate(board, tablefmt='grid'))

def getBoardField(board, col, row):
  foundField = {}

  for f in board:
    if f'{col}{row}' == f['name']:
      foundField = f

  return foundField

def isFieldTakenByPawn(board, check):
  field = getBoardField(board, check[0], check[1])

  if field['taken'] and field['piece']['name'] == 'p':
    return True

def findPiece(board, piece, col = None, row = None):
  found = []

  for f in board:
    if len(f['piece']) > 0:
      checkNameAndColor = f['piece']['name'] == piece['name'] and f['piece']['color'] == piece['color']
      checkCol = f['name'][0] == col
      checkRow = f['name'][0] == row

      if col == None and row == None:
        if checkNameAndColor:
          found.append(f)

      if col != None and row == None:
        if checkNameAndColor and checkCol:
          found.append(f)

      if col == None and row != None:
        if checkNameAndColor and checkRow:
          found.append(f)

      if col != None and row != None:
        if checkNameAndColor and checkCol and checkRow:
          found.append(f)

  return found
