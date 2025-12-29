import random
import time

# random nouns , verbs , adverbs, articles and joining words for forming random sentences using import random as well as random.choice.
nouns = ["apple", "mountain", "river", "chair", "laptop", "ocean", "forest", "cloud", "bicycle", "library",
  "mirror", "garden", "window", "candle", "pencil", "clock", "backpack", "island", "bridge", "camera",
  "notebook", "lantern", "pillow", "bottle", "carpet", "satellite", "tunnel", "helmet", "elevator", "volcano",
  "keyboard", "painting", "statue", "wallet", "telescope", "basket", "diamond", "ladder", "cupboard", "fountain",
  "anchor", "calendar", "blanket", "microscope", "bracelet", "hammer", "envelope", "staircase", "battery",
  "compass", "trophy", "matches", "coin", "drawer", "jacket", "rug", "shelf", "sworwoski", "token",
  "violin", "whistle", "barrel", "button", "castle", "desert", "engine", "feather", "galaxy", "harbor",
  "ink", "jewel", "kettle", "leaf", "machine", "weedle", "orchard", "pikachu", "quagsire", "religant",
  "signal", "temple", "umbrella", "vessel", "wheel", "xylophone", "slaking", "zipper", "shadow-mewtwo", "zapdos",
  "dog", "cat", "bat", "bird"]

verbs =["run", "jump", "walk", "talk", "write", "read", "drive", "fly", "swim", "climb",
  "think", "create", "build", "break", "catch", "throw", "push", "pull", "lift", "drop",
  "open", "close", "start", "stop", "move", "wait", "listen", "speak", "watch", "learn",
  "teach", "play", "sing", "dance", "laugh", "cry", "sleep", "wake", "eat", "drink",
  "cook", "bake", "clean", "wash", "draw", "paint", "design", "code", "debug", "test",
  "plan", "organize", "lead", "follow", "help", "support", "share", "give", "take", "receive",
  "send", "build", "repair", "fix", "destroy", "grow", "shrink", "change", "improve", "reduce",
  "explore", "travel", "arrive", "leave", "enter", "exit", "search", "find", "lose", "discover",
  "believe", "decide", "choose", "prefer", "try", "fail", "succeed", "focus", "relax", "rest"]

adverbs = [
  "slowly", "quickly", "lazily", "happily", "sadly", "angrily", "quietly", "loudly", "softly", "boldly",
  "carefully", "carelessly", "eagerly", "reluctantly", "politely", "rudely", "patiently", "impatiently",
  "bravely", "fearfully", "calmly", "nervously", "confidently", "doubtfully", "honestly", "dishonestly",
  "easily", "hardly", "barely", "nearly", "fully", "partially", "completely", "abruptly", "smoothly",
  "gently", "roughly", "sharply", "brightly", "dimly", "warmly", "coldly", "firmly", "loosely", "tightly",
  "closely", "distantly", "freely", "randomly", "regularly", "rarely", "often", "sometimes", "always",
  "never", "soon", "late", "early", "today", "yesterday", "tomorrow", "already", "finally", "eventually",
  "suddenly", "gradually", "briefly", "forever", "temporarily", "immediately", "eventually", "carefully",
  "wildly", "smoothly", "politely", "cheerfully", "gracefully", "silently", "noisily", "brightly"
]

articles = [
  "The", "A", "An", "They", "This", "That", "These", "Those", "My", "Your",
  "His", "Her", "Its", "Our", "Their", "Some", "Any", "Each", "Every", "No",
  "One", "Two", "Few", "Many", "Several", "All", "Both", "Either", "Neither", "Such",
  "What", "Which", "Whose", "Another", "Other", "Same", "Certain", "Various", "Enough", "Much",
  "Little", "More", "Most", "Less", "Least", "First", "Second", "Next", "Last", "Previous",
  "This", "That", "These", "Those", "The", "A", "An", "They", "My", "Your",
  "His", "Her", "Our", "Their", "Some", "Any", "Each", "Every", "No", "All",
  "Both", "Either", "Neither", "Several", "Many", "Few", "Another", "Other", "Same", "Such",
  "Certain", "Various", "Enough", "Much", "Little", "More", "Most", "Less", "Least", "All"
]

joining_words = [
  "and", "or", "but", "so", "yet", "for", "nor", "although", "because", "since",
  "unless", "while", "whereas", "after", "before", "when", "whenever", "until", "once", "if",
  "though", "even", "even though", "as", "as if", "as long as", "as soon as", "whether", "rather than", "than",
  "that", "which", "who", "whom", "whose", "where", "wherever", "why", "how", "therefore",
  "however", "moreover", "furthermore", "otherwise", "meanwhile", "likewise", "instead", "otherwise", "hence", "thus",
  "consequently", "similarly", "nevertheless", "nonetheless", "still", "also", "too", "either", "neither", "both",
  "not only", "but also", "in addition", "on the other hand", "for example", "for instance", "in contrast", "in conclusion", "in fact", "in summary",
  "despite", "in spite of", "due to", "because of", "owing to", "along with", "together with", "as well as", "including", "excluding"
]


target_text = (
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    f"{random.choice(joining_words)} "
    f"{random.choice(articles)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)} "
    
)


print("Type this fast:")
print(target_text)


input("Press Enter to start...")
start_time = time.time()

user_input = input("\nStart Typing: ")
end_time = time.time()

if user_input.lower().strip() == target_text.lower().strip():
    time_taken = end_time - start_time
    print(f"Time taken: {time_taken:.2f} seconds")
else:
    print("Try again")



