"""99_bottles.py: prints the lyrics to "99 Bottles of Beer on the Wall".

This project is from https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/."""

for n in (range(99, 0, -1)):
    words = (n, "bottle" if n == 1 else "bottles", n - 1, "bottle" if n - 1 == 1 else "bottles")
    print("{0} {1} of beer on the wall\n{0} {1} of beer\nTake one down\nPass it around\n{2} {3} of beer on the wall!\n".format(*words))
