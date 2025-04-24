punctuation = ["!", "?", "…", ",", ".", "'", "-"]
pu_symbols = punctuation + ["SP", "UNK"]
pad = "_"

# English
en_symbols = [
    "aa", "ae", "ah", "ao", "aw", "ay", "b", "ch", "d", "dh",
    "eh", "er", "ey", "f", "g", "hh", "ih", "iy", "jh", "k",
    "l", "m", "n", "ng", "ow", "oy", "p", "r", "s", "sh",
    "t", "th", "uh", "uw", "V", "w", "y", "z", "zh",
]
num_en_tones = 4

# combine all symbols
normal_symbols = sorted(set(en_symbols))
symbols = [pad] + normal_symbols + pu_symbols
sil_phonemes_ids = [symbols.index(i) for i in pu_symbols]

# combine all tones
num_tones = num_en_tones

# language maps
language_id_map = {"EN": 2}
num_languages = len(language_id_map.keys())

language_tone_start_map = {
    "EN": 0,
}
