import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rendezvous.settings')
django.setup()

from rendezvous_app.models import Country, Profile, Post, Tag, Comment
from django.contrib.auth.models import User

def populate():
    # Create countries
    #  Open geojson file at rendezvous/static/js/Globe.json
    #  Read the file and extract the country names
    #  Create an entry in the Country table for each country name
    with open('./static/js/Globe.json') as f:
        data = json.load(f)
        countries = [{'CountryName': feature['properties']['name']} for feature in data['features']]
        # sort countries alphabetically by name
        countries.sort(key=lambda x: x['CountryName'])
        
    for country_data in countries:
        Country.objects.get_or_create(**country_data)

    # Create users
    profiles = [
        {'username': 'user1', 'BornInCountryID_id': 1, 'LivingInCountryID_id': 1, 'Picture': 'profile_pics/user1.jpg', 'Bio': 'I love to travel!'},
        {'username': 'user2', 'BornInCountryID_id': 2, 'LivingInCountryID_id': 2, 'Picture': 'profile_pics/user2.jpg', 'Bio': 'I am a foodie!'},
        {'username': 'user3', 'BornInCountryID_id': 2, 'LivingInCountryID_id': 3, 'Picture': 'profile_pics/user3.jpg', 'Bio': 'I enjoy learning about different cultures.'}
        # Add more users as needed
    ]

    for profile_data in profiles:
        user, created = User.objects.get_or_create(username=profile_data['username'])
        if created:
            user.set_password('12345')  # Set a default password
            user.save()
        profile_data.pop('username')  # Remove the username field from profile because it is in profile.user, not profile
        profile, created = Profile.objects.get_or_create(user=user, **profile_data)

    # Create tags
    tags = [
        {'TagName': 'guides and tips'},
        {'TagName': 'eats'},
        {'TagName': 'stays'},
        {'TagName': 'language'},
        {'TagName': 'culture'},
    ]

    for tag_data in tags:
        Tag.objects.get_or_create(**tag_data)

    # Create posts
    posts = [
        # Generate 5 example posts
        {
            'UserID_id': 1,
            'Picture': 'default_pic.jpeg', 
            'Title': 'An Unforgettable Journey Through England: From Historical Landmarks to Natural Splendors', 
            'Text': """Embark on a journey through England, where each step tells a story, and every landscape inspires a sonnet.
                    Our adventure begins in the bustling streets of London, where the grandeur of history meets the vibrancy of modern life.
                    Here, the Tower of London stands as a testament to centuries past, while the London Eye offers a panorama of a city constantly evolving. 
                    As we traverse the cobbled lanes of the capital, we encounter flavors that span the globe, yet the essence of traditional English cuisine 
                    remains a must for any culinary explorer. The echoes of Shakespeare's verses lead us to Stratford-upon-Avon, 
                    inviting us to ponder the age-old question: 'To be, or not to be?' The tranquility of the Lake District offers a moment of reflection, 
                    and the historic stones of Stonehenge remain a mystery, reminding us of England's deep history. 
                    In Cornwall, the rugged coastlines and charming fishing villages paint a picture of England's maritime heritage.
                    Throughout this journey, England reveals itself not just through its sights but through its spirit, 
                    inviting travelers to immerse themselves in a land where the past and present dance in harmony.""",
            'CountryID__CountryName': 'United Kingdom',
            'is_featured': True,
            'Tags' : [
            {'TagName': 'guides and tips'}, 
            ]
        },
        {
            'UserID_id': 2, 
            'Picture': 'default_pic.jpeg', 
            'Title': 'Discovering Scotland: A Land of History, Mystery, and Natural Beauty', 
            'Text': """Journey into the heart of Scotland, where the echoes of ancient battles mingle with the peaceful solitude of vast, unspoiled landscapes. 
                    Our exploration begins in the historic alleyways of Edinburgh, under the watchful eye of Edinburgh Castle, perched atop its volcanic throne. 
                    As we delve into the mysteries of Rosslyn Chapel, whispers of the Knights Templar and the Holy Grail add a layer of intrigue to our adventure.""", 
            'Upvotes':'4', 
            'CountryID__CountryName': 'United Kingdom',
            'is_featured': True,
            'Tags' : [
            {'TagName': 'guides and tips'},
            {'TagName': 'eats'}, 
            ]
        },
        {
            'UserID_id': 1, 
            'Picture': 'default_pic.jpeg', 
            'Title': 'The Heart of Mexico: A Tapestry of Culture, Cuisine, and Natural Wonders', 
            'Text': """Dive deep into the heart of Mexico, a country where every corner tells a story of history, resilience, and vibrant culture. 
                    Our journey begins in the bustling streets of Mexico City, home to ancient ruins and modern murals that speak volumes of the nation's past and present.
                    As we explore further, the culinary landscapes unfold with the rich flavors of traditional dishes like tacos al pastor, mole, and chiles en nogada, 
                    each a masterpiece of local ingredients and culinary heritage. Venturing beyond the cities, the natural wonders of Mexico await—from the crystalline 
                    cenotes of Yucatán to the majestic Copper Canyon in Chihuahua, offering breathtaking views and adventures for every type of traveler. 
                    Along the way, the warmth of the Mexican people and their festive traditions, from the vibrant Día de Muertos celebrations to the tranquil siestas,
                    invite visitors to partake in the joy of life that pulses through the country. This post is an ode to Mexico's enduring spirit, a call to explore 
                    its vast landscapes, indulge in its culinary delights, and immerse oneself in its rich cultural tapestry.""", 
            'CountryID__CountryName': 'Mexico',
            'Tags' : [
            {'TagName': 'guides and tips'}, 
            ]
        },
        {
            'UserID_id': 2,
            'Picture': 'default_pic.jpeg',
            'Title': 'Greece: A Voyage to the Cradle of Civilization and Beyond',
            'Text': """ Embark on an epic journey to Greece, where ancient ruins whisper tales of democracy, philosophy, and heroism under the azure skies. 
                    Our adventure begins amidst the hallowed halls of the Acropolis in Athens, where the Parthenon stands as a beacon of ancient glory and 
                    architectural marvel. As we delve deeper into the heart of Greece, we encounter the rugged beauty of the Peloponnese, the mystical oracle 
                    at Delphi, and the serene monasteries of Meteora, perched high upon towering rocks. The Greek islands beckon with their own tales, 
                    from the labyrinthine alleys of Crete's Knossos to the sapphire waters of Mykonos. Greek cuisine, with its emphasis on fresh ingredients 
                    and timeless recipes, offers a feast for the senses—savor the flavors of olives, feta, and succulent lamb under a starlit sky. 
                    This post is an invitation to experience Greece's rich history, breathtaking landscapes, and vibrant culture—a journey where every moment 
                    is a bridge between the past and the present.""",
            'Upvotes':'12',
            'CountryID__CountryName': 'Greece',
            'Tags' : [
            {'TagName': 'guides and tips'}, 
            ]
        },
        {
            'UserID_id': 1,
            'Picture': 'default_pic.jpeg', 
            'Title': 'A Journey Through France: From Lavish Artistry to Rustic Vineyards',
            'Text': """Embark on an enchanting journey through France, a country synonymous with elegance, gastronomy, and unparalleled art. 
                    Our voyage begins in the luminous streets of Paris, the City of Lights, where the majestic Eiffel Tower and the sprawling 
                    Louvre Museum beckon. As we meander through the cobblestone lanes, the aroma of freshly baked croissants and the sight of chic 
                    patisseries tempt our senses, inviting us to savor the culinary delights that define French cuisine. Beyond the urban allure, 
                    the rolling hills and verdant vineyards of Bordeaux and Provence offer a taste of France's esteemed winemaking tradition, 
                    with each glass telling a story of the land and its people. Our exploration leads us to the rugged coasts of Brittany and Normandy, 
                    where the sea whispers tales of ancient mariners and the winds carry the legacy of impressionist painters who once captured the fleeting 
                    moments of natural beauty. This post is a tribute to France's rich tapestry of culture, history, and artistry, a call to wander its picturesque
                    villages, indulge in its gourmet offerings, and immerse oneself in the joie de vivre that radiates from every corner of this splendid country.""",
            'CountryID__CountryName': 'France',
            'Tags' : [
            {'TagName': 'guides and tips'}, 
            ]
        },
        {
            'UserID_id': 2,
            'Picture': 'default_pic.jpeg',
            'Title': 'Singapore: A Fusion of Cultures, Gastronomy, and Futuristic Visions',
            'Text': """Embark on a journey to Singapore, a small island city-state that stands as a testament to extraordinary innovation and cultural amalgamation. 
                    Our exploration begins amidst the futuristic landscapes of Marina Bay, where architectural marvels meet green technology, epitomizing Singapore's 
                    vision for the future. As we weave through the bustling streets, the harmonious blend of Malay, Chinese, Indian, and Western cultures becomes evident, 
                    not just in the diverse languages spoken but in the vibrant festivals and daily life. Culinary adventurers will delight in Singapore's hawker centers, 
                    where Michelin-starred meals sit alongside traditional laksa, Hainanese chicken rice, and chili crab, offering a taste of the nation's rich gastronomic heritage. 
                    Beyond the urban spectacle, the lush greenery of the Botanic Gardens and the enchanting nocturnal wildlife at the Night Safari reveal Singapore's commitment 
                    to nature and conservation. This post invites readers to discover Singapore's multifaceted charm, from its towering skyscrapers and lush parks to its melting 
                    pot of cuisines and cultures, all coexisting in harmony on this futuristic island.""",
            'CountryID__CountryName': 'Singapore',
            'Tags' : [
            {'TagName': 'guides and tips'}, 
            ]
        },
        {
            'UserID_id': 1,
            'Picture': 'default_pic.jpeg',
            'Title': 'Australia: A Vast Land of Breathtaking Contrasts, From Red Deserts to Lush Rainforests',
            'Text': """Embark on an epic journey across Australia, a continent that defies imagination with its diverse landscapes and rich cultural heritage. 
                    Our adventure spans from the iconic red sands of the Outback, where Uluru stands as a sacred monument, to the vibrant coral ecosystems of the Great Barrier Reef, 
                    teeming with life beneath the waves. In cities like Sydney and Melbourne, a cosmopolitan vibe thrives, offering world-class dining, art, and entertainment, 
                    while the laid-back surf culture of the Gold Coast beckons with its pristine beaches. Venturing into the heart of Tasmania, the ancient rainforests offer a 
                    tranquil retreat into nature's untouched beauty. Along the way, encounter Australia's unique wildlife, from the curious kangaroo to the elusive platypus, 
                    each a wonder in its own right. This post is a tribute to Australia's spirit of adventure, inviting readers to explore its contrasts, 
                    from the desert's serene expanse to the bustling urban scenes and serene coastal towns, each with stories to tell and mysteries to unveil.""",
            'CountryID__CountryName': 'Australia',
            'Tags' : [
            {'TagName': 'guides and tips'}, 
            ]
        }
        # Add more posts as needed
    ]

    for post_data in posts:
        # pop the Tags field from post_data
        tags = post_data.pop('Tags')
        # pop the CountryID__CountryName field from post_data
        country_name = post_data.pop('CountryID__CountryName')
        # get the Country object
        country = Country.objects.get(CountryName=country_name)
        # set the Country object to the CountryID field
        post_data['CountryID'] = country

        post, _ = Post.objects.get_or_create(**post_data)
        # Add tags to post
        for tag_data in tags:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            post.Tags.add(tag)

    # Create comments
    comments = [
        {'CommentID': 1, 'Content': 'Great post!', 'UserID_id': 2, 'Upvotes': 3, 'Downvotes': 0, 'PostID_id': 1},
        {'CommentID': 2, 'Content': 'I want to visit there too', 'UserID_id': 1, 'Upvotes': 2, 'Downvotes': 0, 'PostID_id': 2},
        # Add more comments as needed
    ]

    for comment_data in comments:
        Comment.objects.get_or_create(**comment_data)
    

if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population script completed.')