import random

class CasinoGame:
    def __init__(self, profit_goal, start_money, min_bet, max_bet):
        self.profit_goal = profit_goal
        self.start_money = start_money
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.red_spaces = list(range(1, 19))
        self.black_spaces = list(range(19, 37))
        self.green_space = 37

    def play_game(self):
        current_money = self.start_money
        player_bet = self.min_bet

        print(f"Starting Money: {current_money}")

        while current_money >= self.min_bet and current_money < self.profit_goal:
            spin = random.randint(0, 36)
            player_lost = True

            while player_lost and player_bet <= self.max_bet and current_money >= player_bet:
                # Simulate the spin
                print(f"Placing bet of ${player_bet}...")
                if spin % 2 == 0:  # Player loses
                    print(f"Spin result: {spin} (Loss)")
                    current_money -= player_bet
                    print(f"Money left: ${current_money}")
                    player_bet *= 2  # Double the bet for the Martingale strategy
                    spin = random.randint(0, 36)  # Spin again
                else:  # Player wins
                    print(f"Spin result: {spin} (Win)")
                    current_money += player_bet
                    player_lost = False
                    print(f"Money left: ${current_money}")
                    player_bet = self.min_bet  # Reset the bet after a win

        # Determine the game outcome
        if current_money < self.min_bet:
            print("You ran out of money.")
        else:
            print("You reached your goal and beat the casino.")
            print(f"Final Money: ${current_money}")

    @staticmethod
    def get_user_input():
        """Prompt the user for game settings."""
        try:
            profit_goal = int(input("Profit Goal: "))
            start_money = int(input("Starting Money: "))
            min_bet = int(input("Table Minimum Bet: "))
            max_bet = int(input("Table Maximum Bet: "))
        except ValueError:
            print("Please enter valid numbers.")
            return None

        if min_bet > max_bet:
            print("Minimum bet should be less than or equal to maximum bet.")
            return None
        if start_money < min_bet:
            print("Starting money should be at least equal to the minimum bet.")
            return None

        return profit_goal, start_money, min_bet, max_bet