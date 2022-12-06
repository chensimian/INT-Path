import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator


def font_setting(title,x_label,y_label):
    font_title = {'family' : 'Times New Roman','weight' : 'normal','size' : title}
    font_ylabel = {'family' : 'Times New Roman','weight' : 'normal','size' : x_label}
    font_xlabel = {'family' : 'Times New Roman','weight' : 'normal','size' : y_label}

    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False
    return font_title,font_xlabel,font_ylabel
i = 13  #字体大小
font_title,font_xlabel,font_ylabel = font_setting(i,i,i)

def line_chart(lab_num,title,x_label,y_label,index_col,font_title,font_xlabel,font_ylabel):
    try:
        excelFile = './b{}.xlsx'.format(lab_num)
        data = pd.read_excel(excelFile,dtype = {index_col:str})
    except:
        excelFile = './b{}.xls'.format(lab_num)
        data = pd.read_excel(excelFile,dtype = {index_col:str})
    data.set_index(index_col,inplace = False)
    data = pd.DataFrame(data)
    plt.figure(figsize=(8, 4))  #调图片大小的
    plt.grid(linestyle='-.',axis='x')  #显示对标x轴的线
    plt.grid(linestyle='-.', axis='y')  # 显示对标y轴的线
    plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号
    plt.rcParams['font.sans-serif'] = ['Times New Roman']

   #40行数据开始
    plt.plot(data['DFS-10-Odds'],label= "DFS-10-Odds",c = "r",marker = "^",markersize=7,markerfacecolor='none')
    plt.plot(data['Euler-10-Odd'],label= "Euler-10-Odd",c = "b",marker = "o",markersize=7,markerfacecolor='none')
    plt.plot(data['DFS-20-Odd'], label="DFS-20-Odd", c="darkviolet", marker="x", markersize=7, markerfacecolor='none')
    plt.plot(data['Euler-20-Odd'], label="Euler-20-Odd", c="g", marker="*", markersize=7, markerfacecolor='none')
    #设置间隔
    #x_major_locator = MultipleLocator(20)
    #ax = plt.gca()
    #ax.xaxis.set_major_locator(x_major_locator)

    plt.title(title,font = font_title) # title with fontsize 20
    plt.xlabel(x_label,font = font_xlabel) # x-axis label with fontsize 15
    plt.ylabel(y_label, font = font_ylabel)
    plt.legend()
    plt.savefig('./Output/lab6.png'.format(lab_num),dpi=1000, bbox_inches='tight')

    plt.show()
#         lab_num,title,x_label,y_label,index_col,font_title,font_xlabel,font_ylabel)   第一个参数是选择excel表的参数
line_chart(6,"","Switch Number","Execution Time (s)","index",font_title,font_xlabel,font_ylabel)