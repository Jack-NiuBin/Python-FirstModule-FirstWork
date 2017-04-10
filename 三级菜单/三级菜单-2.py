#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Jack Niu
###############################
#           三级菜单           #
# 正常输入;                    #
# 输入 B 返回，输入 Q 退出;      #
#                             #
###############################

#定义三级字典的名字和内容:
location = {
    "亚洲": {
        "中国": {
            "北京": ["朝阳区", "海淀区", "昌平区", "门头沟", "东城区"],
            "天津": ["南开区", "和平区", "河东区", "河西区", "北辰区"],
            "上海": ["浦东区", "闵行区", "普陀区", "金山区", "虹口区"]
        },
        "日本": {
            "本州": ["东京", "大阪", "神户", "名古屋", "横滨"],
            "九州": ["大分县", "宫崎县", "福冈县", "佐贺县", "长崎县"],
            "北海道": ["夕张市", "赤平市", "三笠市"],
            "四国": ["德岛县", "香川县", "爱媛县", "高知县"],

        },
        "越南": {
            "河内": ["巴亭广场", "历史博物馆", "还剑湖", "独柱寺"],
            "胡志明市": ["新平", "平新", "富润", "守德"],
        }
    },
    "北美洲": {
        "美国": {
            "加利福尼亚州": ["洛杉矶", "旧金山", "拉斯维加斯"],
            "华盛顿州": ["西雅图", "雷德蒙德", "温哥华"],
            "俄亥俄州": ["帕马", "门托", "辛辛那提"]
        },
        "加拿大": {
            "安大略省": ["多伦多", "渥太华"],
            "魁北克省": ["魁北克城", "圣安妮大教堂"],
            "爱德华王子岛": ["夏洛特敦","苏默尔塞德"]
        },
    },
    "欧洲": {
        "英国": {
            "英格兰": ["", "", "", ""],
            "苏格兰": ["爱丁堡", "东艾尔郡", "南艾尔郡", "东邓巴顿郡"],
            "北爱尔兰": ["卡斯尔雷", "北唐", "利斯本", "安特里姆"],
            "威尔士": ["康威", "登比郡", "弗林特郡", "锡尔迪金"]
        },
        "意大利": {
            "阿布鲁佐": ["阿布鲁佐国家公园和自然保护区", "拉奎拉古迹区及长方形主教教堂", "拉奎拉"],
            "巴西利卡塔": ["皮埃特拉佩托萨", "波坦察", "梅尔菲"],
            "卡拉布里亚": ["值得爱的地中海", "伟大的希腊和罗马遗迹", "西巴利考古区"],
            "坎帕尼亚": ["卡普里", "伊斯基亚", "贝内文托"],
        },
    }
}

#设置退出标志位，默认为 False:
exit_flag = False

#设置列表:
locationlist = sorted(location.keys())

#一级循环并打印:
while not exit_flag:
    for index, first in enumerate(locationlist):
        print(index, first)
    first_input = input("请输入你要选择的地址索引：").strip()
    if first_input.isdigit():
        first_input = int(first_input)
        if first_input >= 0 and first_input <= len(locationlist):
            L1 = locationlist[first_input]
            countylist = sorted(location[L1].keys())

#二级循环并打印:
            while not exit_flag:
                for index, second in enumerate(sorted(countylist)):
                    print(index, second)
                second_input = input("请输入你要选择的地址索引：".strip())
                if second_input.isdigit():
                    second_input = int(second_input)
                    if second_input >= 0 and second_input <= len(countylist):
                        L2 = countylist[second_input]
                        citylist = sorted(location[L1][L2].keys())

#三级循环并打印:
                        while not exit_flag:
                            for index, third in enumerate(sorted(citylist)):
                                print(index, third)
                            third_input = input("请输入你要选择的地址索引：").strip()
                            if third_input.isdigit():
                                third_input = int(third_input)
                                if third_input >= 0 and third_input <= len(citylist):
                                    L3 = citylist[third_input]
                                    town = location[L1][L2][L3]

#打印三级循环的内容:
                                    while not exit_flag:
                                        for index , fourth in enumerate(town):
                                            print(index, fourth)
                                        fourth_input = input("请输入b返回或者输入q退出：".strip())

#判断和退出:
                                        if fourth_input == "b":
                                            break
                                        elif fourth_input == "q":
                                            exit_flag = True
                                        else:
                                            continue

#判断和退出:
                            elif third_input == "b":
                                break
                            elif third_input == "q":
                                exit_flag = True
                            else:
                                continue

#判断和退出:
                elif second_input == "b":
                    break
                elif second_input == "q":
                    exit_flag = True
                else:
                    continue

#判断和退出:
    elif first_input == "q":
        exit_flag = True
    else:
        continue