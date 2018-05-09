# 디비 처리 - 연결, 해제, 검색어 가져오기, 데이터 삽입
import pymysql as my
class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버 함수
    '''
    def db_init(self):
        self.conn = my.connect(
            host='localhost',
            user='root',
            password='blockchain',
            db='pythonDB',
            charset='utf8',
            cursorclass=my.cursors.DictCursor
        )
        
    def db_free(self):
        if  self.conn:
            self.conn.close()
            
    # 검색 키워드 가져오기 
    def db_selectKeyword(self):
        rows = None
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = 'SELECT *  FROM tbl_keyword;'
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        return rows
        
    def db_insertCrawlingData(self, title, price, area, contents, keyword):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into tbl_crawlingData 
            (title, price, area, contents, keyword)
            values( %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (title, price, area, contents, keyword))
        self.conn.commit()

if __name__ == '__main__':
    db = DBHelper()
    print( db.db_selectKeyword() )
    # print( db.db_insertCrawlingData('크슬헝가리 3국일 이번 주말 gogo! 발칸으로', '129만원', '2018.05.06~2018.10.28', '크로아티아','크로아티아') )
    print( db.db_insertCrawlingData('가', '나', '다', '라', '마'))
    # print( db.db_insertCrawlingData('a', 'b', 'c', 'd', 'e'))
    db.db_free()