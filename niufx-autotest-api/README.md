# niufx2-autotest-api(牛人榜API集成项目)

### 实现框架(基于unittest的ddt测试框架):



### 整体思路：

*


### 安装:

```
$ pip install -r requirements.txt
```

### 运行：

```
$ python3 ddtTest.py
```

### 配置：

* 0:退出程序
* 1:爬取swagger
* 2:更新yaml
* 3:生成case

### 项目结构

```
│  .gitignore
│  ddtTest.py
│  README.md
│  requirements.txt
│
├─data
│  └─testData
│
├─module
│  │  bodyDiff.py
│  │  ddt.py
│  │  swagger.py
│  │
│  └─BeautifulReport
│      │  BeautifulReport.py
│      │  README.md
│      │  __init__.py
│      │
│      └─template
│              template
│
└─resource
    ├─log
    ├─meta
    └─report
            测试报告.html
```

