import re
import json


def extract_event_data(markdown_text):
    """
    Extracts event information from markdown text and returns a list of event dictionaries.
    """
    # Split the markdown text into event blocks.
    event_blocks = markdown_text.strip().split("*   ")

    events = []
    for event_block in event_blocks:
        if len(event_block) == 0:
            continue

        brackets = re.findall(r"\((.*?)\)", event_block)

        lines = event_block.split("\n")

        # Extract image URL and event URL from the first line.
        image_url = brackets[0]
        event_url = brackets[1]

        # Extract title from the second line.
        title = re.findall(r"\[(.*?)\]", event_block)[3]

        # Extract date and time from the third line.
        date_time_str = lines[12].strip()

        if " at " in date_time_str:
            day, time = date_time_str.split(" at ")
            date = ""
        else:
            day , date, time = date_time_str.split(", ")

        # Extract location from the fourth lin
        if len(lines) > 13:
            location = lines[14]
        else:
            location = "TBD"

        # Create a dictionary for the event and append it to the list.
        event = {
            "title": title,
            "date": day + " " + date,
            "time": time,
            "location": location,
            "image_url": image_url,
            "event_url": event_url
        }
        events.append(event)

    return events


# Example usage:
markdown_text = """*   [![Image 1: CLT Spring Fest Finale: Late Night Attention ft. Mariah The Scientist primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F724594509%2F1494144234503%2F1%2Foriginal.20240320-223135?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=88fd75baa6c4bb21caaeedfc1a44461a)](https://www.eventbrite.com/e/clt-spring-fest-finale-late-night-attention-ft-mariah-the-scientist-tickets-855555408257?aff=ebdssbdestsearch)

[CLT Spring Fest Finale: Late Night Attention ft. Mariah The Scientist ](https://www.eventbrite.com/e/clt-spring-fest-finale-late-night-attention-ft-mariah-the-scientist-tickets-855555408257?aff=ebdssbdestsearch)

Tomorrow at 10:00 PM

Superstarz CLT

[![Image 2: CLT Spring Fest Finale: Late Night Attention ft. Mariah The Scientist primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F724594509%2F1494144234503%2F1%2Foriginal.20240320-223135?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=88fd75baa6c4bb21caaeedfc1a44461a)](https://www.eventbrite.com/e/clt-spring-fest-finale-late-night-attention-ft-mariah-the-scientist-tickets-855555408257?aff=ebdssbdestsearch)

[CLT Spring Fest Finale: Late Night Attention ft. Mariah The Scientist ](https://www.eventbrite.com/e/clt-spring-fest-finale-late-night-attention-ft-mariah-the-scientist-tickets-855555408257?aff=ebdssbdestsearch)

Tomorrow at 10:00 PM

Superstarz CLT

*   [![Image 3: Freakfestclt returns! Free entry till 11:30! $400 2 bottles! primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F745918139%2F60173928473%2F1%2Foriginal.20240417-161558?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&s=6456c1e2a4538fb41164a5cc8c8dd5f9)](https://www.eventbrite.com/e/freakfestclt-returns-free-entry-till-1130-400-2-bottles-tickets-847259474897?aff=ebdssbdestsearch)

[Freakfestclt returns! Free entry till 11:30! $400 2 bottles! ](https://www.eventbrite.com/e/freakfestclt-returns-free-entry-till-1130-400-2-bottles-tickets-847259474897?aff=ebdssbdestsearch)

Fri, Apr 26, 10:00 PM

Compound Clt

[![Image 4: Freakfestclt returns! Free entry till 11:30! $400 2 bottles! primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F745918139%2F60173928473%2F1%2Foriginal.20240417-161558?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&s=6456c1e2a4538fb41164a5cc8c8dd5f9)](https://www.eventbrite.com/e/freakfestclt-returns-free-entry-till-1130-400-2-bottles-tickets-847259474897?aff=ebdssbdestsearch)

[Freakfestclt returns! Free entry till 11:30! $400 2 bottles! ](https://www.eventbrite.com/e/freakfestclt-returns-free-entry-till-1130-400-2-bottles-tickets-847259474897?aff=ebdssbdestsearch)

Fri, Apr 26, 10:00 PM

Compound Clt

*   [![Image 5: The Lowe's "Got Soul: Savor the Culture" Festival primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F742036319%2F267848188995%2F1%2Foriginal.20240412-113555?w=361&auto=format%2Ccompress&q=75&sharp=10&s=8197d0cd67b3087d9612888107dd70d6)](https://www.eventbrite.com/e/the-lowes-got-soul-savor-the-culture-festival-tickets-779832318457?aff=ebdssbdestsearch)

[The Lowe's "Got Soul: Savor the Culture" Festival -](https://www.eventbrite.com/e/the-lowes-got-soul-savor-the-culture-festival-tickets-779832318457?aff=ebdssbdestsearch)

Sat, Apr 27, 3:00 PM

The Amp Ballantyne, Upper Ave, Charlotte, NC, USA

[![Image 6: The Lowe's "Got Soul: Savor the Culture" Festival primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F742036319%2F267848188995%2F1%2Foriginal.20240412-113555?w=361&auto=format%2Ccompress&q=75&sharp=10&s=8197d0cd67b3087d9612888107dd70d6)](https://www.eventbrite.com/e/the-lowes-got-soul-savor-the-culture-festival-tickets-779832318457?aff=ebdssbdestsearch)

[The Lowe's "Got Soul: Savor the Culture" Festival -](https://www.eventbrite.com/e/the-lowes-got-soul-savor-the-culture-festival-tickets-779832318457?aff=ebdssbdestsearch)

Sat, Apr 27, 3:00 PM

The Amp Ballantyne, Upper Ave, Charlotte, NC, USA

*   [![Image 7: Charlotte Grilled Cheese Festival 2024 primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F714972549%2F23349073362%2F1%2Foriginal.20240308-165409?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=265ec3f0117f4deaa0395c2d0b0881d0)](https://www.eventbrite.com/e/charlotte-grilled-cheese-festival-2024-tickets-853118038017?aff=ebdssbdestsearch)

[Charlotte Grilled Cheese Festival 2024 --](https://www.eventbrite.com/e/charlotte-grilled-cheese-festival-2024-tickets-853118038017?aff=ebdssbdestsearch)

Sat, Apr 27, 1:00 PM

SouthEnd Station Parking Lot

[![Image 8: Charlotte Grilled Cheese Festival 2024 primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F714972549%2F23349073362%2F1%2Foriginal.20240308-165409?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=265ec3f0117f4deaa0395c2d0b0881d0)](https://www.eventbrite.com/e/charlotte-grilled-cheese-festival-2024-tickets-853118038017?aff=ebdssbdestsearch)

[Charlotte Grilled Cheese Festival 2024 --](https://www.eventbrite.com/e/charlotte-grilled-cheese-festival-2024-tickets-853118038017?aff=ebdssbdestsearch)

Sat, Apr 27, 1:00 PM

SouthEnd Station Parking Lot

*   [![Image 9: INVIRTIENDO EN BIENES RAICES CON EXITO EN EL 2024! CHARLOTTE NC primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F737745269%2F1052047509583%2F1%2Foriginal.20240407-144127?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=a5dced80cce883d72714ef16071ebec7)](https://www.eventbrite.com/e/invirtiendo-en-bienes-raices-con-exito-en-el-2024-charlotte-nc-tickets-831227934127?aff=ebdssbdestsearch)

[INVIRTIENDO EN BIENES RAICES CON EXITO EN EL 2024! CHARLOTTE NC ](https://www.eventbrite.com/e/invirtiendo-en-bienes-raices-con-exito-en-el-2024-charlotte-nc-tickets-831227934127?aff=ebdssbdestsearch)

Sat, May 11, 8:00 AM

2800 Coliseum Centre Dr

[![Image 10: INVIRTIENDO EN BIENES RAICES CON EXITO EN EL 2024! CHARLOTTE NC primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F737745269%2F1052047509583%2F1%2Foriginal.20240407-144127?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=a5dced80cce883d72714ef16071ebec7)](https://www.eventbrite.com/e/invirtiendo-en-bienes-raices-con-exito-en-el-2024-charlotte-nc-tickets-831227934127?aff=ebdssbdestsearch)

[INVIRTIENDO EN BIENES RAICES CON EXITO EN EL 2024! CHARLOTTE NC ](https://www.eventbrite.com/e/invirtiendo-en-bienes-raices-con-exito-en-el-2024-charlotte-nc-tickets-831227934127?aff=ebdssbdestsearch)

Sat, May 11, 8:00 AM

2800 Coliseum Centre Dr

*   [![Image 11: Blazers and Bling primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F690706649%2F268899599709%2F1%2Foriginal.20240206-014850?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C12%2C1024%2C512&s=64e9315b9d42611938c8855b261e9d74)](https://www.eventbrite.com/e/blazers-and-bling-tickets-818512441747?aff=ebdssbdestsearch)

[Blazers and Bling --](https://www.eventbrite.com/e/blazers-and-bling-tickets-818512441747?aff=ebdssbdestsearch)

Tomorrow at 3:00 PM

RSVP South End

[![Image 12: Blazers and Bling primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F690706649%2F268899599709%2F1%2Foriginal.20240206-014850?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C12%2C1024%2C512&s=64e9315b9d42611938c8855b261e9d74)](https://www.eventbrite.com/e/blazers-and-bling-tickets-818512441747?aff=ebdssbdestsearch)

[Blazers and Bling --](https://www.eventbrite.com/e/blazers-and-bling-tickets-818512441747?aff=ebdssbdestsearch)

Tomorrow at 3:00 PM

RSVP South End

*   [![Image 13: CLT Spring Fest Friday: Freaks, Greeks, and Athletes primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F746289789%2F1494144234503%2F1%2Foriginal.20240417-232521?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=797009ea151b7236ab9194907accdd38)](https://www.eventbrite.com/e/clt-spring-fest-friday-freaks-greeks-and-athletes-tickets-877668318567?aff=ebdssbdestsearch)

[CLT Spring Fest Friday: Freaks, Greeks, and Athletes -](https://www.eventbrite.com/e/clt-spring-fest-friday-freaks-greeks-and-athletes-tickets-877668318567?aff=ebdssbdestsearch)

Today at 10:00 PM

Brooklyn Nightclub and Lounge

[![Image 14: CLT Spring Fest Friday: Freaks, Greeks, and Athletes primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F746289789%2F1494144234503%2F1%2Foriginal.20240417-232521?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C2160%2C1080&s=797009ea151b7236ab9194907accdd38)](https://www.eventbrite.com/e/clt-spring-fest-friday-freaks-greeks-and-athletes-tickets-877668318567?aff=ebdssbdestsearch)

[CLT Spring Fest Friday: Freaks, Greeks, and Athletes -](https://www.eventbrite.com/e/clt-spring-fest-friday-freaks-greeks-and-athletes-tickets-877668318567?aff=ebdssbdestsearch)

Today at 10:00 PM

Brooklyn Nightclub and Lounge

*   [![Image 15: Official Tacos N Tequila Bar Crawl Charlotte Cinco De Mayo Bar Crawl LIVE primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F704563819%2F196710296272%2F1%2Foriginal.20240224-225526?h=200&w=400&auto=format%2Ccompress&q=75&sharp=10&s=dadeee6304fd566ce7f6837f0baa61d4)](https://www.eventbrite.com/e/official-tacos-n-tequila-bar-crawl-charlotte-cinco-de-mayo-bar-crawl-live-tickets-850170020417?aff=ebdssbdestsearch)

[Official Tacos N Tequila Bar Crawl Charlotte Cinco De Mayo Bar Crawl LIVE -](https://www.eventbrite.com/e/official-tacos-n-tequila-bar-crawl-charlotte-cinco-de-mayo-bar-crawl-live-tickets-850170020417?aff=ebdssbdestsearch)

Sat, May 4, 10:00 AM

Tattooz & Booz

[![Image 16: Official Tacos N Tequila Bar Crawl Charlotte Cinco De Mayo Bar Crawl LIVE primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F704563819%2F196710296272%2F1%2Foriginal.20240224-225526?h=200&w=400&auto=format%2Ccompress&q=75&sharp=10&s=dadeee6304fd566ce7f6837f0baa61d4)](https://www.eventbrite.com/e/official-tacos-n-tequila-bar-crawl-charlotte-cinco-de-mayo-bar-crawl-live-tickets-850170020417?aff=ebdssbdestsearch)

[Official Tacos N Tequila Bar Crawl Charlotte Cinco De Mayo Bar Crawl LIVE -](https://www.eventbrite.com/e/official-tacos-n-tequila-bar-crawl-charlotte-cinco-de-mayo-bar-crawl-live-tickets-850170020417?aff=ebdssbdestsearch)

Sat, May 4, 10:00 AM

Tattooz & Booz

*   [![Image 17: Nothin But Anthems: Charlotte primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F720592809%2F550880913871%2F1%2Foriginal.20240315-180707?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=3%2C0%2C1914%2C957&s=4efe3d73feda022cbf0941d531a64148)](https://www.eventbrite.com/e/nothin-but-anthems-charlotte-tickets-860618873217?aff=ebdssbdestsearch)

[Nothin But Anthems: Charlotte --](https://www.eventbrite.com/e/nothin-but-anthems-charlotte-tickets-860618873217?aff=ebdssbdestsearch)

Sun, May 5, 5:00 PM

RSVP South End

[![Image 18: Nothin But Anthems: Charlotte primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F720592809%2F550880913871%2F1%2Foriginal.20240315-180707?h=200&w=512&auto=format%2Ccompress&q=75&sharp=10&rect=3%2C0%2C1914%2C957&s=4efe3d73feda022cbf0941d531a64148)](https://www.eventbrite.com/e/nothin-but-anthems-charlotte-tickets-860618873217?aff=ebdssbdestsearch)

[Nothin But Anthems: Charlotte --](https://www.eventbrite.com/e/nothin-but-anthems-charlotte-tickets-860618873217?aff=ebdssbdestsearch)

Sun, May 5, 5:00 PM

RSVP South End

*   [![Image 19: Unity in the Community - Praise and Worship with Pastor Shirley Caesar primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F737573279%2F161880081586%2F1%2Foriginal.20240407-002512?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C3000%2C1500&s=b40ae2d165c9dbff7c48d08416d96923)](https://www.eventbrite.com/e/unity-in-the-community-praise-and-worship-with-pastor-shirley-caesar-tickets-877599623097?aff=ebdssbdestsearch)

[Unity in the Community - Praise and Worship with Pastor Shirley Caesar -](https://www.eventbrite.com/e/unity-in-the-community-praise-and-worship-with-pastor-shirley-caesar-tickets-877599623097?aff=ebdssbdestsearch)

Sunday at 4:00 PM

The Park Church Beatties Ford

[![Image 20: Unity in the Community - Praise and Worship with Pastor Shirley Caesar primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F737573279%2F161880081586%2F1%2Foriginal.20240407-002512?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C0%2C3000%2C1500&s=b40ae2d165c9dbff7c48d08416d96923)](https://www.eventbrite.com/e/unity-in-the-community-praise-and-worship-with-pastor-shirley-caesar-tickets-877599623097?aff=ebdssbdestsearch)

[Unity in the Community - Praise and Worship with Pastor Shirley Caesar -](https://www.eventbrite.com/e/unity-in-the-community-praise-and-worship-with-pastor-shirley-caesar-tickets-877599623097?aff=ebdssbdestsearch)

Sunday at 4:00 PM

The Park Church Beatties Ford

*   [![Image 21: ⭐-⭐ SO FAR GONE ⭐-⭐ Cinco De Mayo Edition primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F725147449%2F8726145409%2F1%2Foriginal.20240321-154144?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C176%2C1200%2C600&s=9ab0c0037fe8707331c8a19f2e6ee613)](https://www.eventbrite.com/e/-so-far-gone-cinco-de-mayo-edition-tickets-867425361607?aff=ebdssbdestsearch)

[⭐-⭐ SO FAR GONE ⭐-⭐ Cinco De Mayo Edition --](https://www.eventbrite.com/e/-so-far-gone-cinco-de-mayo-edition-tickets-867425361607?aff=ebdssbdestsearch)

Sun, May 5, 4:00 PM

Encore Nightclub Charlotte

[![Image 22: ⭐-⭐ SO FAR GONE ⭐-⭐ Cinco De Mayo Edition primary image](https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F725147449%2F8726145409%2F1%2Foriginal.20240321-154144?w=512&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C176%2C1200%2C600&s=9ab0c0037fe8707331c8a19f2e6ee613)](https://www.eventbrite.com/e/-so-far-gone-cinco-de-mayo-edition-tickets-867425361607?aff=ebdssbdestsearch)

[⭐-⭐ SO FAR GONE ⭐-⭐ Cinco De Mayo Edition --](https://www.eventbrite.com/e/-so-far-gone-cinco-de-mayo-edition-tickets-867425361607?aff=ebdssbdestsearch)

Sun, May 5, 4:00 PM
"""

events = extract_event_data(markdown_text)

# Convert the list of events to JSON format.
json_data = json.dumps(events, indent=4)

# Print the JSON data.
print(json_data)