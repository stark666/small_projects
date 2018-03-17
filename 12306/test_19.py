#coding=gbk
import re
import requests
from docopt import docopt
from prettytable import PrettyTable

if __name__ == "__main__":
        argu = docopt(__doc__)

        station_code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
        #ȥ��https���ʵľ�����Ϣ
        requests.packages.urllib3.disable_warnings()
        r = requests.get(station_code_url, verify=False)
        station_code_html = r.text
        #���������ַ�
        station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
        station_code_dict = dict(station_code)
        #��ȡվ��Ĵ���
        source = station_code_dict.get(argu['<from>'].decode("utf-8"))
        des = station_code_dict.get(argu['<to>'].decode("utf-8"))
        date = argu['<date>']

        query_url = "https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date, source, des)
        table = PrettyTable(["����", "����վ", "����վ", "����ʱ��", "����ʱ��", "��ʱ", "������", "�ص���", "һ����", "������", "�߼�����", "����", "Ӳ��", "����", "Ӳ��", "����", "����"])
        r2 = requests.get(query_url, verify=False)
        for info in r2.json()["data"]:
                detail = info["queryLeftNewDTO"]
                table.add_row([detail["station_train_code"], detail["start_station_name"], detail["to_station_name"], detail["start_time"], detail["arrive_time"], detail["lishi"], detail["swz_num"], detail["tz_num"], detail["zy_num"], detail["ze_num"], detail["gr_num"], detail["rw_num"], detail["yw_num"], detail["rz_num"], detail["yz_num"], detail["wz_num"], detail["qt_num"]])
        #��ӡ������Ϣ
        print table