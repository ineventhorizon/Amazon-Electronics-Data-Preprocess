import pandas as pd

READ_JSON = False


def isValuable(like, dislike):
    if dislike is 0 and like is 0:
        return True
    percent = (dislike*100) / (like + dislike)
    if percent >= 80:
        return False
    else:
        return True

if READ_JSON:

    jsonFile = pd.read_json('D:\\bitirme\data\Electronics_5.json', lines=True)
    jsonFile.to_pickle("./electronics.pkl")
else:
    jsonFile = pd.read_pickle("./electronics.pkl")

print('Schema:', jsonFile.dtypes)
print('Number of questions,columns:', jsonFile.shape)

reviewText = list(jsonFile['reviewText'])
ratings = list(jsonFile['overall'])
helpfullnes = list(jsonFile['helpful'])

myData = []
positive, negative, valuable, notValuable = 0, 0, 0, 0

i = 0
for text, rating, hlp in zip(reviewText, ratings, helpfullnes):
    like, dislike = hlp[0], hlp[1]
    if isValuable(like, dislike):
        if rating >= 4.0:
            state = 'positive'
            positive += 1
        else:
            state = 'negative'
            negative += 1
        dt = '{ ' \
             f'"name":"{text}", ' \
             f'"rating":"{rating}", ' \
             f'"state":"{state}"' \
             '} \n'
        #myData.append(dt)
        with open('myData.json', 'a') as fd:
            fd.write(dt)
        i += 1
        valuable += 1
    else:
        print(f'{i}. {hlp} is not valuable')
        notValuable += 1

with open('count.csv', 'a') as f:
    fd.write(f'Positive:{positive}, Negative:{negative}, Valuable:{valuable}, Not Valuable:{notValuable}')

#ratings.to_csv('ratings')
