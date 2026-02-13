# Take note tuples, and fill in each values for string based on provided tuning
from notes import notes, notes_accidentals_flats, notes_accidentals_sharps, chromatic_scale



# Works if tuning is passed in this order 6-5-4-3-2-1
# Returned fretboard is in order 6-5-4-3-2-1
def build_fretboard(tuning, frets, accidental):
    fretboard = []
    for open_note in tuning:
        fretboard.append(build_string(open_note, frets, accidental))

    return fretboard

# ('A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab')
def build_string(open_note, frets, accidental):
    string = [open_note]
    pointer = chromatic_scale[open_note]
    accidental_indicies = [1,4,6,9,11]

    while len(string) <= frets:
        note = chromatic_scale[pointer]

        if accidental == 'Flats' and pointer in accidental_indicies:
            string.append(chromatic_scale[pointer].split('/')[1])

        elif accidental == 'Sharps' and pointer in accidental_indicies:
            string.append(chromatic_scale[pointer].split('/')[0])

        elif pointer in accidental_indicies: #This can likely go, but the organization is helpful for clarity
            string.append(chromatic_scale[pointer])
        else:
            string.append(note)

        pointer += 1
        pointer %= 12

    return string


# Coordinate pair to search fretboard
def get_note_at(fretboard, string, fret):
    return []








'''
Test Suite
('A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab')
'''
def build_string_test1():
    frets = 22
    open_note = 'E'
    accidental = 'Sharp'

    actual = build_string()
    expected = ['E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C', 'C#', 'D']

    return actual == expected


def build_string_test2():
    frets = 22
    open_note = 'D'
    accidental = 'Sharp'

    actual = build_string()
    expected = ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C', 'C#', 'D', 'D#','E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C']

    return actual == expected

def build_string_test3():
    frets = 22
    open_note = 'E'
    accidental = 'Flat'

    actual = build_string()
    expected = ['E', 'F', 'Gb', 'G', 'Ab','A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab','A', 'Bb', 'B', 'C', 'Db', 'D']

    return actual == expected



def main():
    print(build_string_test1)
    print(build_string_test2)
    print(build_string_test3)


if __name__ == "__main__":
    main()