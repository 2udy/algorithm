import sys
sys.stdin = open('input.txt')

'''
좌 우 모두 2칸 이상 확보될 때 조망권 확보
'''

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        # 좌우 건물들의 높이를 저장하는 리스트 생성
        near_by_buildings = [buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]]
        # 좌우 건물들의 높이중 최대값이 현재 빌딩의 높이보다 낮을 때
        if max(near_by_buildings) < buildings[i]:
            # 가장 높은 건물과 현재 건물의 높이 차만큼 조망권 확보 가능
            ans += buildings[i] - max(near_by_buildings)

    print(f'#{tc} {ans}')