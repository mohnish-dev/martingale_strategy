from martingale_strategy import CasinoGame

def main():
    user_input = CasinoGame.get_user_input()
    if user_input:
        profit_goal, start_money, min_bet, max_bet = user_input
        game = CasinoGame(profit_goal, start_money, min_bet, max_bet)
        game.play_game()

if __name__ == "__main__":
    main()