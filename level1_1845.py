nums = [3,1,2,3,2,3,1,4]
# len(nums)/2 -> 가져갈 포켓몬 수

def solution(nums):
    max_ = len(nums)/2
    if len(set(nums)) < max_:
        return len(set(nums))
    else:
        return int(max_)

print(solution(nums))