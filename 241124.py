import framebuf

def draw_image_ultra_fast(path):
    try:
        with open(path, 'rb') as f:
            print("초고속 출력 중...")
            # LCD 통신을 위한 준비 (가장 빠른 하위 레벨 접근)
            for y in range(220):
                # 한 줄(352바이트)을 가져옴
                row_data = f.read(352)
                if not row_data:
                    break
                
                # 1. LCD에게 "지금부터 (0,y)부터 (175,y)까지 한 줄을 채울게"라고 알려줌
                lcd._set_window(0, y, 175, y)
                
                # 2. 데이터를 쪼개지 않고 통째로 전송 (이게 핵심!)
                # 라이브러리에 따라 이름이 다를 수 있으니 아래 둘 중 하나를 시도
                try:
                    lcd._write_data(row_data)
                except:
                    # _write_data가 안 되면 SPI로 직접 쏨
                    lcd.cs.value(0) # CS 활성화
                    lcd.rs.value(1) # Data 모드
                    spi_lcd.write(row_data) # SPI 통째로 전송
                    lcd.cs.value(1) # CS 비활성화
            
            print("번개처럼 출력 완료!")
    except Exception as e:
        print("에러 발생:", e)

# 실행
lcd.clear(0x0000)
draw_image_ultra_fast('/sd/image.bin')
