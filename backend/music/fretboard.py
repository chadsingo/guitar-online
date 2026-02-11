# Take note tuples, and fill in each values for string based on provided tuning
from notes import notes, notes_accidentals_flats, notes_accidentals_sharps, chromatic_scale




def build_fretboard(tuning, frets, accidental):
    return

('A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab')
def build_string(open_note, frets, style):
    string = [open_note]
    pointer = chromatic_scale[open_note]
    accidental_indicies = [1,4,6,9,11]

    while len(string) <= frets:
        note = chromatic_scale[pointer]

        if style == 'Flats' and pointer in accidental_indicies:
            string.append(chromatic_scale[pointer].split('/')[1])

        elif style == 'Sharps' and pointer in accidental_indicies:
            string.append(chromatic_scale[pointer].split('/')[0])

        elif pointer in accidental_indicies:
            string.append(chromatic_scale[pointer])

        else:
            string.append(note)
        pointer += 1
        pointer %= 12

    return None
# Tuning in order string 6-5-4-3-2-1
# Shows Shaps by default
def build_fretboard_sharps(tuning):
    # Number of Frets
    frets = 22

    string_6 = [tuning[0]]
    pointer_6 = notes_accidentals_sharps.index(tuning[0]) + 1

    string_5 = [tuning[1]]
    pointer_5 = notes_accidentals_sharps.index(tuning[1]) + 1

    string_4 = [tuning[2]]
    pointer_4 = notes_accidentals_sharps.index(tuning[2]) + 1

    string_3 = [tuning[3]]
    pointer_3 = notes_accidentals_sharps.index(tuning[3]) + 1

    string_2 = [tuning[4]]
    pointer_2 = notes_accidentals_sharps.index(tuning[4]) + 1

    string_1 = [tuning[5]]
    pointer_1 = notes_accidentals_sharps.index(tuning[5]) + 1


    while len(string_6) < 23:
        # Tuple index reset to repeat notes
        if pointer_6 >= len(notes_accidentals_sharps):
            pointer_6 = 0
        if pointer_5 >= len(notes_accidentals_sharps):
            pointer_5 = 0
        if pointer_4 >= len(notes_accidentals_sharps):
            pointer_4 = 0
        if pointer_3 >= len(notes_accidentals_sharps):
            pointer_3 = 0
        if pointer_2 >= len(notes_accidentals_sharps):
            pointer_2 = 0
        if pointer_1 >= len(notes_accidentals_sharps):
            pointer_1 = 0

        string_6.append(notes_accidentals_sharps[pointer_6])
        string_5.append(notes_accidentals_sharps[pointer_5])
        string_4.append(notes_accidentals_sharps[pointer_4])
        string_3.append(notes_accidentals_sharps[pointer_3])
        string_2.append(notes_accidentals_sharps[pointer_2])
        string_1.append(notes_accidentals_sharps[pointer_1])
        
        

        pointer_1, pointer_2, pointer_3, pointer_4, pointer_5, pointer_6 += 1


    return [string_6, string_5, string_4, string_3, string_2, string_1]




# Tuning in order string 6-5-4-3-2-1
# Shows flats by default
def build_fretboard_flats(tuning):
    # Number of Frets
    frets = 22

    string_6 = [tuning[0]]
    pointer_6 = notes_accidentals_flats.index(tuning[0]) + 1

    string_5 = [tuning[1]]
    pointer_5 = notes_accidentals_flats.index(tuning[1]) + 1

    string_4 = [tuning[2]]
    pointer_4 = notes_accidentals_flats.index(tuning[2]) + 1

    string_3 = [tuning[3]]
    pointer_3 = notes_accidentals_flats.index(tuning[3]) + 1

    string_2 = [tuning[4]]
    pointer_2 = notes_accidentals_flats.index(tuning[4]) + 1

    string_1 = [tuning[5]]
    pointer_1 = notes_accidentals_flats.index(tuning[5]) + 1


    while len(string_6) < 23:
        # Tuple index reset to repeat notes
        if pointer_6 >= len(notes_accidentals_flats):
            pointer_6 = 0
        if pointer_5 >= len(notes_accidentals_flats):
            pointer_5 = 0
        if pointer_4 >= len(notes_accidentals_flats):
            pointer_4 = 0
        if pointer_3 >= len(notes_accidentals_flats):
            pointer_3 = 0
        if pointer_2 >= len(notes_accidentals_flats):
            pointer_2 = 0
        if pointer_1 >= len(notes_accidentals_flats):
            pointer_1 = 0

        string_6.append(notes_accidentals_flats[pointer_6])
        string_5.append(notes_accidentals_flats[pointer_5])
        string_4.append(notes_accidentals_flats[pointer_4])
        string_3.append(notes_accidentals_flats[pointer_3])
        string_2.append(notes_accidentals_flats[pointer_2])
        string_1.append(notes_accidentals_flats[pointer_1])
        
        

        pointer_1, pointer_2, pointer_3, pointer_4, pointer_5, pointer_6 += 1


    return [string_6, string_5, string_4, string_3, string_2, string_1]









# Coordinate pair to search fretboard
def get_note_at(fretboard, string, fret):
    return []




