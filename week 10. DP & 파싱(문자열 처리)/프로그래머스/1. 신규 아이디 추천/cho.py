import re


def solution(new_id):
    answer = ""
    answer1 = new_id.lower()
    for letter in answer1:
        if letter.isalnum() or letter in "-_.":
            answer += letter

    answer = re.sub("\.\.+", ".", answer)
    answer = re.sub("^\.", "", answer)
    answer = re.sub("\.$", "", answer)
    if answer == "":
        answer = "a"
    if len(answer) > 15:
        answer = answer[:15]
        answer = re.sub("\.$", "", answer)
    if len(answer) < 4:
        for i in range(3 - len(answer)):
            answer += answer[-1]

    return answer
