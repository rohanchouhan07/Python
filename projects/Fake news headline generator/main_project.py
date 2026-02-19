# Fake news generator
import random as rd
print("WELCOME TO FAKE NEWS GENERATOR")

subjects = [
    # Actors / Actresses
    "Barack Obama","Narendra Modi","Vladimir Putin",
    "Elon Musk","Gates","Cristiano Ronaldo","Lionel Messi",
    "Amitabh Bachchan","Dilip Kumar","Raj Kapoor","Dev Anand",
    "Naseeruddin Shah","Shashi Kapoor","Kishore Kumar",
        "Anupam Kher","Mithun Chakraborty","Om Puri"
]

actions = [
    "perform", "act", "direct", "produce", "sing", "dance", "write", "compose", 
    "govern", "lead", "campaign", "legislate", "debate", "negotiate", "represent",
    "innovate", "invest", "build", "launch", "design", "create", "strategize",
    "advocate", "organize", "educate", "campaign", "protest",
    "compete", "train", "score", "win", "practice", "coach",
    "perform", "record", "compose", "tour", "inspire",
    "speak", "interview", "host", "broadcast", "share", "engage"
]

Objects_contexts = [
    "project", "idea", "plan", "report", "strategy", "presentation", "performance", "speech",
    "guitar", "piano", "camera", "computer", "software", "vehicle", "microphone", "script", "book", "document",
    "stage", "office", "studio", "arena", "conference hall", "classroom", "laboratory", "field", "court", "stadium",
    "meeting", "conference", "campaign", "workshop", "seminar", "protest", "concert", "exhibition",
    "website", "social media", "blog", "app", "virtual meeting", "live stream", "podcast",
    "match", "tournament", "race", "training session", "gym", "track", "pitch",
    "song", "painting", "article", "movie", "design", "product", "invention"
]
s="yes"
while True:
    sub=rd.choice(subjects)
    act=rd.choice(actions)
    obj=rd.choice(Objects_contexts)
    print(sub,act,obj)
    s=input("enter yes if you want to see another otherwise type no \n" ).strip().lower()
    if s=="no":
        exit()