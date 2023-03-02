from game import Game
from player import Player
from intelligence import Intelligence
from dice import Dice
from diceHand import DiceHand
from highScore import HighScore


def main():
    game = Game()
    print(game.header())
    print()
    print(game.get_startMenu())
    choice = int(input("-> "))
    if choice == 2:
        print()
        play = "y"
        while (play == "y"):
            gameTurn()
            play = input("Do you want to play again(y/n)").lower
        print("Goodbye")


def gameTurn():
    name = input("Enter the first player name: ")
    name2 = input("Enter the seconde player name: ")
    player = Player(name, 0)
    player2 = Player(name2, 0)
    game = Game()
    high_score = HighScore()
    while (player.get_score() < high_score.get_highScore() and computer.get_score() < high_score.get_highScore()):
        print(f"{player.get_name()} score: {player.get_score()}")
        print(f"{player2.get_name()} score: {player2.get_score()}")
        print()
        print("Player", game.get_turn(), "it is your turn")
        print()
        input("Hit enter to continue ")
        takeTurn(player, player2, game)
    if player.get_score >= 100:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= 100:
        game.end_game(player2.get_name(), player2.get_score())


def takeTurn(player_1, player_2, turn):
    die = Dice()
    diceHand = DiceHand(die)
    roll = "y"
    turnScore = 0
    while (roll == "y"):
        die_num = diceHand.roll()
        print("You rolled a ", die_num)
        print()
        if die_num == 1:
            print("You rolled a 1")
            print("Your turn is over")
            print()
            roll = "n"
            turnScore = 0
        else:
            turnScore = turnScore + die_num
            print("Your turn so far is ", turnScore)
            roll = input("Do you want to roll again(y/n)? ").lower()
    if turn.get_turn() == 1:
        turn.set_turn(2)
        if turnScore == 0:
            player_1.set_score(0)
        else:
            player_1.set_score(player_1.get_score() + turnScore)
    elif turn.get_turn() == 2:
        turn.set_turn(1)
        if turnScore == 0:
            player_2.set_score(0)
        else:
            player_2.set_score(player_2.get_score() + turnScore)


if __name__ == "__main__":
    main()
