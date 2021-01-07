import nltk

# nltk.download()

#------------pre-processing-----------------

base = [('I am admired by many', 'joy'),
        ('I feel completely loved', 'joy'),
        ('loving and wonderful', 'joy'),
        ('I am feeling very excited again', 'joy'),
        ('I am fine today', 'joy'),
        ('what a beautiful day to drive a new car', 'joy'),
        ('the day is very beautiful', 'joy'),
        ('I am happy with the result of the test I did yesterday', 'joy'),
        ('love is beautiful', 'joy'),
        ('our friendship and love will last forever', 'joy'),
        ('I am scared', 'fear'),
        ('he is been threatening me for days', 'fear'),
        ('it terrifies me', 'fear'),
        ('this place is terrifying', 'fear'),
        ('if we lose another game we will be eliminated and that makes me terrified', 'fear'),
        ('be careful with the werewolf', 'fear'),
        ('if they find out we are in trouble', 'fear'),
        ('I am shaking with fear', 'fear'),
        ('I am very afraid of him', 'fear'),
        ('I am afraid of my test results', 'fear')]

base_training = [

('you are abominable', 'heartbreak'),
('I loathe the way you act', 'heartbreak'),
('I am sick', 'heartbreak'),
('my father is sick', 'heartbreak'),
('we are all sick', 'heartbreak'),
('this situation is very bitter', 'heartbreak'),
('said goodbye bitterly', 'heartbreak'),
('I dislike that person', 'heartbreak'),
('how can you be so unfriendly!', 'heartbreak'),
('how horrible you disgusting', 'heartbreak'),
('I have an aversion to acting like you', 'heartbreak'),
('all that and just annoyance', 'heartbreak'),
('I am very upset with your lies', 'heartbreak'),
('so unpleasant', 'heartbreak'),
('it completely dislikes me', 'heartbreak'),
('you dislike it', 'heartbreak'),
('I have terrible seasickness', 'heartbreak'),
('everyone is sick', 'heartbreak'),
('it was a terrible illness', 'heartbreak'),
('this is very serious', 'heartbreak'),
('dont be so rude', 'heartbreak'),
('you did an illegal maneuver', 'heartbreak'),
('you indecent, arent you ashamed?', 'heartbreak'),
('you are mean to children', 'heartbreak'),
('what a mean comment', 'heartbreak'),
('unscrupulous you manipulate everything', 'heartbreak'),
('I feel disgust for you', 'heartbreak'),
('and disgusting the way you look at people', 'heartbreak'),
('I am unwell', 'heartbreak'),
('the indisposition attacked me today', 'heartbreak'),
('I think Im going to be sick', 'heartbreak'),
('there is a lot of vomit there', 'heartbreak'),
('how bothering this pain', 'heartbreak'),
('dont bother me again', 'heartbreak'),
('your nonsense is bothering us', 'heartbreak'),
('what disgust looks at all this dirt', 'disgust'),
('how dirty this is', 'heartbreak'),
('I have nausea just to remember', 'heartbreak'),
('I feel sick with the smell of this food', 'heartbreak'),
('you are blocking the air passage', 'heartbreak'),
('you are terribly ill', 'heartbreak'),
('look how ugly this outfit', 'heartbreak'),
('what a deplorable attitude', 'heartbreak'),
('our like you are ugly', 'heartbreak'),
('very bad all this', 'heartbreak'),
('I am disgusted with you', 'disgust'),
('you cut my subject', 'heartbreak'),
('why so much upset?', 'heartbreak'),
('this perfume is sickening', 'heartbreak'),
('being dangerous is not good', 'heartbreak'),
('you are too dangerous for my daughters', 'heartbreak'),
('what fetid this sewer', 'heartbreak'),
('how stinky you are', 'heartbreak'),
('what a smelly dog', 'heartbreak'),
('hour that outrages', 'heartbreak'),
('and outrageous of you', 'heartbreak'),
('this unpleasant situation', 'heartbreak'),
('you just give me heartbreak', 'heartbreak'),
('I have an aversion to people like that', 'heartbreak'),
('dislike and an evil of society', 'heartbreak'),
('what an abominable creature', 'heartbreak'),
('and depressing the way you see the world', 'heartbreak'),
('I dislike your presence at the party', 'heartbreak'),
('I dislike this thing', 'heartbreak'),
('how hideous!', 'heartbreak'),
('I will golf the cafe outside', 'heartbreak'),
('time for that hateful girl!', 'heartbreak'),
('I am sick', 'heartbreak'),
('what you said was very serious', 'heartbreak'),
('dont be obscene in front of the kids', 'heartbreak'),
('dont be rude to visitors', 'heartbreak'),
('this subject disgusts me', 'heartbreak'),
('what a terribly mischievous child', 'heartbreak'),
('what a rude child', 'heartbreak'),
('I am unwilling to give you a divorce', 'heartbreak'),
('so pathetic, dont you have anything rude to say?', 'heartbreak'),
('for awkward reason, using cruel means and unable to defend the victim', 'heartbreak'),
('envy is so vile and shameful that no one dares to confess it', 'heartbreak'),
('the miserable fear of being sentimental and the most vile of all modern fears', 'heartbreak'),
('naughty cat when he misses the owner, pisses on his shoe', 'heartbreak'),
('this is a detestable and cowardly act', 'heartbreak'),
('reveal only what is destructive and hateful to the people', 'heartbreak'),
('I dont know what a rascals life is like, more like an honest and abominable man', 'heartbreak'),
('there are things we have to endure so that we dont find life unbearable', 'heartbreak'),
('the injuries of time and the injustices of man', 'heartbreak'),
('hateful and inhuman', 'heartbreak'),
('you will not post hateful, pornographic or threatening content', 'heartbreak'),
('spiteful and repressed', 'heartbreak'),
('there is no animal more degrading, stupid, cowardly, pitiful, selfish, resentful and envious than man', 'heartbreak'),
('the virulent debate between politicians', 'heartbreak'),

('please dont abandon me', 'sadness'),
('I dont want to be alone', 'sadness'),
('dont leave me alone', 'sadness'),
('I am down', 'sadness'),
('he is all down', 'sadness'),
('so sad your words', 'sadness'),
('your love is no longer mine', 'sadness'),
('I am upset', 'sadness'),
('it will bore me', 'sadness'),
('I am in great distress', 'sadness'),
('it troubles me the way you speak', 'sadness'),
('I am in agony with my intimate', 'sadness'),
('I dont want to do anything', 'sadness'),
('I feel anxious and tense', 'sadness'),
('I cant stop crying', 'sadness'),
('and a lot of pain to lose a loved one', 'sadness'),
('I am really sorry', 'sadness'),
('I think karma comes back, because now I am the one who suffers', 'sadness'),
('you didnt keep your promises', 'sadness'),
('I feel bitter', 'sadness'),
('poor thing is so sad', 'sadness'),
('its too late', 'sadness'),
('our love is over', 'sadness'),
('tonight hurts just for me', 'sadness'),
('I am no longer in your heart', 'sadness'),
('you changed with me', 'sadness'),
('when I think of you it really hurts', 'sadness'),
('as if it were nothing you see my tears', 'sadness'),
('you said cruelly that you didnt regret it', 'sadness'),
('I will never see you again', 'sadness'),
('she is depressed', 'sadness'),
('depression afflicts people', 'sadness'),
('being depressed and very bad', 'sadness'),
('I am defeated and depressed after this day', 'sadness'),
('and touching to see you that way', 'sadness'),
('and touching to see what the children of Brazil are going through', 'sadness'),
('how guilty I feel', 'sadness'),
('I am down', 'sadness'),
('anxiety has taken over me', 'sadness'),
('people dont like my way', 'sadness'),
('goodbye we had a good time together', 'sadness'),
('I miss you', 'sadness'),
('he didnt like my food', 'sadness'),
('I have no money for food', 'sadness'),
('I wish it was the last day of my life', 'sadness'),
('youre ashamed of me', 'sadness'),
('she did not accept my proposal', 'sadness'),
('it was my last penny', 'sadness'),
('I failed my year in college', 'sadness'),
('after all you only know how to undo me', 'sadness'),
('I failed in everything in this life', 'sadness'),
('I was very humiliated', 'sadness'),
('and a very sad story', 'sadness'),
('nobody believes in me', 'sadness'),
('I really dont do anything', 'sadness'),
('damn, I dont do anything right', 'sadness'),
('double suffering in my life', 'sadness'),
('I got fired this week', 'sadness'),
('children suffer even more than adults', 'sadness'),
('for me one day is bad, the next is worse', 'sadness'),
('I suddenly lost my appetite', 'sadness'),
('oh what an unhappy day', 'sadness'),
('we are sunk in beads', 'sadness'),
('not even a miracle can save us', 'sadness'),
('I only have hope', 'sadness'),
('it cant be worse', 'sadness'),
('my salary is low', 'sadness'),
('I didnt pass the entrance exam', 'sadness'),
('nobody cares about me', 'sadness'),
('nobody remembered my birthday', 'sadness'),
('I am so unlucky', 'sadness'),
('the taste of revenge and bitter', 'sadness'),
('I am a bitter woman after you left me', 'sadness'),
('I am discouraged with life', 'sadness'),
('and just a poor thing', 'sadness'),
('defeat and depression', 'sadness'),
('discriminating and inhuman', 'sadness'),
('how discouraged', 'sadness'),
('and a dishonor for the country', 'sadness'),
('worry should lead us to action, not depression', 'sadness'),
('we go into dismay and madness', 'sadness'),
('he who has never seen sadness will never recognize joy', 'sadness'),
('beware of sadness, it is addiction', 'sadness'),

('I beg you, dont kill me!', 'fear'),
('are you sure it is not dangerous?', 'fear'),
('I am not sure if it is safe', 'fear'),
('I have to run so they dont catch me', 'fear'),
('help! he wanted to steal my candy!', 'fear'),
('this guy is chasing me', 'fear'),
('I dont go there, it is a very dangerous place', 'fear'),
('this place is still scary', 'fear'),
('in the jungle there are many dangerous animals', 'fear'),
('proceed with caution', 'fear'),
('this place is too quiet, watch out!', 'fear'),
('please let me live!', 'fear'),
('I will be without an allowance if I get a low grade', 'fear'),
('it looks like eyes are watching us', 'fear'),
('I fear the judges sentence may be negative', 'fear'),
('but this mission is risky', 'fear'),
('save yourselves who can!', 'fear'),
('my plan can be discovered', 'fear'),
('it was not my fault, I swear it was not me', 'fear'),
('I have to be careful with the werewolf', 'fear'),
('if I dont find it, he will discover the truth', 'fear'),
('my god, he disappeared!', 'fear'),
('I hope they dont see me from here!', 'fear'),
('keep it a secret, if they find out we will be screwed', 'fear'),
('please release me, I am innocent', 'fear'),
('I am hearing footsteps behind me', 'fear'),
('I am going to ask for help!', 'fear'),
('watch out for curves on the road', 'fear'),
('I dont know, it looks dangerous', 'fear'),
('I am shaking with fear!', 'fear'),
('help, I am going to fall!', 'fear'),
('I dont go to the black forest, and it is very dangerous', 'fear'),
('I hear footsteps towards me', 'fear'),
('I think it is too risky', 'fear'),
('lets go back, and very dangerous', 'fear'),
('run away, if we dont end up dead', 'fear'),
('I am afraid I wont get rid of this situation', 'fear'),
('help! he is armed!', 'fear'),
('hey watch out, you are going to hit the pole!', 'fear'),
('help, we are sinking', 'fear'),
('seriously, be careful with that gun!', 'fear'),
('sharks are attacking!', 'fear'),
('I get goosebumps when I am alone in the dark', 'fear'),
('calm down, I dont have the money', 'fear'),
('I think I am being deceived', 'fear'),
('fast, we have to run quickly', 'fear'),
('there is a wild crocodile coming over here', 'fear'),
('if we keep quiet they wont find us', 'fear'),
('run away! the tiger looks hungry', 'fear'),
('I am stuck, I need a miracle', 'fear'),
('take it from me! help!', 'fear'),
('I cant swim, I will drown!', 'fear'),
('I am not sure if it is safe', 'fear'),
('I will be beaten if my parents see my newsletter', 'fear'),
('I cant get out of here!', 'fear'),
('if I leave so late, I may be mugged', 'fear'),
('please dont leave me!', 'fear'),
('wait, you cant leave me here alone', 'fear'),
('I fear for your safety', 'fear'),
('I give you the money, please dont kill me!', 'fear'),
('he will take all my money', 'fear'),
('dont drive that fast', 'fear'),
('they discovered me, they will arrest me!', 'fear'),
('I just hope they dont do me any harm', 'fear'),
('I will drown, help me out of the water', 'fear'),
('we wont be safe here', 'fear'),
('I dont even want to think about what can happen', 'fear'),
('in this city and one disgrace after another', 'fear'),
('someone is calling me, Im scared', 'fear'),
('this is no cure, dont kill me', 'fear'),
('I dont trust him, I have to be careful', 'fear'),
('very cautious', 'fear'),
('I am going to be discovered, my god', 'fear'),
('I am afraid I will have to go', 'fear'),
('the night is very dangerous', 'fear'),
('I am shaking with this house', 'fear'),
('look at that creature moving monstrously', 'fear'),
('I cant stand this suspense', 'fear'),
('scare the dogs away', 'fear'),
('I am shocked and frightened by this brutal murder', 'fear'),
('and I must chase away this fear of hell', 'fear'),
('your politicians use their strength to scare and frighten the people', 'fear'),
('the purpose of that and just scaring me more', 'fear'),
('it terrifies me', 'fear')]

base_test = [
('the world is ugly as sin', 'heartbreak'),
('the hardest thing to hide and what doesnt exist', 'heartbreak'),
('you missed that goal badly', 'heartbreak'),
('I am never going to get married, Im very ugly', 'heartbreak'),
('the blows of adversity are terribly bitter', 'heartbreak'),
('men get terribly boring', 'heartbreak'),
('abominably convinced', 'heartbreak'),
('terribly angry', 'heartbreak'),
('public institutions are terribly decadent', 'heartbreak'),
('the population lived in isolation for a long time', 'heartbreak'),
('I am terribly worried', 'heartbreak'),
('nationalism and a childhood illness', 'heartbreak'),
('if you dislike me my denial is ready', 'heartbreak'),
('many documentaries about this unsympathetic couple', 'heartbreak'),
('your beauty does not undo your dislike', 'heartbreak'),
('this is an unpleasant experience', 'heartbreak'),
('unpleasant damage to bathrooms', 'heartbreak'),
('the most irritating in love and that it is a crime that needs an accomplice', 'heartbreak'),
('the situation makes us very uncomfortable', 'heartbreak'),
('I am worried about the pain in my throat', 'heartbreak'),
('I just dont want a nuisance from the police', 'heartbreak'),
('you are a very naughty little creature', 'heartbreak'),
('the weight and pain of life', 'heartbreak'),
('I bitterly regret my actions', 'heartbreak'),
('fate is cruel and men are not worthy of compassion', 'heartbreak'),
('hatred leads to cruel isolation and despair', 'heartbreak'),
('ended with the most disgusting and disgusting massacre known', 'heartbreak'),
('tasteless and disgusting', 'disgust'),
('everything is inserted in this hideous world', 'heartbreak'),
('the crime of corruption and a heinous crime', 'heartbreak'),
('the river is fetid and dark in color', 'heartbreak'),
('too much trash in the river makes it smelly', 'heartbreak'),
('there is a rotten orange in the group and we already suspect who it is', 'heartbreak'),
('I was suddenly hurt and feeling sick', 'heartbreak'),
('I was disgusted', 'heartbreak'),
('in a few months I will leave this country because I am already sick', 'heartbreak'),

('this is all a mistake', 'sadness'),
('I am wrong, I am errant', 'sadness'),
('I am very sorry for the dog', 'sadness'),
('the loss of a child is painful', 'sadness'),
('this tragedy will shake us forever', 'sadness'),
('I lost my children', 'sadness'),
('I lost my way', 'sadness'),
('I am just a crybaby', 'sadness'),
('you are a crybaby', 'sadness'),
('if regret killed', 'sadness'),
('I feel out of place in the classroom', 'sadness'),
('it was a funeral passage', 'sadness'),
('our condolences and sadness at your loss', 'sadness'),
('discouragement, anger, loneliness or emptyness, depression', 'sadness'),
('I keep discouraging you', 'sadness'),
('I am discouraged', 'sadness'),
('bloodthirsty, depraved and fearful emperor', 'sadness'),
('my being is in agony', 'sadness'),
('this friction between us must end', 'sadness'),
('darkness desolates my being', 'sadness'),
('your false concern', 'sadness'),
('its falsehood saddens me', 'sadness'),
('those who are unhappy with others are unhappy with themselves', 'sadness'),
('the crowd is unhappy with the dismissal of the coach', 'sadness'),
('I am really upset about the newspaper', 'sadness'),
('I feel lonely and bored', 'sadness'),
('life is lonely for those who are not fake', 'sadness'),
('as with compulsion after depression', 'sadness'),
('I am discouraging myself from living', 'sadness'),
('it discourages my wishes', 'sadness'),
('this is depressing inside', 'sadness'),
('I think this is defective', 'sadness'),
('the medicines drop me on the bed', 'sadness'),
('depression will bring me down', 'sadness'),
('your excuses are false', 'sadness'),
('dont hurt people', 'sadness'),

('how abominable this monster!', 'fear'),
('lets alarm everyone about the situation', 'fear'),
('I am scared', 'fear'),
('I am really scared of the night', 'scared'),
('he is been threatening me for days', 'fear'),
('how much anguish', 'fear'),
('I am distressed', 'fear'),
('anxiously I will go out and home', 'fear'),
('it terrifies me', 'fear'),
('you are scaring me', 'fear'),
('I am suspicious of you', 'fear'),
('I dont trust you', 'fear'),
('even the dog is terrified', 'fear'),
('I am scared of my colleagues actions', 'fear'),
('now he feels humiliated, terrified', 'fear'),
('scared the population and caused deaths', 'fear'),
('I am having trouble breathing and very scared', 'fear'),
('the police were scared when the car overturned', 'fear'),
('the worker is haunted by the fear of unemployment', 'fear'),
('this place is haunted', 'fear'),
('I am haunted by the financial crisis', 'fear'),
('even terrified I remember you', 'fear'),
('terrified and sweating cold', 'fear'),
('a group of wild elephants has been terrorizing villages', 'fear'),
('I feel intimidated by your presence', 'fear'),
('I am afraid of being warned again', 'fear'),
('I am in danger of being warned', 'fear'),
('I am taking health risks', 'fear'),
('the risks are real', 'fear'),
('we can lose a lot of money with this onslaught', 'fear'),
('help, I was summoned to testify', 'fear'),
('I was notified and I am afraid of losing my daughters custody', 'fear'),
('I am distressed with my children on the street', 'fear'),
('what they do with animals is abhorrent', 'fear'),
('it was terrible the tiger almost killed him', 'fear'),
('they warned me about it', 'fear')]

stopwordsnltk = nltk.corpus.stopwords.words('english')

#print(stopwordsnltk)

def remove_stopwords(text):
                  phrases = []
                  for (words, emotion) in text:
                      semstop = [p for p in words.split() if p not in stopwordsnltk]
                      phrases.append((semstop, emotion))
                  return phrases

#print(remove_stopwords(base))

def apply_stemmer(text):
    stemmer = nltk.stem.SnowballStemmer('english')
    phrases_stemming = []
    for (words, emotion) in text:
            comstemming = [str(stemmer.stem(p)) for p in words.split()if p not in stopwordsnltk]
            phrases_stemming.append((comstemming, emotion))
    return phrases_stemming

phrases_with_stemming = apply_stemmer(base_training)
#print(phases_with_stemming)

def search_words(phrases):
    all_words = []
    for(words, emotion) in phrases:
        all_words.extend(words)
    return all_words

words = search_words(phrases_with_stemming)
#print(words)

def search_frequency(words):
    words = nltk.FreqDist(words)
    return words

frequency = search_frequency(words)
#print (frequency.most_common(50)) #qtd of time that words shows up

def search_uniq_words(frequency):
    freq = frequency.keys()
    return freq

uniq_words = search_uniq_words(frequency)
#print(uniq_words)

def extract_words(document):
    doc = set(document)
    charact = {}
    for words in uniq_words:
        charact ['%s' % words] = (words in doc)
    return charact


complete_base = nltk.classify.apply_features(extract_words, phrases_with_stemming)
#print(complete_base[15])

#------------classification-----------------

classificator = nltk.NaiveBayesClassifier.train(complete_base)
print(classificator.labels())
#print(classificator.show_most_informative_features(10))

test = 'I feel sad'
test_stemming = []
stemmer = nltk.stem.SnowballStemmer('english')
for (words) in test.split():
    with_steam = [p for p in words.split()]
    test_stemming.append(str(stemmer.stem(with_steam[0])))
#print(test_stemming)

new = extract_words(test_stemming)
#print(new)

print(classificator.classify(new))
distribuition = classificator.prob_classify(new)
for clas in distribuition.samples():
 print("%s: %f" % (clas, distribuition.prob(clas)))