def solution(common):
    if common[1]*common[1] == common[0]*common[2]: # 등비수열
        if common[len(common)-2] == 0:
            return 0
        else:
            return common[len(common)-1]*common[len(common)-1]//common[len(common)-2]
    else: # 등차수열
        return common[len(common)-1]*2-common[len(common)-2]