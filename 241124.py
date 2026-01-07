def draw_image_fast(path):
    try:
        with open(path, 'rb') as f:
            print("고속 출력 시작...")
            for y in range(220):
                # 한 줄 데이터(352바이트)를 통째로 읽어옴
                row_data = f.read(352)
                if not row_data:
                    break
                
                # LCD의 특정 영역(한 줄)을 지정하고 데이터를 한꺼번에 전송
                # 라이브러리마다 이름이 다를 수 있으니 아래 3가지 중 하나를 시도합니다.
                try:
                    # 방법 A: 최적화된 블록 전송 (가장 빠름)
                    lcd.set_window(0, y, 175, y) 
                    lcd._write_data(row_data)
                except AttributeError:
                    # 방법 B: 방법 A가 안될 경우 한 줄씩 그리기
                    for x in range(176):
                        color = (row_data[x*2] << 8) | row_data[x*2 + 1]
                        lcd.fill_rect(x, y, 1, 1, color)
            print("출력 완료!")
    except Exception as e:
        print("에러 발생:", e)

# 실행
lcd.clear(0x0000)
draw_image_fast('/sd/image.bin')
