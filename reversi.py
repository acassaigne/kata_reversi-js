class Reversi():

  def __init__(self, situation):
    array = situation.split("\n")
    self.board = array[0:len(array) - 1]
    self.current_player = array[-1]

  def count_rows(self):
    return len(self.board)

#  def is_valid_proposition(self, proposition):
#    if self.has_same_color_pion(proposition, 'W', 'EAST') and self.last_pion_has_color(proposition, 'B', 'EAST'):
#      # TODO
#      return True
#    return False

  def get_row(self, proposition):
    return self.board[int(proposition[1]) - 1]

  def get_column(self,proposition):
    column_number = self.convert_column_letter_to_number(proposition)
    column = self.extract_column(column_number)
    return column

  def convert_column_letter_to_number(self, proposition):
    return "ABCDEFGH".find(proposition[0])

  def extract_column(self, column_number):
    column = ""
    for row in range(0,8):
      column += self.board[row][column_number]
    return column

  def get_neighbour(self, proposition, direction):
    row = self.get_row(proposition)
    if direction == 'EAST':
      column_number = self.convert_column_letter_to_number(proposition)
      return row[ (column_number+1) * 2 ]

  def get_current_player(self):
    return self.current_player

  def get_opposite_player(self):
    if (self.current_player == 'B'):
      return 'W'
    return 'B'

  def move_proposition(self, proposition, direction):
    all_directions = self.get_elementary_directions(direction)
    for one_direction in all_directions:
      if one_direction in ('SOUTH', 'NORTH'):
        proposition = self.move_latitude(proposition, one_direction)
      if one_direction in ('EAST', 'WEST'):
        proposition = self.move_longitude(proposition, one_direction)
    return proposition

  def move_latitude(self, proposition, elementary_direction):
    decalage_direction = {'NORTH' : -1, 'SOUTH' : 1}
    local_decalage = decalage_direction[elementary_direction]
    row_number = int(proposition[1]) + local_decalage
    return proposition[0] + str(row_number)

  def move_longitude(self, proposition, elementary_direction):
    decalage_direction = {'EAST': 1 , 'WEST' : -1}
    local_decalage = decalage_direction[elementary_direction]
    column_letter = chr(self.convert_column_letter_to_number(proposition) + local_decalage + ord('A'))
    return column_letter + proposition[1]

  def get_elementary_directions(self, full_direction):
    return full_direction.split('_')

  #def is_valid_proposition(self, proposition):
  #  current_direction = 'EAST'
  #  current_proposition = proposition
  #  while(self.get_neighbour(current_proposition, current_direction)) == self.get_opposite_player()):
  #    current_proposition = move_proposition(current_proposition, current_direction)

