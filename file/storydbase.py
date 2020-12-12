import pyttsx3
import random


engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

list = [
    'Here is a story with Moral Lying breaks trust  even if you’re telling the truth, no one believes a liar. Let us start the story. Once, there was a boy who became bored when he watched over the village sheep grazing on the hillside. To entertain himself, he sang out, Wolf! Wolf! The wolf is chasing the sheep! When the villagers heard the cry, they came running up the hill to drive the wolf away. But, when they arrived, they saw no wolf. The boy was amused when seeing their angry faces. Don’t scream wolf, boy, warned the villagers, when there is no wolf! They angrily went back down the hill. Later, the shepherd boy cried out once again, Wolf! Wolf! The wolf is chasing the sheep! To his amusement, he looked on as the villagers came running up the hill to scare the wolf away. As they saw there was no wolf, they said strictly, Save your frightened cry for when there really is a wolf! Don’t cry wolf when there is no wolf! But the boy grinned at their words while they walked grumbling down the hill once more. Later, the boy saw a real wolf sneaking around his flock. Alarmed, he jumped on his feet and cried out as loud as he could, Wolf! Wolf! But the villagers thought he was fooling them again, and so they didn’t come to help. At sunset, the villagers went looking for the boy who had not returned with their sheep. When they went up the hill, they found him weeping. There really was a wolf here! The flock is gone! I cried out, Wolf! but you didn’t come, he wailed. An old man went to comfort the boy. As he put his arm around him, he said, Nobody believes a liar, even when he is telling the truth!',
    'Here is a story with moral Greed will always lead to downfall. Let us start the story. There once was a king named Midas who did a good deed for a Satyr. And he was then granted a wish by Dionysus, the god of wine. For his wish, Midas asked that whatever he touched would turn to gold. Despite Dionysus efforts to prevent it, Midas pleaded that this was a fantastic wish, and so, it was bestowed. Excited about his newly-earned powers, Midas started touching all kinds of things, turning each item into pure gold. But soon, Midas became hungry. As he picked up a piece of food, he found he couldn’t eat it. It had turned to gold in his hand. Hungry, Midas groaned, I will starve! Perhaps this was not such an excellent wish after all! Seeing his dismay, Midas beloved daughter threw her arms around him to comfort him, and she, too, turned to gold. The golden touch is no blessing, Midas cried.',
    'Here is a story with moral Never despise what we can not have nothing comes easy. Let us start the story. One day, a fox became very hungry as he went to search for some food. He searched high and low, but could not find something that he could eat. Finally, as his stomach rumbled, he stumbled upon a farmers wall. At the top of the wall, he saw the biggest, juiciest grapes he had ever seen. They had a rich, purple color, telling the fox they were ready to be eaten. To reach the grapes, the fox had to jump high in the air. As he jumped, he opened his mouth to catch the grapes, but he missed. The fox tried again but missed yet again. He tried a few more times but kept failing. Finally, the fox decided it was time to give up and go home. While he walked away, he muttered, I am sure the grapes were sour anyway',
    'Here is a story with Moral Never judge anyone by the way they look. Let us start the story. Once upon a time, in a desert far away, there was a rose who was so proud of her beautiful looks. Her only complaint was growing next to an ugly cactus. Every day, the beautiful rose would insult and mock the cactus on his looks, all while the cactus remained quiet. All the other plants nearby tried to make the rose see sense, but she was too swayed by her own looks. One scorching summer, the desert became dry, and there was no water left for the plants. The rose quickly began to wilt. Her beautiful petals dried up, losing their lush color. Looking to the cactus, she saw a sparrow dip his beak into the cactus to drink some water. Though ashamed, the rose asked the cactus if she could have some water. The kind cactus readily agreed, helping them both through the tough summer, as friends'
    ]
n = 1
for i in range(n):
    speak(random.choice(list))

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[].id')

speak("I hope you liked the story")

