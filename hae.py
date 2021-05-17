import naverPapago
import komoranSpacing
import hgtkTest
import engInputAnalysis
import hgtk

def hae(first_res):
    temp=[]
    for i in range(len(first_res[1])):
       if first_res[1][i][1] == 'EF' and first_res[1][i][0] == '다':
           first_res[0][i] = '어'
           first_res[1][i][0] = '어'
       if first_res[1][i][1] == 'EF' and first_res[1][i][0] == '어요':
           first_res[0][i] = '어'
           first_res[1][i][0] = '어'
    return first_res    