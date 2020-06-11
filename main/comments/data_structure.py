import re


class InstagramCleaning():
    def __init__(self, rawdata):
        self.rawdata = rawdata
        # self.first = self.preprocessing(rawdata)
        self.rest = self.excluding_user(self.rawdata)
        self.dates = self.filter_dates(self.rest)
        self.likes = self.filter_likes(self.rest)
        self.username = self.username(rawdata)
        self.comment = self.comment_text(self.rest)
        self.building_dict()

    def building_dict(self):
        all_data = list(zip(self.username, self.comment_text, self.dates, self.likes))
        print(self.username, self.comment_text, self.dates, self.likes)
        self.dicts = {i: {'Username': all_data[i][0], 'Comment': all_data[i][1], 'Dates back': all_data[i][2],
                          'Likes': all_data[i][3]} for i in range(len(all_data)
                                                                  )}
        return self.dicts

    # Splitting the comment and removing the word "ответить"
    # def preprocessing(self, rawdata):
    # notSorted = [comment.text.split('Ответить') for comment in rawdata]
    # allin = [word for comment in rawdata for word in comment.text.split('Ответить')]
    # return allin

    # Removing the user from the list (so we can work with the data in the comment)
    def excluding_user(self, allin):
        rest = [rest for comment in allin for _, rest in [comment.split('\n', 1)]]
        return rest

    # Getting dates out of the whole comment string
    def filter_dates(self, rest):
        self.dates = []
        for date_back in self.rest:
            # for those posts that do not have any likes
            if bool(re.search(r"[0-9]+[a-zA-Z]", date_back.rsplit('\n', 1)[1])) is True:
                my_findings = re.search(r"[0-9]+[a-zA-Z]", date_back.rsplit('\n', 1)[1])
                self.dates.append(my_findings.group().split('Reply', 1)[0])
        return self.dates

    # оставшиеся
    # Getting likes out of the whole comment string
    def filter_likes(self, rest):
        self.likes = [like.split()[-2][-1] if like.split()[-1] in ("likesReply", 'likeReply') else 'None' for like in
                      rest]
        return self.likes

    # Getting the username from the whole string

    def username(self, allin):
        self.username = [user for comment in allin for user, _ in [comment.split('\n', 1)]]
        return self.username

    # оставшиеся
    # Getting the text of the comment out
    def comment_text(self, rest):
        self.comment_text = [comment.rsplit('\n', 1)[0] for comment in rest]
        return self.comment_text

# if __name__ == '__main__':
# InstagramCleaning = InstagramCleaning()
# InstagramCleaning.building_dict()