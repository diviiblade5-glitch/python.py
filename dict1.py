class MoviePicker:

    def funny_movie(self):
        return "Rush Hour"

    def show_funny_movie(self):
        return self.funny_movie()

    def best_movie(self):
        return "Avengers"

    def show_best_movie(self):
        return self.best_movie()


picker = MoviePicker()

print("My movie recommendations:")
print(picker.funny_movie())
print(picker.show_funny_movie())
print(picker.best_movie())
print(picker.show_best_movie())