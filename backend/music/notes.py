# Tuples generally represent data that shouldnt change

notes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')

# Indexes represent identical notes, even though for example A# and Bb are written differently
# This logic may need to change for scales to make sure each letter is used once
notes_accidentals_sharps = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
notes_accidentals_flats = ('A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab')

# Combines the sharps and flats into one scale
chromatic_scale = ('A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab')



# Takes a note name that has been checked to be well formatted and returns the index, for accidentals it
# returns both

def get_chromatic_scale():
    return chromatic_scale

def note_to_index(note):
    index = -1

    for i in range(len(chromatic_scale)):
        if chromatic_scale[i] == note:
            index = i

    return index


# Takes an index and finds the note a that idex
def index_to_note(index):
    return chromatic_scale[index]



