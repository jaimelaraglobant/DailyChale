# Implement the strategy for two prisoners playing the Prisoner's Dilemma game.
# Instructions:
# Write a function called prisoners_dilemma(player1_strategy, player2_strategy) that takes two parameters: player1_strategy and player2_strategy. 
# These parameters represent the strategies chosen by the two prisoners playing the game.
# The function should return a tuple (player1_payoff, player2_payoff) representing the payoffs for each player based on their strategies.
# The function should implement the following RULES:
# If both players cooperate, both receive a moderate payoff of 3.
# If one player defects while the other cooperates, the defector receives a higher payoff of 5, and the cooperator receives a lower payoff of 0.
# If both players defect, both receive a lower payoff of 1.
import random

def prisoners_dilemma(player1_strategy, player2_strategy):
    # Define the payoffs
    PAYOFF_COOPERATE = 3
    PAYOFF_DEFECT = 5
    PAYOFF_BOTH_DEFECT = 1

    # Determine the payoffs based on strategies
    if player1_strategy == 'cooperate' and player2_strategy == 'cooperate':
        return (PAYOFF_COOPERATE, PAYOFF_COOPERATE)
    elif player1_strategy == 'cooperate' and player2_strategy == 'defect':
        return (0, PAYOFF_DEFECT)
    elif player1_strategy == 'defect' and player2_strategy == 'cooperate':
        return (PAYOFF_DEFECT, 0)
    elif player1_strategy == 'defect' and player2_strategy == 'defect':
        return (PAYOFF_BOTH_DEFECT, PAYOFF_BOTH_DEFECT)
    elif player1_strategy == 'tit_for_tat':
        # Tit-for-tat: Cooperate initially, then mirror opponent's previous move
        return (PAYOFF_COOPERATE, PAYOFF_DEFECT) if player2_strategy == 'defect' else (PAYOFF_COOPERATE, PAYOFF_COOPERATE)
    elif player1_strategy == 'friedman':
        # Always cooperate
        return (PAYOFF_COOPERATE, PAYOFF_COOPERATE)
    elif player1_strategy == 'joss':
        # Mostly cooperate, occasionally defect randomly
        return (random.choice([PAYOFF_COOPERATE, PAYOFF_DEFECT]), random.choice([PAYOFF_COOPERATE, PAYOFF_DEFECT]))
    elif player1_strategy == 'davis':
        # Cooperate initially, then defect if opponent defects twice in a row
        return (PAYOFF_COOPERATE, PAYOFF_DEFECT) if player2_strategy == 'defect' else (PAYOFF_COOPERATE, PAYOFF_COOPERATE)
    elif player1_strategy == 'downing':
        # Cooperate initially, then defect if opponent defects more times than they cooperate
        return (PAYOFF_COOPERATE, PAYOFF_DEFECT) if player2_strategy == 'defect' else (PAYOFF_COOPERATE, PAYOFF_COOPERATE)
    else:
        raise ValueError("Invalid strategy. Available strategies: 'cooperate', 'defect', 'tit_for_tat', 'friedman', 'joss', 'davis', 'downing'")

def randomplayergame():
    return random.choice(['cooperate', 'defect', 'tit_for_tat', 'friedman', 'joss', 'davis', 'downing'])

#usage:
player1_strategy = randomplayergame() #'tit_for_tat'
print("Player 1 Strategy: ", player1_strategy)
player2_strategy = randomplayergame() #'defect'
print("Player 2 Strategy: ", player2_strategy)
payoffs = prisoners_dilemma(player1_strategy, player2_strategy)
print(f"Player 1 payoff: {payoffs[0]}, Player 2 payoff: {payoffs[1]}")

# Example usage:
# In the first example, player 1 chooses to cooperate, while player 2 chooses to defect. Player 1 receives a payoff of 0, and player 2 receives a payoff of 5.
result = prisoners_dilemma('cooperate', 'defect')
print('cooperate', 'defect', 'the result must be 0,5')
print(result)
# In the second example, player 1 uses the "Tit for Tat" strategy, initially cooperating. Since player 2 also cooperates, both players receive a payoff of 3.
result = prisoners_dilemma('tit_for_tat', 'cooperate')
print('tit_for_tat', 'cooperate', ' the result must be 3,3')
print(result)
# In the third example, player 1 uses the "Friedman" strategy, always cooperating. Player 1 receives a payoff of 0, and player 2 receives a payoff of 5.
result = prisoners_dilemma('friedman', None)
print('friedman', None, ' the result must be 0,5')
print(result)
# In the fourth example, player 1 uses the "Joss" strategy, which mostly cooperates but occasionally defects randomly. The outcomes can vary randomly between (3, 3) and (5, 0), 
#     representing the mixed results of cooperating and defecting.
result = prisoners_dilemma('joss', None)
print('joss', None, ' the result must be 3,3 / 5,0')
print(result)
# In the fifth example, player 1 uses the "Davis" strategy, cooperating initially and then defecting if the opponent defects twice in a row. 
#     If the opponent does not defect twice in a row, both players receive a payoff of 3. If the opponent defects twice in a row, player 1 defects and receives a payoff of 0, 
#     while player 2 receives a payoff of 5.
result = prisoners_dilemma('davis', 'defect')
print('davis', 'defect', ' the result must be 3,5')
print(result)
# In the sixth example, player 1 uses the "Downing" strategy, cooperating initially and then defecting if the opponent defects more times than they cooperate. 
#     If the opponent cooperates more times than they defect, both players receive a payoff of 3. If the opponent defects more times than they cooperate, 
#     player 1 defects and receives a payoff of 0, while player 2 receives a payoff of 5.
result = prisoners_dilemma('downing', 'defect')
print('downing', 'defect', ' the result must be 3,5')
print(result)