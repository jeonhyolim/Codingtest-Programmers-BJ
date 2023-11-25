def solution(n, lost, reserve):
    both = set(lost) & set(reserve)
    lost = list(set(lost)-both)
    reserve = list(set(reserve)-both)
    copy_lost = lost.copy()

    # 도난당했고 자신은 여분 옷 없음 -> 다른 사람 빌리기 시도 , 빌릴 수 있는 사람 짜고 -> 최적 알아내야 함
    for i in range(len(copy_lost)):
        if lost[i]-1 in reserve: # 작은 사람 O 큰 사람 X 둘 다 있음 -> 누구한테 빌릴지 보
            reserve.remove(lost[i]-1)
            copy_lost.remove(lost[i])
        elif lost[i]+1 in reserve: # 큰 사람 있는지 확인
            reserve.remove(lost[i]+1)
            copy_lost.remove(lost[i])
    return n-len(copy_lost)