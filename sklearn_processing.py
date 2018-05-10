#coding=gbk
from sklearn.preprocessing import MinMaxScaler, StandardScaler
'''数据的特征处理'''
def minMax():
    '''
    数据的归一化，避免某一特征对最终结果造成很大的影响
    缺点：容易受异常点的影响
    '''
    mms = MinMaxScaler()
    data = mms.fit_transform([[90, 2, 10, 40],
                              [60, 4, 15, 45],
                              [75, 3, 13, 46]])
    print(data)
def standar():
    '''
    数据的标准化，解决异常点对结果影响很大的问题，让数据维持很好的稳定性
    '''
    stand =  StandardScaler()
    data =  stand.fit_transform([[1, -1, 3], [2, 4, 2], [4, 6, -1]])
    print(data)
def main():
    #minMax()
    standar()
if __name__ == "__main__":
    main()