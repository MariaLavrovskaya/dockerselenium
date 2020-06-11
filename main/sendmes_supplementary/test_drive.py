import csv
import pandas as pd


#a = [ 'https://www.instagram.com/p/B-4kf_GKMmo/', 'https://www.instagram.com/p/B-KY9v4C9Tr/', 'https://www.instagram.com/p/B-cWqCuCPyt/', 'https://www.instagram.com/p/B963UryqSuv/', 'https://www.instagram.com/p/B9R55ugqPv5/', 'https://www.instagram.com/p/B-uZqkvp9Mp/', 'https://www.instagram.com/p/B-E2ARyqbGA/', 'https://www.instagram.com/p/B9bfkXOJK1m/', 'https://www.instagram.com/p/B9joDbXpH2R/', 'https://www.instagram.com/p/B-fF2A3iDtB/',
      #'https://www.instagram.com/p/B-r_zjJKGvW/']

#df = pd.DataFrame(data={"col1": a})
#df.to_csv("./test8.csv", sep=',', index=False)


comcom = pd.DataFrame(data={"col1": not_sorted_comments1})
comcom.to_csv("./comments.csv", sep=',', index=False)