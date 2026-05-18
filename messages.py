MESSAGES = {
    "welcome": "\nWelcome, {name}! Starting balance: {balance}$\n",

    "menu": (
        "Press Enter to play, "
        "type 'q' to quit, "
        "'p' to see your profile, "
        "or 'c' to change player: "
    ),

    "bet_prompt": "How much do you want to bet? (Balance: {balance}$) ",
    "invalid_bet": "Invalid input — please enter a whole number.",
    "negative_bet": "Please enter a positive amount.",
    "exceeds_balance": "You cannot bet more than your current balance.",

    "color_prompt": "Choose a color (blanc / noir / rouge): ",
    "invalid_color": "Invalid color. Please type one of the available colors (blanc / noir / rouge)",
    "not_a_color": "A color can't be a number. Please choose a valid color.",

    "number_prompt": "Choose a number (0-49): ",
    "invalid_number": "Invalid input — please enter a whole number.",
    "number_out_of_range": "Number must be between 0 and 49.",

    "result": "\n  → Result: {color} / {number}",

    "jackpot": (
        "🎉 Jackpot! "
        "You won {gain}$ "
        "(Balance: {balance}$)"
    ),

    "win": (
        "✅ Good guess! "
        "You won {gain}$ "
        "(Balance: {balance}$)"
    ),

    "lose": (
        "❌ Wrong. "
        "You lost {loss}$ "
        "(Balance: {balance}$)"
    ),

    "profile": (
        "\nProfile for {name}:\n"
        "  ID: {id}\n"
        "  Balance: {balance}$"
    ),

    "switch_prompt": (
        "Enter the name of the player "
        "you want to switch to: "
    ),

    "switch_existing": (
        "\nSwitched to existing player: "
        "{name} (Balance: {balance}$)"
    ),

    "switch_new": (
        "\nSwitched to player: "
        "{name} (Balance: {balance}$)"
    ),

    "quit": "\nThanks for playing! Final balance: {balance}$",

    "game_over": "\nGame over — you have no money left."
}