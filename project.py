import json
import requests
import random
import re
from os import system
import emoji
import csv
from tabulate import tabulate
import pandas as pd

movie_list = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Godfather Part II', '12 Angry Men', "Schindler's List", 'The Lord of the Rings: The Return of the King', 'Pulp Fiction', 'The Lord of the Rings: The Fellowship of the Ring', 'The Good, the Bad and the Ugly', 'Forrest Gump', 'Fight Club', 'Inception', 'The Lord of the Rings: The Two Towers', 'Star Wars: Episode V - The Empire Strikes Back', 'The Matrix', 'Goodfellas', "One Flew Over the Cuckoo's Nest", 'Se7en', 'Seven Samurai', "It's a Wonderful Life", 'The Silence of the Lambs', 'City of God', 'Saving Private Ryan', 'Life Is Beautiful', 'The Green Mile', 'Interstellar', 'Star Wars', 'Terminator 2: Judgment Day', 'Back to the Future', 'Spirited Away', 'Psycho', 'The Pianist', 'Léon: The Professional', 'Parasite', 'The Lion King', 'Gladiator', 'American History X', 'The Departed', 'The Usual Suspects', 'The Prestige', 'Casablanca', 'Whiplash', 'The Intouchables', 'Harakiri', 'Grave of the Fireflies', 'Modern Times', 'Once Upon a Time in the West', 'Rear Window', 'Alien', 'City Lights', 'Cinema Paradiso', 'Apocalypse Now', 'Memento', 'Indiana Jones and the Raiders of the Lost Ark', 'Django Unchained', 'WALL·E', 'The Lives of Others', 'Sunset Blvd.', 'Paths of Glory', 'The Shining', 'The Great Dictator', 'Top Gun: Maverick', 'Witness for the Prosecution', 'Avengers: Infinity War', 'Aliens', 'American Beauty', 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'Spider-Man: Into the Spider-Verse', 'The Dark Knight Rises', 'Oldboy', 'Joker', 'Amadeus', 'Braveheart', 'Toy Story', 'Coco', 'Inglourious Basterds', 'The Boat', 'Princess Mononoke', 'Avengers: Endgame', 'Once Upon a Time in America', 'Good Will Hunting', 'Your Name.', 'Requiem for a Dream', 'Toy Story 3', "Singin' in the Rain", '3 Idiots', 'Star Wars: Episode VI - Return of the Jedi', 'High and Low', '2001: A Space Odyssey', 'Eternal Sunshine of the Spotless Mind', 'Reservoir Dogs', 'Capernaum', 'Lawrence of Arabia', 'The Hunt', 'Citizen Kane', 'M', 'North by Northwest', 'Come and See', 'Vertigo', 'Amélie', 'A Clockwork Orange', 'Double Indemnity', 'Full Metal Jacket', 'The Apartment', 'Scarface', 'Ikiru', 'The Sting', 'To Kill a Mockingbird', 'Taxi Driver', 'Heat', 'Up', 'L.A. Confidential', 'Incendies', 'Metropolis', 'A Separation', 'Die Hard', 'Snatch', 'Hamilton', 'Indiana Jones and the Last Crusade', 'Bicycle Thieves', '1917', 'Like Stars on Earth', 'Downfall', 'For a Few Dollars More', 'Batman Begins', 'Dangal', 'The Kid', 'Some Like It Hot', 'All About Eve', 'The Father', 'Green Book', 'The Wolf of Wall Street', 'Spider-Man: No Way Home', 'Judgment at Nuremberg', 'Ran', 'Casino', 'Unforgiven', "Pan's Labyrinth", 'There Will Be Blood', 'The Truman Show', 'The Sixth Sense', 'A Beautiful Mind', 'Monty Python and the Holy Grail', 'Yojimbo', 'The Treasure of the Sierra Madre', 'Shutter Island', 'Jurassic Park', 'The Great Escape', 'Rashomon', 'Kill Bill: Vol. 1', 'No Country for Old Men', 'Finding Nemo', 'The Elephant Man', 'Chinatown', 'Raging Bull', 'The Thing', 'Gone with the Wind', 'V for Vendetta', 'Inside Out', 'Lock, Stock and Two Smoking Barrels', 'Dial M for Murder', 'The Secret in Their Eyes', "Howl's Moving Castle", 'The Bridge on the River Kwai', 'Three Billboards Outside Ebbing, Missouri', 'Trainspotting', 'Warrior', 'Gran Torino', 'Fargo', 'Prisoners', 'My Neighbor Totoro', 'Million Dollar Baby', 'Catch Me If You Can', 'The Gold Rush', 'Blade Runner', 'On the Waterfront', 'Children of Heaven', 'The Third Man', 'Before Sunrise', 'Ben-Hur', '12 Years a Slave', 'Wild Strawberries', 'Harry Potter and the Deathly Hallows: Part 2', 'Gone Girl', 'The General', 'The Deer Hunter', 'In the Name of the Father', 'The Grand Budapest Hotel', 'Everything Everywhere All at Once', 'Barry Lyndon', 'Mr. Smith Goes to Washington', 'The Wages of Fear', 'Sherlock Jr.', 'Hacksaw Ridge', 'Memories of Murder', 'Klaus', 'Wild Tales', 'The Seventh Seal', 'Room', 'Mad Max: Fury Road', 'How to Train Your Dragon', 'The Big Lebowski', 'Mary and Max', 'Monsters, Inc.', 'Jaws', 'Tokyo Story', 'Dead Poets Society', 'The Passion of Joan of Arc', 'Hotel Rwanda', 'Rocky', 'Ford v Ferrari', 'Platoon', 'Pather Panchali', 'Stand by Me', 'The Terminator', 'Spotlight', 'Rush', 'Logan', 'Network', 'Ratatouille', 'Into the Wild', 'The Wizard of Oz', 'Groundhog Day', 'Before Sunset', 'The Exorcist', 'The Best Years of Our Lives', 'The Incredibles', 'To Be or Not to Be', 'The Grapes of Wrath', 'The Battle of Algiers', 'Rebecca', "Hachi: A Dog's Tale", 'Cool Hand Luke', 'Amores perros', 'Pirates of the Caribbean: The Curse of the Black Pearl', 'La Haine', 'My Father and My Son', 'The 400 Blows', 'Jai Bhim', 'It Happened One Night', 'Persona', 'The Sound of Music', 'Life of Brian', 'The Handmaiden', 'Dersu Uzala', 'Aladdin', 'Gandhi', 'The Help', 'The Iron Giant']

def main():
    introduction()
    z = input("Type anything and press enter when you're ready!")
    system("clear")
    new_list, level = level_generator() #new_list is a list of top50,150 or 250 movies. Altered movie_list. level is number chosen.
    system("clear")
    score = 0
    lives = 3
    lifeline = 3
    while lives > 0:
        movie = movie_generator(random.choice(new_list))
        movie_title = (movie["Title"]).upper()
        length = create_underscores(movie_title)
        year, awards, rating, genre, actors, plot, director = clues_generator(movie_title)
        clues_to_text(year, awards, rating, genre, actors, plot, director)
        print("")
        print(f"The length of the title is: {length}")
        print("")
        if lives > 0:
            guess = input('What is the movie? (PS: type "plot" to use a lifeline if you still have one): ').upper()
            if guess == movie_title:
                score += 1 * level
                correct_answer(lives, lifeline, score)
                continue
            if guess == "PLOT" and lifeline > 0: #need to figure out how to reprompt without restarting the loop if user says Plot but no lifeline
                lifeline -= 1
                print(f"The plot is: {plot}")
                print("")
                new_guess = input("What is the movie? ").upper()
                if new_guess == movie_title:
                    score += 1 * level
                    correct_answer(lives, lifeline, score)
                    continue
                else:
                    lives -= 1
                    if lives != 0:
                        wrong_answer(movie_title, lives, lifeline, score)
                        continue
                    else:
                        system("clear")
                        break
            if not guess == movie_title and not guess == "PLOT":
                lives -= 1
                if lives != 0:
                    wrong_answer(movie_title, lives, lifeline, score)
                    continue
                else:
                    system("clear")
                    break
    new_line = "\n"
    print(f"Game over! Last movie title was: {movie_title}. Your final score was: {score}{new_line}")
    user_name = input("What's your name: ")
    system("clear")
    add_to_scoreboard(user_name, score)
    print_sorted_scoreboard()




def correct_answer(lives, lifeline, score):
    system("clear")
    print(f"**********************")
    print("Lives remaining: ", "💖" * lives)
    print("Lifelines remaining: ", "ℹ️}" * lifeline)
    print(f"Current score {score}")
    print(f"**********************")

def wrong_answer(movie_title, lives, lifeline, score):
    system("clear")
    print(f"**********************")
    print(f"Wrong answer! The movie title was: {movie_title}.")
    print("Lives remaining: ", "💖" * lives)
    print("Lifelines remaining: ", "ℹ️}" * lifeline)
    print(f"Current score {score}")
    print(f"**********************")

def add_to_scoreboard(name, score):
    with open("scoreboard.csv", "a", newline='') as scoreboard:
        writer = csv.writer(scoreboard)
        addition = [name, score]
        writer.writerow(addition)

def print_sorted_scoreboard():
    with open("scoreboard.csv", "r") as scoreboard:
        reader = pd.read_csv("scoreboard.csv", delimiter=",")
        sorted = reader.sort_values(by="Score", ascending=False)
        removed_index = sorted.reset_index(drop=True)
        removed_index.index +=1
        result = removed_index.head(5)
        print(tabulate(result, headers=["Name", "Score"], tablefmt="fancy_grid"))

def clues_to_text(year, awards, rating, genre, actors, plot, director):
    new = "\n"
    print(f"The movie was made during year of {year} and it won {awards} awards.{new}The movie's IMDb rating is: {rating} and its genre is: {genre}.")
    print(f"Actors who played key roles were: {actors}.")

def clues_generator(movie):
    movie = movie_generator(movie)
    year = movie["Year"]
    awards = movie["Awards"]
    rating = movie["Ratings"][0]["Value"]
    genre = movie["Genre"]
    actors = movie["Actors"]
    plot = movie["Plot"]
    director = movie["Director"]
    return year, awards, rating, genre, actors, plot, director

def create_underscores(title):
    return re.sub(r'[a-zA-Z]', r'_', title)

def movie_generator(movie_name): #takes in movie name, returns json string with all info for that movie
    movie = movie_name.replace(" ", "+")
    reformat = "https://www.omdbapi.com/?t=" + movie + "&apikey=c56e482a"
    response = requests.get(reformat)
    movie_info = response.json()
    return movie_info

def level_generator(): #returns a redacted list only including top 50,150 or 250 movies
    level = 0
    while level not in [1,2,3]:
        level = int(input("Choose level (1, 2 or 3): "))
    if level == 1: return movie_list[0:50], 1
    if level == 2: return movie_list[0:150], 2
    if level == 3: return movie_list[0:250], 3

def introduction():
    print("****************\nHello! Welcome to my Movie Buff game. Rules:\n- There are 3 levels based on IMDB's Top250 movies:\n * Level 3 includes all 250 movies and grants 3 points per correct answer.\n * Level 2 includes Top150 movies and grants 2 points per correct answer.\n * Level 1 includes Top50 movies and grants 1 point per correct answer.\n- Each round, you will get a randomly generated movie along with some clues about that movie.\n- If you guess correctly, you will be awarded points.\n- If you guess incorrectly, you will lose a life (3 total lives).\n- You have 3 lifelines which reveal the movie plot. Use these lifelines if you're not completely sure of the answer!\n- Answers will be handled case insensitively, but make sure your spelling is correct!\n\nGood luck!\n****************")


if __name__ in "__main__":
    main()