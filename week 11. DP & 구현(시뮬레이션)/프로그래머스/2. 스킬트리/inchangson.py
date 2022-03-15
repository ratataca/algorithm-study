def solution(skill, skill_trees):
    answer = 0
    fails = 0
    
    for skill_tree in skill_trees:
        memo = [s for s in skill_tree if s in skill]
        tmp = ''.join(memo)
        if tmp == skill[:len(tmp)]:
            answer += 1
    #     for idx in range(len(memo)):
    #         if skill[idx] != memo[idx]:
    #             fails += 1
    #             break
    # answer = len(skill_trees) - fails
#     for skill_tree in skill_trees:
#         tmp = ''
#         for s in skill_tree:
#             if s in skill:
#                 tmp += s
#         if tmp == skill[:len(tmp)]:
#             answer += 1
    return answer