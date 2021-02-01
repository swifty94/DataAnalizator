# DataAnalizator

Application for analizing statistics of FTL ACS/UI applications provided in CSV format.

You just need to:
    -  have your CSV in correct format (see usage section and samples folder)
    -  define your settings in settings.py

Once it is done, you'll have graphs and text summury of KPI statistics for all the servers.
---

Installation:
---
    ``` git clone git@github.com:swifty94/DataAnalysis.git ```  
    ``` pip3 install -r dependencies.txt ```      

Usage:
---    
1. Header of each ACS serer CSV report for input MUST be as below:

timestampt,javathreads,oracle_1521,acs_port_8080,acs_port_8181,acs_port_8443,acs_port_80,acs_port_443,acs_port_8182,total_ram,used_ram,free_ram,java_ram,cpu_load

2. Header of each UI server CSV report for input MUST be as below:

timestampt,total_ram,free_ram,used_ram,cpu_total,cpu_loadavg,acs_8080,acs_8181,acs_8443,mysql,oracle,iis_ram,iis_cpu

3. Timestampt in the all CSVs MUST be in following standard - "DD-MM-YYYY-HH:MM:SS"

4. Please check content of 'samples' folder to see the input CSV reports exaples

5. Place your CSV reports to root directory of the application

6. Check settings.py and define your specific details there, such as name of the CSV files (see respective section of settings.py)
or SMTP.

7. Run:

On Linux

``` user@host:~$ python3 report.py & ```

On Windows

``` C:\Users\Administrator\DataAnalizator\> pythonw report.py```

7. Follow the log file (FTDataAnalysis.log) or if SMTP notification is defined and enabled - relax.

Examples:
---
![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/kpi-summury.png)

![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/acs1_8080_vs_80.png)

![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/acs1_port_80.png)

![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/acs1_cpu_load.png)

![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/acs1_javathreads.png)

![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/mng1_iis_ram.png)

![](https://raw.githubusercontent.com/swifty94/DataAnalizator/master/samples/acs1_db_connections.png)