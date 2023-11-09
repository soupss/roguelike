from game import Game


game = Game()
while game.is_running():
    game.handle_events()
    game.update()
    game.draw()
del game
