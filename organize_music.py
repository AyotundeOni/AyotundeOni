#!/usr/bin/env python3
import os
import shutil

# --- User Configuration ---
# 1.  **Source Directory:**
#     Set the `SOURCE_DIRECTORY` variable to the path of the folder containing your music files.
#     Example for macOS: "/Users/yourusername/Downloads/Music"
#     Example for Windows: "C:\\Users\\yourusername\\Downloads\\Music"
SOURCE_DIRECTORY = "music_files"  # <<< CHANGE THIS

# 2. **Song List:**
#    The `song_list_text` variable contains the categorized list of songs.
#    You can modify this list to match your needs.
song_list_text = """
Ceremony / Cocktail Hour / Dinner (Feel-Good, Singalong, Light Energy)

Barry White – You’re The First, The Last, My Everything
Billy Joel – Piano Man
Bruno Mars – 24k Magic
Clean Bandit – Rather Be
Earth, Wind & Fire – Let’s Groove / September
Elvis Presley – Can’t Help Falling In Love
Gloria Estefan – Conga
Jackson 5 – ABC / I Want You Back
Katrina & The Waves – Walking On Sunshine
Mark Ronson & Amy Winehouse – Valerie
Marvin Gaye & Tammi Terrell – Ain’t No Mountain High Enough
Neil Diamond – Sweet Caroline
Prince – I Wanna Be Your Lover
Stevie Wonder – Signed, Sealed, Delivered / Isn’t She Lovely
Whitney Houston – How Will I Know
Whitney Houston – I Wanna Dance With Somebody (could also go in party)
The Outfield – Your Love
Walk The Moon – Shut Up and Dance
Journey – Don’t Stop Believin’
Queen – Don’t Stop Me Now
Taylor Swift – Love Story
Taylor Swift – You Belong With Me
Billy Joel – Piano Man
The Vamps, Matoma – All Night

💃 Early Dancefloor / Fun Throwbacks (Everyone Can Dance)

Abba – Dancing Queen / Gimme Gimme Gimme
Bee Gees – Stayin’ Alive
Belinda Carlisle – Heaven Is A Place On Earth
Madonna / Cher – Believe
Shania Twain – Man! I Feel Like a Woman
Spice Girls – Wannabe
Pink – Raise Your Glass
Britney Spears – Baby One More Time
Justin Timberlake – Can’t Stop The Feeling
Mark Ronson ft Bruno Mars – Uptown Funk
Calvin Harris ft Rihanna – We Found Love
Dua Lipa – Don’t Start Now / Levitating
Lizzo x Kool & The Gang – About Damn Time x Celebration
Pitbull ft Ne-Yo – Time Of Our Lives / Give Me Everything / Fireball / Don’t Stop The Party
Rihanna – Don’t Stop The Music / We Found Love / Pon De Replay
Black Eyed Peas – I Gotta Feeling / Let’s Get It Started / Boom Boom Pow
Daft Punk – One More Time
Avicii – Wake Me Up / Levels
Calvin Harris – Feel So Close
David Guetta & Bebe Rexha – I’m Good (Blue)
Zedd, Maren Morris, Grey – The Middle

🔥 Main Dancefloor Bangers (Peak Party / Club Vibes)

50 Cent – In Da Club
Akon – Smack That / I Wanna Love You
Beyonce, Jay-Z, Fatman Scoop – Crazy In Love
Black Eyed Peas – Pump It / Imma Be
Chris Brown – Yeah 3x
DJ Snake ft Cardi B, Selena Gomez, Ozuna – Taki Taki
Daddy Yankee – Gasolina / Danza Kuduro
Don Omar – Danza Kuduro
Farruko – Pepas
J Balvin & Skrillex – In Da Ghetto
Bad Bunny – Tití Me Preguntó / Dákiti
Sean Paul – Get Busy / Temperature
Usher ft Lil Jon & Ludacris – Yeah / DJ Got Us Fallin’ In Love / OMG
Missy Elliott – Work It
Ginuwine – Pony
Lil Jon ft E-40 & Sean Paul – Snap Yo Fingers
Flo Rida – Club Can’t Handle Me / Right Round / Good Feeling
Pitbull ft Kesha – Timber
LMFAO – Party Rock Anthem / Shots
DJ Kool – Let Me Clear My Throat
Fatman Scoop – Be Faithful
DMX – Party Up
Montell Jordan – This Is How We Do It
House of Pain – Jump Around
Nelly – Hot In Herre / Ride Wit Me
Kanye West ft Jamie Foxx – Gold Digger
Ja Rule – Livin’ It Up
The Notorious B.I.G. – Mo Money Mo Problems
Joe Budden – Pump It Up
Sean Kingston – Fire Burning
Nicki Minaj – Super Bass / Starships
Doja Cat – Woman
Trey Songz ft Nicki Minaj – Bottoms Up
Waka Flocka Flame – No Hands
V.I.C. – Wobble
Ying Yang Twins ft Lil Jon – Salt Shaker

🕺 Pop-Punk / Rock Singalongs

Blink 182 – All The Small Things
Bowling For Soup – 1985
Fall Out Boy – Sugar, We’re Goin’ Down
The Killers – Mr. Brightside
Fountains of Wayne – Stacy’s Mom
Aerosmith – Walk This Way
Queen-Fisher – Bohemian Losing It (Mashup)
White Stripes – Seven Nation Army
Journey – Don’t Stop Believin’ (can double as finale)

💃 Latin / Reggaeton / International Party Section

Don Omar ft Lucenzo – Danza Kuduro
Daddy Yankee – Gasolina
J Balvin – Mi Gente / In Da Ghetto
Bad Bunny – Tití Me Preguntó / Dákiti
Farruko – Pepas
Ricky Martin – Un Dos Tres (Bootleg)
Elvis Crespo vs Steve Aoki – Suavemente / Azukita
El Alfa – La Mamá de la Mamá
Me Rehuso X Calm Down – Calm Down (Rema x Danny Ocean Segway)

💗 Slow / Romantic (Couples Moments)

Elvis Presley – Can’t Help Falling In Love
Marvin Gaye & Tammi Terrell – Ain’t No Mountain High Enough
Stevie Wonder – Isn’t She Lovely
Barry White – You’re The First, The Last, My Everything
Whitney Houston – I Wanna Dance With Somebody (start slow, then upbeat)
Taylor Swift – Love Story
Billy Joel – Piano Man (late-night singalong)

🎤 Finale / Singalong / Last Dance

Journey – Don’t Stop Believin’
Neil Diamond – Sweet Caroline
Queen – Don’t Stop Me Now
Mark Ronson ft Bruno Mars – Uptown Funk
Walk The Moon – Shut Up And Dance
Whitney Houston – I Wanna Dance With Somebody
"""

def parse_song_list(text):
    """Parses the song list text and returns a dictionary of categories and songs."""
    categories = {}
    current_category = None
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        # This is a naive way to check for a category line.
        # It assumes that lines with emojis or certain keywords are categories.
        if line.startswith('Ceremony') or line.startswith('💃') or line.startswith('🔥') or line.startswith('🕺') or line.startswith('💗') or line.startswith('🎤'):
            current_category = line
            categories[current_category] = []
        elif current_category:
            categories[current_category].append(line)
    return categories

def create_folders(categories):
    """Creates the category folders on the filesystem."""
    for category_name in categories.keys():
        # Sanitize folder name
        folder_name = "".join(c for c in category_name if c.isalnum() or c in (' ', '-')).rstrip()
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")

def get_music_files(directory):
    """Returns a list of music files in the given directory."""
    files = []
    for item in os.listdir(directory):
        if item.endswith(".mp3"): # Assuming the music files are in mp3 format
            files.append(item)
    return files

def sanitize_name(name):
    """Removes special characters and converts to lowercase."""
    return "".join(c for c in name if c.isalnum()).lower()

def move_files(categories, files, base_directory):
    """Moves files to their corresponding category folders."""
    moved_files = set()

    for file in files:
        file_title = get_song_title(file)
        sanitized_file_title = sanitize_name(file_title)
        moved = False
        for category_name, songs in categories.items():
            folder_name = "".join(c for c in category_name if c.isalnum() or c in (' ', '-')).rstrip()
            for song in songs:
                song_parts = [s.strip() for s in song.split('/')]
                for part in song_parts:
                    song_title_from_list = get_song_title(part)
                    sanitized_song_from_list = sanitize_name(song_title_from_list)

                    if sanitized_song_from_list == sanitized_file_title:
                        source_path = os.path.join(base_directory, file)
                        destination_path = os.path.join(folder_name, file)

                        if os.path.exists(source_path) and file not in moved_files:
                            os.rename(source_path, destination_path)
                            print(f"Moved '{file}' to '{folder_name}'")
                            moved_files.add(file)
                            moved = True
                            break
                if moved:
                    break
            if moved:
                break

    unmoved_files = set(files) - moved_files
    for file in unmoved_files:
        print(f"Could not find a category for '{file}'")

def get_song_title(s):
    # Remove file extension and apostrophes
    s = s.replace('.mp3', '').replace("'", "").replace("’", "")
    # Handle artist-title separation
    if '–' in s:
        s = s.split('–')[1].strip()
    elif '-' in s:
        s = s.split('-')[1].strip()

    # Specific handling for "You're" vs "You are"
    return s.lower().replace("youre", "youare")

if __name__ == "__main__":
    song_categories = parse_song_list(song_list_text)
    create_folders(song_categories)

    music_files_directory = "music_files"
    music_files = get_music_files(music_files_directory)

    move_files(song_categories, music_files, music_files_directory)

"""
Next steps:
1.  Read the list of files to be moved.
2.  For each file, determine which category it belongs to.
3.  Move the file to the corresponding folder.
"""
