# MovieBuffDb
    My final project for the CS50 Python course is a simple game based on movie knowledge.
    
# Description:
    The game uses an imported list of the Top250 rated movies on IMDb as its baseline. The game itself provides the user with some basic information to start, explaining the rules. Following the intro, the user gets prompted to choose a level. The lower the level, the fewer points the player is granted, and the shorter the list of randomly generated movies:

    - Level 1: Top50 movies, 1 point per correct answer
    - Level 2: Top150 movies, 2 points per correct answer
    - Level 3: Top250 movies, 3 points per correct answer

    The user is then presented with clues such as year, actors, awards, IMDb rating and the length of the title for a randomly generated movie. If the user is unable to figure out the answer, he can use a lifeline by inputting "plot", which reveals the movie's plot. The user gets 3 lives and 3 lifelines and plays until there are no lives remaining, after which the user is prompted for their name and added to a scoreboard that is printed on the screen. If the user is among the Top5 performers, their name can be seen on the scoreboard.

# Files:
    The files included in the game are:

    - requirements.txt the required libraries to play the game
    - scoreboard.csv: the file that gets created/updated each time a player completes a round and submits their name. This file is then reorganized with "pandas" and "tabulate" libraries and a neat scoreboard is printed in descending order at the end of the game
    - MovieBuffDb.py: The main game file
    - test_MovieBuffDb.py: A couple of unit tests for the game
    - This file
