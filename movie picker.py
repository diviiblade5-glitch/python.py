class MoviePicker:

    def funny_movies(self):
        return "Mr. Bean"
    
    def action_movies(self):
        return "Avengers"
    
    def anime_movies(self):
        return "Blue Lock"

    def  horror_movies(self):
         return "the Nun"
    
print("\n")

picker = MoviePicker() 
print("My movie recommendations:")

print("\n")

print(picker.funny_movies())
print(picker.action_movies())
print(picker.anime_movies())
print(picker.horror_movies())
print("\n")
user_choice=input("which movie do you wnat to try first?:").strip().lower()

if user_choice == "horror":
    print(picker.horror_movies())
elif user_choice == "action":
    print(picker.action_movies())
elif user_choice == "funny":
    print(picker.funny_movies())
elif user_choice == "anime":
    print(picker.anime_movies())
else:
    print("Genre not found!")

