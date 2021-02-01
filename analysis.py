import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import dateutil
from datetime import datetime
from settings import logging

plt.rcParams.update({'figure.max_open_warning': 0})

class Reader(object):    
    def __init__(self, csvfile, columns):
        self.csvfile = csvfile
        self.columns = columns

    def read_data(self):
        data = pd.read_csv(self.csvfile, usecols=self.columns)        
        return data
    
    def read_single_col(self,colname):
        colvalues = []
        for x in self.read_data()[colname]:
            colvalues.append(x)
        return colvalues

class Analysis(Reader):
    """
    Accepts in class constructor: \n 
        - csvfile (str)
        - columns (list of str)
        - plot title (str)        
        - name of the image file to output (str) 
    Main method (void) .analize_param_vs_time() will save the plot to .graphs/ folder \n
    >>> cols = ['name','job','salary'] \n
    >>> data = Analysis('data.csv', cols, 'data.png') \n
    >>> data.analize_param_vs_time()
    >>> Successfully created data.png
    """
    def __init__(self, csvfile, columns, title=None, image_name=None, label=None, timeinterval=None):
        super().__init__(csvfile, columns)
        self.image_name = image_name
        self.title = title
        self.label = label
        self.timeinterval = timeinterval

    def single_kpi_vs_time(self):
        """
        Void -> save plot to .graphs/
        """             
        try:
            if self.timeinterval == None:
                hours = 5
            else:
                hours = self.timeinterval

            new = Reader(self.csvfile, self.columns)
            logging.info(f'{__class__.__name__ } [{new.__class__.__name__} Processing {self.columns}')      
            param = new.read_single_col(self.columns[0])        
            time = new.read_single_col(self.columns[1])
            logging.info(f'{__class__.__name__ } [Target KPI [{self.columns[0]}] ')
            logging.info(f'{__class__.__name__ } [Number of KPIs to be drawn - {len(param)}')       
            timestampt = [dateutil.parser.parse(s) for s in time]
            figure = plt.figure()
            ax = plt.gca().xaxis.set_major_locator(md.HourLocator(interval=5))
            figure, ax = plt.subplots(figsize=(15,4))            
            ax.xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y-%H:%M'))
            plt.plot_date(x=(timestampt), y=(param),xdate=True, fmt='b', label=self.label,)            
            plt.xticks(rotation=50)
            plt.xticks(timestampt)
            plt.tight_layout()
            plt.legend(loc="upper left")            
            plt.subplots_adjust(wspace=1, bottom=0.2)
            plt.title(self.title, loc='center')            
            ax.tick_params(direction='out', length=1, width=0.5, color='b')
            figure = plt.gca().xaxis.set_major_locator(md.HourLocator(interval=hours))
            plt.savefig(f'graphs/{self.image_name}', bbox_inches='tight')
            logging.info(f'{__class__.__name__ } [Successfully created {self.image_name} graph')            
        except Exception as e:            
            logging.exception(f'{__class__.__name__ } [Exception during creation of {self.image_name} graph')
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)            
        finally:
            plt.clf()
            plt.close(figure)     

    def multi_kpi_vs_time(self, label1, label2):
        """
        Void -> save plot to .graphs/
        """         
        try:
            new = Reader(self.csvfile, self.columns)
            logging.info(f'{__class__.__name__ } [{new.__class__.__name__} Processing {self.columns}')
            param = new.read_single_col(self.columns[0])
            param2 = new.read_single_col(self.columns[1])
            logging.info(f'{__class__.__name__ } [Target KPIs [{self.columns[0]}] [{self.columns[1]}] ')            
            logging.info(f'{__class__.__name__ } [Number of KPIs to be drawn - {(len(param)+len(param2))}')
            time = new.read_single_col(self.columns[2])        
            timestampt = [dateutil.parser.parse(s) for s in time]  
            figure = plt.figure()
            ax = plt.gca().xaxis.set_major_locator(md.HourLocator(interval=5))
            figure, ax = plt.subplots(figsize=(15,4))            
            ax.xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y-%H:%M'))
            plt.plot_date(x=(timestampt), y=(param),xdate=True, fmt='r', label=label1,)
            plt.plot_date(x=(timestampt), y=(param2),xdate=True, fmt='b', label=label2,)    
            plt.xticks(rotation=40)
            plt.xticks(timestampt)
            plt.tight_layout()
            plt.legend(loc="upper left")            
            plt.subplots_adjust(wspace=1, bottom=0.2)
            plt.title(self.title, loc='center')            
            ax.tick_params(direction='out', length=1, width=0.5, color='b')
            figure = plt.gca().xaxis.set_major_locator(md.HourLocator(interval=5))
            plt.savefig(f'graphs/{self.image_name}', bbox_inches='tight')
            logging.info(f'{__class__.__name__ } [Successfully created {self.image_name} graph')            
        except Exception as e:            
            logging.exception(f'{__class__.__name__ } [Exception during creation of {self.image_name} graph')
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)
        finally:
            plt.clf()
            plt.close(figure)

    def compare_acs(self):
        try:
            logging.info(f'{__class__.__name__ } [Successfully created {self.image_name} graph')            
        except Exception as e:            
            logging.exception(f'{__class__.__name__ } [Exception during creation of {self.image_name} graph')
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)

    def text_stats(self):
        try:
            logging.info(f'{__class__.__name__ } [Start - TXT stats generation')            
            data = pd.read_csv(self.csvfile, usecols=self.columns)
            server = str(self.csvfile).replace('.csv','')  
            with open(f'reports/{server}-kpis-summury.txt', 'a') as stats:
                    stats.write(f'KPIs Summury\n')
            for i in self.columns:
                max_v = data[i].max()
                min_v = data[i].min()
                avg = round(sum(data[i])/len(data[i]),2)
                MAX = f'MAX value for {i} - {max_v}'
                MIN = f'MIN value for {i} - {min_v}'
                AVG = f'AVG value for {i} - {avg}'
                with open(f'reports/{server}-kpis-summury.txt', 'a') as stats:
                    stats.write(f'\n{MAX}\n{MIN}\n{AVG}\n')
            
            logging.info(f'{__class__.__name__ } [End - TXT stats generation')  
        except Exception as e:                        
            logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)