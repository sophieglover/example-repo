# define the class Album

class Album():
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return (f"{self.album_name}, {self.album_artist}, {self.number_of_songs}")

    def __repr__(self):
        return self.__str__()


# add albums into an empty list

albums1 = []

albums1.append(Album("you seem pretty sad for a girl so in love", 13, "Olivia Rodrigo"))

albums1.append(Album("play with earth! 0.03", 7, "wave to earth"))

albums1.append(Album("Super Trouper", 12, "ABBA"))

albums1.append(Album("Pylon", 14, "beabadoobee"))

albums1.append(Album("Songs For The Spine", 10, "The Royston Club"))


# print the list as it is and in order of how many albums are in them

print("This is the unsorted list albums1:")
print(*albums1, sep='\n')

print() 

sorted_albums1 = sorted(albums1, key=lambda album: album.number_of_songs)

print("This is the list albums1 sorted by number of songs:")
print(*sorted_albums1, sep='\n')


# add albums to another empty list

albums2 = []

albums2.append(Album("How to Save a Life", 12, "The Fray"))

albums2.append(Album("Abbey Road", 17, "The Beatles"))

albums2.append(Album("Fearless", 19, "Taylor Swift"))

albums2.append(Album("OK Computer", 12, "Radiohead"))

albums2.append(Album("Beautiful Chaos", 5, "KATSEYE"))

print("This is the unsorted list albums2:")
print(*albums2, sep='\n')


# copy all of the albums from albums1 into albums2

albums2 += albums1

print()
print(*albums2, sep='\n')


# add two more albums to albums2

albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))

albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))


# sort the new albums2 by alphabetical album name

sorted_albums2 = sorted(albums2, key=lambda album: album.album_name)

print()
print("This is the appended list albums2 according to album name:")
print(*sorted_albums2, sep='\n')


# print the index of Dark Side of the Moon in albums2

def binary_search(target, items):
    low, high = 0, len(items) - 1
 
    while high >= low:
        mid = (low + high) // 2

        if items[mid].album_name == target:
            return mid

        elif items[mid].album_name < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

target = "Dark Side of the Moon"
result = binary_search(target, sorted_albums2)

print()
print(f"The index of Dark Side of the Moon is {result}")





      

      

