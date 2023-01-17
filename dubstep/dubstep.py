# Input

# The input consists of a single non-empty string, consisting only of uppercase
#  English letters, the string's length doesn't exceed 200 characters

# Output

# Return the words of the initial song that Polycarpus used to make a dubsteb
#  remix. Separate the words with a space.

# Examples

# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
# # =>  'WE ARE THE CHAMPIONS MY FRIEND'



# My solution
def song_decoder(song):
    newSong = song.replace('WUB', ' ')
    cleanSong = newSong.strip()
    finalSong = ' '.join(cleanSong.split())
    return finalSong


# Function driver
# print(':::'+song_decoder('WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB')+':::')
# print('')
# print(':::WE ARE THE CHAMPIONS MY FRIEND:::')

