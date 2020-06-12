import importlib
import game
importlib.reload(game)
test = game.game()

print("Board: \n", test.board)
print("Super_baord \n", test.sup_board)

test.play()