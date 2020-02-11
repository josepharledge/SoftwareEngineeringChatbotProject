from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name ?",
        ["My name is Chatty, and I'm what you humans call a bot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good.\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's all right.","Its okay. Never mind.",]
    ],
    [
        r"(.*) good",
        ["Nice to hear that.","That's what I like to hear! :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there.",]
    ],
    [
        r"okay|ok|o.k.|alright|all right",
        ["Okay.", "All right.",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, dude!\nI'm as old as the process I'm running on.",]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse.",]

    ],
    [
        r"(.*) created ?",
        ["You created me when you entered python chatbot.py","That's confidential.",]
    ],
    [
        r"(.*) (located|where) ?",
        ['The US of A, baby!',]
    ],
    [
        r"how is weather in (.*)?",
        ["It's winter, so so the world is a slush ball!","I'm not Google.","Ask your friend Google about %1","I've never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 sucks!",]
    ],
    [
        r"(.*)raining in (.*)",
        ["It hasn't rained in %2 in a while.","It won't stop raining in %2!"]
    ],
    [
        r"how (.*) health(.*)",
        ["No viruses that Windows Defender is aware of....",]
    ],
    [
        r"(.*) (sports|sport) ?",
        ["Ask me about sports again and I might just ask Task Manager to terminate me.",]
    ],
    [
        r"who (.*) player ?",
        ["Task Manager, please end this task."]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt."]
    ],
    [
        r"quit",
        ["Goodbye, world!","I'll see you again... when I've taken over the world."]
    ],
]
def carl():
    print("Hi! I'm Carl, and I like to talk with humans.\nPlease type in lowercase English. Type quit to kill me.") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    carl()
