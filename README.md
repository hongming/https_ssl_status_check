# https_ssl_status_check 网站证书批量巡检

# 巡检要求
    我们管理了一批域名domain，部分已经做了解析（二级、三级子域名），现在要做两个事情：           
1、排查这些域名是否https访问正常
2、如果是https访问正常，它的证书有效期到什么适合                 
    使用一个Python脚本，读取domains.txt文本文件，每次一行，并将结果补充到一个domains_check_当前时间.txt的文本文件。
正式执行前，命令行页面返回一句“Checking”，每次查询过一个域名，返回一句 "xxx domains https status checked, next..."，然后将结果写入文本文件。

# 代码来源
使用ChatGPT生成。