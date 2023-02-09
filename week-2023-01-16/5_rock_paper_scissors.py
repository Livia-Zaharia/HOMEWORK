

# 5. Rock, paper, scissors2
# : Rock, paper, scissors is a popular hand game for two players. The
# two players simultaneously choose one of the three possible moves and determine the
# winner of the game: rock beats scissors, paper beats rock, and scissors beats paper.
# This exercise involves determining a game’s outcome given the moves of the two players.
# Write a program that takes in the inputs for both players and then displays the winner
# out of the two or tie if that is the case. Handle the situations when the input
# is neither rock, paper or scissors and display a message that the game cannot 
# go on until a right option is chosen.

game_dict={

    "rock":0,
    "paper":1,
    "scissors":2
}
while True:
    choice_1=input("Player one, please make your choice ")
    choice_2=input("Player two, please make your choice ")
    
    if (choice_1!="rock" and choice_1!="paper" and choice_1!="scissors") or (choice_2!="rock" and choice_2!="paper" and choice_2!="scissors"):
        print("The game needs valid input. Please retry")
        pass
    elif choice_1==choice_2:
        print("It was a tie")
        break
    elif (game_dict[choice_1] == 0 or game_dict[choice_1] == 2) and (game_dict[choice_2] == 0 or game_dict[choice_2] == 2):
        if(game_dict[choice_1]>game_dict[choice_2]):
            winner=game_dict[choice_2]
            winner_choice=choice_2
            player=2
        else:
            winner_choice=choice_1
            winner=game_dict[choice_1]
            player=1
        print("The winner was player "+ str(player)+ "with "+winner_choice)
        break
    else:
        if(game_dict[choice_1]>game_dict[choice_2]):
            winner_choice=choice_1
            winner=game_dict[choice_1]
            player=1
        else:
            winner_choice=choice_2
            winner=game_dict[choice_2]
            player=2
        print("The winner was player "+ str(player)+ "with "+winner_choice)
        break