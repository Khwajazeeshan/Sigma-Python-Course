# Using Regular Expression In Python...........//////////////////
"""
A regular expression, often referred to as "regex," is a powerful tool used in programming to find and manipulate patterns in text.
It's like a special language that helps you describe and search for specific combinations of characters in strings.
"""
import re

pattern = "small"
pattern1 = r"[A-Z]+yclone"
text = '''
The sun was setting behind the hills, casting a warm and golden glow over the landscape. Birds were chirping their 
evening songs, and a gentle breeze rustled the leaves of the trees. It was a peaceful scene that seemed to bring a 
sense of calm to anyone who happened to be there.
In the distance, a small farmhouse stood with its windows reflecting the last rays of sunlight. Smoke rose from the
chimney, carrying with it the comforting scent of a home-cooked meal. Inside, a family gathered around the dining table, 
sharing stories of their day and laughing together.
As the evening progressed, the sky transformed into a canvas of vibrant colors – shades of orange, pink, and purple
painted across the horizon. The first stars timidly peeked through the darkening sky, and the world started to quiet down.
Down the road, a little stream meandered through the meadows, its gentle babbling providing a soothing soundtrack to
the serene landscape. The water sparkled as it caught the fading light, and the pebbles at the bottom seemed to shimmer
like hidden treasures.
In the town nearby, the streets were lined with quaint shops that were closing up for the day. Shopkeepers chatted with 
the last few customers, their voices filled with the familiarity of a community that had known each other for years.
In the park, children's laughter echoed as they played on swings and slides. Parents watched over them, smiling at their
boundless energy and innocence. cyclone Dyclone Hyclone.
'''
match = re.search(pattern, text)
print(match)
match = re.search(pattern1, text)
print(match)