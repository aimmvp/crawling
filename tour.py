# 상품정보 담는 클래스
class TourInfo:
    #@ 멤버변수
    title = ''
    price = ''
    area  = ''
    link  = ''
    img = ''
    # 생성자
    def __init__(self, title, price, area, link, img):
        self.title = title
        self.prices = price
        self.area = area
        self.link = link
        self.img = img
