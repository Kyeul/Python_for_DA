#File name : my_area.py

PI = 3.14

def quadrangle_area(height, width):
        return height * width
    
def circle_area(r):
    return (r**2)*PI

if __name__ == '__main__':
    print('모듈 테스트 코드일 때만 실행')
    print('사각형: ', quadrangle_area(2,3))
    print('원: ', circle_area(3))

else:
    print("모듈이 정상적으로 임포트되었습니다.")
