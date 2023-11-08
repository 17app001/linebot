from tools import get_soup

# 爬找發票
def get_invoice_numbers():
    numbers=[]
    try:
        url='https://invoice.etax.nat.gov.tw/'
        soup=get_soup(url)
        trs=soup.find('table',class_="etw-table-bgbox etw-tbig").find_all('tr')
        datas=[[td.text.strip() for td in tr.find_all('td')]for tr in trs[1:4]]       
        for data in datas:         
            numbers+=data[1].split()[:-1]        
    except Exception as e:
        print(e)

    return numbers

# 進行兌獎
def search_invoice_bingo(invoice_number,numbers):
    bingo=False
    for i in range(len(numbers)):               
        if numbers[i][5:] == invoice_number[len(invoice_number)-3:]:
            bingo=True
            break     

    if bingo:
        if i==0:
            message='有機會中特別獎1000萬(八個號碼)'            
        elif i==1:
            message='有機會中特獎200萬(八個號碼)'          
        else:
            message='有機會中頭獎20萬(三個號碼已中200元)'
        
        message+=f'\n請繼續對其他號碼==>{numbers[i]}'
    else:
        message='@@沒有中獎～～'       

    return message

if __name__=='__main__':
    numbers=get_invoice_numbers()
    print(numbers)
    print(search_invoice_bingo('09505731',numbers))