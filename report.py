from settings import smtp_enable, smtp_server, smtp_port, smtp_user, smtp_pass, receiver_email
from settings import ACS_CSV, MNG_CSV
from settings import logging
from inner_smtp import Notificator
from analysis import Analysis
from time import time

class Report(object):
    """
    Class constructor accepts list of CSV files to be processed
    """
    def __init__(self, list_of_csv):
        super().__init__()
        self.list_of_csv = list_of_csv    
    
    def acs_stats_single(self):
        try:
            if isinstance(self.list_of_csv, list):
                logging.info(f'{__class__.__name__ } [Processing CSVs: \n [{self.list_of_csv}]')
                for single_csv in self.list_of_csv:                    
                    server = str(single_csv).replace('.csv','')                    
                    javathreads = ['javathreads','timestampt']
                    javat = Analysis(single_csv, javathreads, f'{server.upper()} Java threads', f'{server}_javathreads.png','threads')
                    javat.single_kpi_vs_time()

                    db_c = ['oracle_1521', 'timestampt']
                    db_conn = Analysis(single_csv, db_c, f'{server.upper()} DB connections', f'{server}_db_connections.png','estb. connecitons')
                    db_conn.single_kpi_vs_time()

                    acs_port1 = ['acs_port_8080', 'timestampt']
                    acs_8080 = Analysis(single_csv, acs_port1, f'{server.upper()} Connections on port 8080', f'{server}_port_8080.png', '8080')
                    acs_8080.single_kpi_vs_time()

                    acs_port2 = ['acs_port_80', 'timestampt']
                    acs_80 = Analysis(single_csv, acs_port2, f'{server.upper()} Connections on port 80', f'{server}_port_80.png', '80')
                    acs_80.single_kpi_vs_time()

                    acs_port3 = ['acs_port_8181', 'timestampt']
                    acs_8181 = Analysis(single_csv, acs_port3, f'{server.upper()} Connections on port 8181', f'{server}_port_8181.png', '8181')
                    acs_8181.single_kpi_vs_time()

                    acs_port4 = ['acs_port_8443', 'timestampt']
                    acs_8181 = Analysis(single_csv, acs_port4, f'{server.upper()} Connections on port 8443', f'{server}_port_8443.png', '8443')
                    acs_8181.single_kpi_vs_time()

                    acs_port4 = ['acs_port_443', 'timestampt']
                    acs_8181 = Analysis(single_csv, acs_port4, f'{server.upper()} Connections on port 443', f'{server}_port_443.png', '443')
                    acs_8181.single_kpi_vs_time()

                    cpu = ['cpu_load', 'timestampt']
                    cpu_load = Analysis(single_csv, cpu, f'{server.upper()} CPU load', f'{server}_cpu_load.png', '%')
                    cpu_load.single_kpi_vs_time()

                    txt = ["javathreads","oracle_1521","acs_port_8080","acs_port_8181","acs_port_8443","acs_port_80","acs_port_443","acs_port_8182","cpu_load","used_ram"]
                    text = Analysis(single_csv, txt)
                    text.text_stats()

            else:
                logging.error(f'{__class__.__name__ } [{self.list_of_csv} is not type of list!')
                
            
        except Exception as e:            
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)

    def acs_stats_multi(self):
        try:
            if isinstance(self.list_of_csv, list):
                logging.info(f'{__class__.__name__ } [Processing CSVs: \n [{self.list_of_csv}]')
                
                for single_csv in self.list_of_csv:
                    
                    logging.info(f'{__class__.__name__ } [Start - Processing report - {single_csv}]')
                    server = str(single_csv).replace('.csv','')

                    acs_sockets1 = ['acs_port_8080', 'acs_port_80', 'timestampt']
                    acss1 = Analysis(single_csv, acs_sockets1, f'{server.upper()} port 80 vs 8080', f'{server}_8080_vs_80.png')
                    acss1.multi_kpi_vs_time('8080','80')

                    acs_sockets2 = ['acs_port_8181', 'acs_port_8182', 'timestampt']
                    acss2 = Analysis(single_csv, acs_sockets2, f'{server.upper()} port 8181 vs 8182', f'{server}_8181_vs_8182.png')
                    acss2.multi_kpi_vs_time('8181','8182')

                    acs_sockets3 = ['acs_port_443', 'acs_port_8443', 'timestampt']
                    acss2 = Analysis(single_csv, acs_sockets3, f'{server.upper()} port 443 vs 8443', f'{server}_443_vs_8443.png')
                    acss2.multi_kpi_vs_time('443','8443')

                    ram = ['total_ram','used_ram','timestampt']
                    used_ram = Analysis(single_csv, ram, f'{server.upper()} Used RAM', f'{server}_used_ram.png')
                    used_ram.multi_kpi_vs_time('total','used')

                    logging.info(f'{__class__.__name__ } [Finish - Processing report - {single_csv}]')

            else:
                logging.error(f'{__class__.__name__ } [{self.list_of_csv} is not type of list!')                

        except Exception as e:            
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)

    def mng_stats(self):
        try:            
            if isinstance(self.list_of_csv, list):
                logging.info(f'{__class__.__name__ } [Processing CSVs: \n [{self.list_of_csv}]')
                for single_csv in self.list_of_csv:
                    
                    logging.info(f'{__class__.__name__ } [Start - Processing report - {single_csv}]')
                    server = str(single_csv).replace('.csv','')

                    acs_port1 = ['acs_8080', 'timestampt']
                    acs_8080 = Analysis(single_csv, acs_port1, f'{server.upper()} Connections on port 8080', f'{server}_port_8080.png', '8080', 10)
                    acs_8080.single_kpi_vs_time()

                    acs_port2 = ['acs_8181', 'timestampt']
                    acs_8181 = Analysis(single_csv, acs_port2, f'{server.upper()} Connections on port 8181', f'{server}_port_8181.png', '8181', 10)
                    acs_8181.single_kpi_vs_time()

                    db_c = ['oracle', 'timestampt']
                    db = Analysis(single_csv, db_c, f'{server.upper()} DB connections', f'{server}_db_connections.png','estb. connecitons', 10)
                    db.single_kpi_vs_time()

                    iisr = ['iis_ram','timestampt']
                    iisram = Analysis(single_csv,iisr, f'{server.upper()} RAM usage by IIS',f'{server}_iis_ram.png','GB', 10)
                    iisram.single_kpi_vs_time()

                    iisc = ['iis_cpu','timestampt']
                    iiscpu = Analysis(single_csv,iisr, f'{server.upper()} CPU usage by IIS',f'{server}_iis_cpu.png','%', 10)
                    iiscpu.single_kpi_vs_time()

                    txt = ["used_ram","cpu_loadavg","acs_8080","acs_8181","acs_8443","oracle","iis_ram","iis_cpu"]
                    text = Analysis(single_csv, txt)
                    text.text_stats()

                    logging.info(f'{__class__.__name__ } [Finish - Processing report - {single_csv}]')

            else:
                logging.error(f'{__class__.__name__ } [{self.list_of_csv} is not type of list!')                

        except Exception as e:            
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)


if __name__ == "__main__":
    start = time()
    #acs = Report(ACS_CSV)
    #acs.acs_stats_single()
    #acs.acs_stats_multi()
    mng = Report(MNG_CSV)
    mng.mng_stats()
    end = time()
    delta = round((end - start), 4)
    execution_time = f'Reports processed - {ACS_CSV, MNG_CSV}. Elapsed time - {delta}'
    if smtp_enable:           
        Notificator.send_email(smtp_port,smtp_server,smtp_user,smtp_pass,receiver_email,execution_time,'FTDataAnalysis.log')
    else:
        logging.info(execution_time)