import cohere
from cohere.classify import Example
co = cohere.Client('SWNcF7UPyIJhRbZYT6IQsgpySycWUQ0Wj2JnmEsH')


testtxt = "may be like my only role now would be to tear your sails with mydiscontent"
response = co.classify(
  model='66c45e0f-9156-4f63-a7a4-419d1ca6658e-ft',
  inputs=[testtxt])


max_lable=""
max_confidence = 0
for i in response.classifications[0].confidence:
    if i.confidence >= max_confidence:
        max_lable = i.label
        max_confidence = i.confidence

print(f"Therefor the Input is of Type {max_lable} with confidence {max_confidence}")
# print('The confidence levels of the labels are: {}'.format(reslt))