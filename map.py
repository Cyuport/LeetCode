from pyecharts.charts import Map
from pyecharts import options as opts
#将数据处理成列表
country = ["United States", "United Kingdom", "India", "Australia", "Egypt", "Italy", "South Korea", "France", "Myanmar", "Germany"]
number = [16,2,1,6,1,4,1,1,1,1]
list1 = [[country[i],number[i]] for i in range(len(country))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="发起赔偿的国家热度分布"),
    visualmap_opts=opts.VisualMapOpts(max_=16)  #最大数据范围
    )
map_1.add("发起者数量", list1, maptype="world")
map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

map_1.render('map1.html')