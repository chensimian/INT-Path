import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def font_setting(title,x_label,y_label,y1_label):
    font_title = {'family' : 'Times New Roman','weight' : 'normal','size' : title}
    font_ylabel = {'family' : 'Times New Roman','weight' : 'normal','size' : x_label}
    font_y1label = {'family': 'Times New Roman', 'weight': 'normal', 'size': x_label}
    font_xlabel = {'family' : 'Times New Roman','weight' : 'normal','size' : y_label}

    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False
    return font_title,font_xlabel,font_ylabel,font_y1label
i = 13  #字体大小
font_title,font_xlabel,font_ylabel,font_y1label= font_setting(i,i,i,i)

def line_chart(lab_num,title,x_label,y_label,y1_label,index_col,font_title,font_xlabel,font_ylabel,font_y1label):
    try:
        excelFile = './b{}.xlsx'.format(lab_num)
        data = pd.read_excel(excelFile,dtype = {index_col:str})
    except:
        excelFile = './b{}.xls'.format(lab_num)
        data = pd.read_excel(excelFile,dtype = {index_col:str})
    data.set_index(index_col,inplace = False)
    data = pd.DataFrame(data)
    #
    plt.grid(linestyle='-.', axis='x')  # 显示对标y轴的线
    plt.grid(linestyle='-.', axis='y')  # 显示对标y轴的线
    fig=plt.figure(figsize=(8, 4))  #调图片大小的
    ax = fig.add_subplot(111)

    plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号
    plt.rcParams['font.sans-serif'] = ['Times New Roman']

    time = np.arange(125)
    #plt.plot(data['value'][239:], label="value", c="b", marker=".", markersize=7, markerfacecolor='none')
    lns1=plt.plot(time,data['Execution Time'], label="Execution Time", c="b", marker="o", markersize=7, markerfacecolor='none')
    ax2 = ax.twinx()
    #ax1 = plt.twinx()  #镜像
    lns2=plt.plot(time,data['Hierholzer Call Times'],label= "Hierholzer Call Times",c = "r",marker = "^",markersize=7,markerfacecolor='none')

    #合并
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)

    #显示
    ax.grid()
    ax.set_xlabel(x_label,font = font_xlabel)
    ax.set_ylabel(y_label, font = font_ylabel)
    ax2.set_ylabel(y1_label,font=font_y1label)
    ax2.set_ylim(0, 100)
    ax.set_ylim(0, 1.7)
    plt.savefig('./Output/lab7.png'.format(lab_num), dpi=1000, bbox_inches='tight')
    plt.show()

    # plt.title(title,font = font_title) # title with fontsize 20
    # plt.xlabel(x_label,font = font_xlabel) # x-axis label with fontsize 15
    # plt.ylabel(y_label, font = font_ylabel)
    # plt.legend()
    # #plt.savefig('./Output/lab7.png'.format(lab_num),dpi=1000, bbox_inches='tight')
    #
    # plt.show()
#         lab_num,title,x_label,y_label,index_col,font_title,font_xlabel,font_ylabel)   第一个参数是选择excel表的参数
line_chart(7,"","Odd Vertex Number","Execution Time(s)","Call Times of Hierholzer's","index",font_title,font_xlabel,font_ylabel,font_y1label)
