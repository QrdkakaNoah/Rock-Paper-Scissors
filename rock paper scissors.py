###
#Noah Gaviña
#2.7.19
#Rock Paper Scissors game
###
print("Game made by Noah Gaviña.")
print("Hello I am NG451 and welcome to this rock, paper, scissors program.")
print("In case you forgot or somehow have never heard of rock paper scissors you pick between either rock paper or scissors.")
print("Rock beats scissors. Scissors beats paper. Paper beats rock.")
print("With that being said let's play!")
Play = input("Do you want to play?")
if Play.lower() == 'yes':
    print("Okay.")
    print("1 for rock, 2 for paper, 3 for scissors")
    p1 = input("Player 1 selection ")
    p2 = input("Player 2 selection ")
    if p1 == "1" and p2 == "3":
        print("Player 1 wins.")
    if p1 == "1" and p2 == "2":
        print("Player 2 wins.")
    if p1 == "2" and p2 == "1":
        print("Player 1 wins.")
    if p1 == "2" and p2 == "3":
        print("Player 2 wins.")
    if p1 == "3" and p2 == "1":
        print("Player 2 wins.")
    if p1 == "3" and p2 == "2":
        print("Player 1 wins.")
    if p1 == p2:
        print("Draw.")
elif Play.lower() == 'no':
    print("Oh...Okay...")
    print("Goodbye")
    input()
