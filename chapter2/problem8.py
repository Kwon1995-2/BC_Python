"""판매자가 딸기와 포도를 판매하고 있다. 
포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다. 
사용자로부터 포도 알의 개수와 딸기의 개수를 입력받아 
총 무게를 계산하여 출력하는 프로그램 작성 """

m_nGrapeNum = int(input("Grape : "))
m_nStrawberryNum = int(input("Strawberry : "))
m_nTotalWght = m_nGrapeNum*75 + m_nStrawberryNum*113.5 
print(m_nTotalWght)