import cohere
from cohere.classify import Example





def identify(testtxt):
    # testtxt = "life is like riding a bicycle to keep your balance you must keep moving albert einstein"
    co = cohere.Client('SWNcF7UPyIJhRbZYT6IQsgpySycWUQ0Wj2JnmEsH')
    response = co.classify(
    model='66c45e0f-9156-4f63-a7a4-419d1ca6658e-ft',
    inputs=[testtxt])
    max_lable=""
    max_confidence = 0
    for i in response.classifications[0].confidence:
        if i.confidence >= max_confidence:
            max_lable = i.label
            max_confidence = i.confidence
    return max_lable,max_confidence

# print(f"Therefor the Input is of Type {max_lable} with confidence {max_confidence}")
# print('The confidence levels of the labels are: {}'.format(reslt))