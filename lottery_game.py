
import random

class Player:
    def __init__(self, name, money, player_id=None):
        self.name = name
        self.money = money
        self.bet = 0
        self.lottery_number = None
        self.color = None
        self.player_id = player_id


class GameEngine:
    def __init__(self):
        self.player = Player("Player1", 100, player_id=1)  # Default player; will be updated by UI
        self.colors = ["blanc", "noir", "rouge"]
        self.numbers = (0, 49)

    def get_bet(self, bet) -> str:
        """Get and validate the player's bet amount."""
        try :
            if bet <= 0:
                return 'negative'
            elif bet > self.player.money:
                return 'exceeds_balance'
            else:
                self.player.bet = bet
        except ValueError:
            return 'invalid_input'

    def get_choices(self, color, number) -> str:
        """Collects the player's color and number choices."""
        if color in self.colors:
            self.player.color = color
        else:
            return 'Invalid_color'

        try:
            if self.numbers[0] <= number <= self.numbers[1]:
                self.player.lottery_number = number
            else:
                return 'Number_out_of_range'
        except ValueError:
            return 'Invalid_number'

    def spin(self) -> tuple:
        """Generates the round's winning color and number."""
        return random.choice(self.colors), random.randint(self.numbers[0], self.numbers[1])

    def resolve(self, win_color, win_number) -> tuple:
        """Applies the outcome and updates the player's balance."""

        if self.player.color == win_color and self.player.lottery_number == win_number:
            gain = self.player.bet * 4
            self.player.money += gain
            return 'jackpot', gain 

        elif self.player.color == win_color:
            gain = self.player.bet 
            self.player.money += gain
            return 'win', gain

        else:
            if self.player.bet == 1:
                loss = 1  # minimum loss is 1$
            else:
                loss = self.player.bet // 2   # player recovers 50% of stake
            self.player.money -= loss
            return 'lose', loss



class PlayerManager:
    def __init__(self) : 
        self.player_base = {}

    def add_player(self, id, name) -> Player:
        """Adds a new player to the player base or switches to existing one."""
        if id in self.player_base:
            return self.switch_player(id)
        else:
            new_player = Player(name, 100, player_id=len(self.player_base) + 1)
            self.player_base[id] = new_player
            return new_player
        
    def switch_player(self, id) -> Player :
        """Switches to an existing player or creates a new one if the name doesn't exist."""
        if id in self.player_base:
            return self.player_base[id]
        else:
            return self.add_player(id)

    def save_player(self, player) -> Player:
        """Saves the current player to the player base."""
        if player.name in self.player_base:
            return
        self.player_base[player.player_id] = player
        return player
    
    def show_profile(self, player) -> tuple:
        """Returns the player's profile information."""
        return player.name, player.player_id, player.money
    