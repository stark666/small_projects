#coding=gbk
import re
import requests
from docopt import docopt
from prettytable import PrettyTable

if __name__ == "__main__":
        argu = docopt(__doc__)

        station_code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
        #去除https访问的警告信息
        requests.packages.urllib3.disable_warnings()
        r = requests.get(station_code_url, verify=False)
        station_code_html = r.text
        #过滤中文字符
        station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
        station_code_dict = dict(station_code)
        #获取站点的代码
        source = station_code_dict.get(argu['<from>'].decode("utf-8"))
        des = station_code_dict.get(argu['<to>'].decode("utf-8"))
        date = argu['<date>']

        query_url = "https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date, source, des)
        table = PrettyTable(["车次", "出发站", "到达站", "出发时间", "到达时间", "历时", "商务座", "特等座", "一等座", "二等座", "高级软卧", "软卧", "硬卧", "软座", "硬座", "无座", "其他"])
        r2 = requests.get(query_url, verify=False)
        for info in r2.json()["data"]:
                detail = info["queryLeftNewDTO"]
                table.add_row([detail["station_train_code"], detail["start_station_name"], detail["to_station_name"], detail["start_time"], detail["arrive_time"], detail["lishi"], detail["swz_num"], detail["tz_num"], detail["zy_num"], detail["ze_num"], detail["gr_num"], detail["rw_num"], detail["yw_num"], detail["rz_num"], detail["yz_num"], detail["wz_num"], detail["qt_num"]])
        #打印车次信息
        print table