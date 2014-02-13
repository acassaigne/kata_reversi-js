import unittest
from reversi import Reversi

class TestReversi(unittest.TestCase):

  INITIAL_SITUATION = """. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . B W . . .
. . . W B . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
B"""

  def setUp(self):
    self.reversi = Reversi(self.INITIAL_SITUATION)

  def test_count_rows(self):
    self.assertEqual(self.reversi.count_rows(), 8)

  def test_get_row_C4(self):
    self.assertEqual(self.reversi.get_row('C4'), '. . . B W . . .')

  def test_get_column_C4(self):
    self.assertEqual(self.reversi.get_column('C4'), "........")

#  def test_is_valid_C4_from_init(self):
#    reversi = Reversi(self.INITIAL_SITUATION)
#    self.assertTrue(reversi.is_valid_proposition('C4'), True)

  def test_get_neighbour_east_from_C5(self):
    self.assertEqual(self.reversi.get_neighbour('C5','EAST'), 'W')

  #def test_valid_C5_from_init(self):
  #  reversi = Reversi(self.INITIAL_SITUATION)
  #  self.assertTrue(reversi.is_valid_proposition('C5'), True)

  def test_current_player_should_be_B_from_init(self):
    self.assertEqual(self.reversi.get_current_player(), 'B')

  def test_move_position_EAST_from_C5_should_be_D5(self):
    self.assertEqual(self.reversi.move_proposition( 'C5', 'EAST'), 'D5')

  def test_move_position_WEST_from_C5_should_be_B5(self):
    self.assertEqual(self.reversi.move_proposition( 'C5', 'WEST'), 'B5')

  def test_move_position_SOUTH_from_C5_should_be_C6(self):
    self.assertEqual(self.reversi.move_proposition( 'C5', 'SOUTH'), 'C6')

  def test_move_position_NORTH_from_C5_should_be_C4(self):
    self.assertEqual(self.reversi.move_proposition( 'C5', 'NORTH'), 'C4')

  def test_from_direction_NORTH_EAST_get_elementary_directions_should_be_array_NORTH_and_EAST(self):
    self.assertEqual(self.reversi.get_elementary_directions('NORTH_EAST'),  ['NORTH', 'EAST'])

  def test_from_direction_WEST_get_elementary_directions_should_be_array_WEST(self):
    self.assertEqual(self.reversi.get_elementary_directions('WEST'),  ['WEST'])



  #def test_move_position_NORTH_EAST_from_C5_should_be_D4(self):
  #  self.assertEqual(self.reversi.move_proposition( 'C5', 'NORTH_EAST'), 'D4')
