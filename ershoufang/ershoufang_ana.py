import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Map
from pyecharts import options as opts

# 导入数据
info1 = pd.read_csv('info1.csv')
info2 = pd.read_csv('info2.csv')
info3 = pd.read_csv('info3.csv')
info4 = pd.read_csv('info4.csv')
info5 = pd.read_csv('info5.csv')
info6 = pd.read_csv('info6.csv')
info7 = pd.read_csv('info7.csv')
info8 = pd.read_csv('info8.csv')
info9 = pd.read_csv('info9.csv')
# 合并成一个
info0 = [info1,info2,info3,info4,info5,info6,info7,info8,info9]
infos = pd.concat(info0)

name = ['name','address','area','tag','price']
info_csv = pd.DataFrame(columns=name,data=infos)
info_csv.to_csv('infos.csv',encoding='utf-8')

# 查看其信息
print(infos)
print(infos.info())

# 数据分析
infos1 = infos['price'].groupby(infos['address'])
# 二手房数量
size = infos1.size()
# 二手房价格平均值
mean = infos1.mean()
# 房价最高
max_price = infos1.max()
# 房价最低
min_price = infos1.min()
# 房价的方差
var = infos1.var()

print(size)
print(mean)
print(var)
print(max_price)
print(min_price)

def draw(obj,obj_name,html):
    '''画出条形图'''
    bar = Bar()
    name = ['中原','二七','惠济','新郑','管城','经开','航空','郑东',
            '金水','高新']
    bar.add_xaxis(['中原','二七','惠济','新郑','管城','经开','航空港',
                   '郑东新区','金水','高新'])
    bar.add_yaxis(obj_name, [int(obj[name[0]]),int(obj[name[1]]),int(obj[name[2]]),
                          int(obj[name[3]]),int(obj[name[4]]),int(obj[name[5]]),
                          int(obj[name[6]]),int(obj[name[7]]),int(obj[name[8]]),
                          int(obj[name[9]])])
    bar.set_global_opts(title_opts=opts.TitleOpts(title = ''))
    bar.render(html)

draw(size,'各区二手房数量','size.html')
draw(mean,'各区房价均值','mean.html')
draw(max_price,'各区房价最高值','max.html')
draw(min_price,'各区房价最低值','min.html')
draw(var,'各区房价方差','var.html')
def create_city_map(obj,obj_name):
    '''生成地图'''
    name_r = ['中原区','二七区','惠济区','新郑市','管城回族区','经开区','航空港区',
              '中牟县','金水区','高新区']
    name = ['中原','二七','惠济','新郑','管城','经开','航空','郑东',
            '金水','高新']
    detail = [[name_r[0],int(obj[name[0]])],[name_r[1],int(obj[name[1]])],
                [name_r[2],int(obj[name[2]])],[name_r[3],int(obj[name[3]])],
                [name_r[4],int(obj[name[4]])],[name_r[5],int(obj[name[5]])],
                [name_r[6],int(obj[name[6]])],[name_r[7],int(obj[name[7]])],
                [name_r[8],int(obj[name[8]])],[name_r[9],int(obj[name[9]])]]
    max_v = max(int(obj[name[0]]),int(obj[name[1]]),int(obj[name[2]]),
                int(obj[name[3]]),int(obj[name[4]]),int(obj[name[5]]),
                int(obj[name[6]]),int(obj[name[7]]),int(obj[name[8]]),
                int(obj[name[9]]))
    (   # 大小设置
        Map()
        .add(series_name=obj_name, data_pair=detail, maptype="郑州", )
        # 全局配置项
        .set_global_opts(
            title_opts=opts.TitleOpts(title=''),  # 标题
            visualmap_opts=opts.VisualMapOpts(max_=max_v, is_piecewise=False))  # 标准显示
        # 标签名称显示，默认为True
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="blue"))
        # 生成本地html文件
        .render(obj_name + '.html'))
create_city_map(size,'二手房数量')
create_city_map(mean,'二手房价格均值')
create_city_map(var,'二手房价格方差')
