# Convert Text Into Speaking Program In Python............///////////
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech

# The message you want the computer to speak
message = "Hello, zeeshan How are you!"

# Make the computer speak the message
engine.say(message)

# Wait for the speech to finish
engine.runAndWait()