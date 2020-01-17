# 移动监控平台-微信小程序 API
- [移动监控平台-微信小程序 API](#%e7%a7%bb%e5%8a%a8%e7%9b%91%e6%8e%a7%e5%b9%b3%e5%8f%b0-%e5%be%ae%e4%bf%a1%e5%b0%8f%e7%a8%8b%e5%ba%8f-api)
  - [约定](#%e7%ba%a6%e5%ae%9a)
  - [用户登录](#%e7%94%a8%e6%88%b7%e7%99%bb%e5%bd%95)
  - [主页](#%e4%b8%bb%e9%a1%b5)
    - [工程](#%e5%b7%a5%e7%a8%8b)
      - [获取工程数量](#%e8%8e%b7%e5%8f%96%e5%b7%a5%e7%a8%8b%e6%95%b0%e9%87%8f)
      - [获取施工数量趋势图](#%e8%8e%b7%e5%8f%96%e6%96%bd%e5%b7%a5%e6%95%b0%e9%87%8f%e8%b6%8b%e5%8a%bf%e5%9b%be)
      - [获取施工告警趋势图](#%e8%8e%b7%e5%8f%96%e6%96%bd%e5%b7%a5%e5%91%8a%e8%ad%a6%e8%b6%8b%e5%8a%bf%e5%9b%be)
    - [告警](#%e5%91%8a%e8%ad%a6)
      - [获取告警类型](#%e8%8e%b7%e5%8f%96%e5%91%8a%e8%ad%a6%e7%b1%bb%e5%9e%8b)
      - [获取告警数量](#%e8%8e%b7%e5%8f%96%e5%91%8a%e8%ad%a6%e6%95%b0%e9%87%8f)
      - [获取最近告警图片](#%e8%8e%b7%e5%8f%96%e6%9c%80%e8%bf%91%e5%91%8a%e8%ad%a6%e5%9b%be%e7%89%87)
      - [获取告警数量柱状图](#%e8%8e%b7%e5%8f%96%e5%91%8a%e8%ad%a6%e6%95%b0%e9%87%8f%e6%9f%b1%e7%8a%b6%e5%9b%be)
    - [设备](#%e8%ae%be%e5%a4%87)
      - [获取设备总数](#%e8%8e%b7%e5%8f%96%e8%ae%be%e5%a4%87%e6%80%bb%e6%95%b0)
      - [获取设备利用率](#%e8%8e%b7%e5%8f%96%e8%ae%be%e5%a4%87%e5%88%a9%e7%94%a8%e7%8e%87)
  - [实时监测](#%e5%ae%9e%e6%97%b6%e7%9b%91%e6%b5%8b)
    - [云台控制](#%e4%ba%91%e5%8f%b0%e6%8e%a7%e5%88%b6)
      - [云台控制-移动](#%e4%ba%91%e5%8f%b0%e6%8e%a7%e5%88%b6-%e7%a7%bb%e5%8a%a8)
      - [云台控制-预置位操作-和-巡航路径](#%e4%ba%91%e5%8f%b0%e6%8e%a7%e5%88%b6-%e9%a2%84%e7%bd%ae%e4%bd%8d%e6%93%8d%e4%bd%9c-%e5%92%8c-%e5%b7%a1%e8%88%aa%e8%b7%af%e5%be%84)
  - [工程管理](#%e5%b7%a5%e7%a8%8b%e7%ae%a1%e7%90%86)
    - [工程列表](#%e5%b7%a5%e7%a8%8b%e5%88%97%e8%a1%a8)
    - [工程概述](#%e5%b7%a5%e7%a8%8b%e6%a6%82%e8%bf%b0)
      - [工程详情](#%e5%b7%a5%e7%a8%8b%e8%af%a6%e6%83%85)
      - [工程详情 - 告警总览](#%e5%b7%a5%e7%a8%8b%e8%af%a6%e6%83%85---%e5%91%8a%e8%ad%a6%e6%80%bb%e8%a7%88)
    - [工程-告警记录](#%e5%b7%a5%e7%a8%8b-%e5%91%8a%e8%ad%a6%e8%ae%b0%e5%bd%95)
    - [工程-告警记录-关闭告警](#%e5%b7%a5%e7%a8%8b-%e5%91%8a%e8%ad%a6%e8%ae%b0%e5%bd%95-%e5%85%b3%e9%97%ad%e5%91%8a%e8%ad%a6)
    - [工程-历史采集](#%e5%b7%a5%e7%a8%8b-%e5%8e%86%e5%8f%b2%e9%87%87%e9%9b%86)
  - [告警管理](#%e5%91%8a%e8%ad%a6%e7%ae%a1%e7%90%86)
  - [设备管理](#%e8%ae%be%e5%a4%87%e7%ae%a1%e7%90%86)
    - [设备-列表](#%e8%ae%be%e5%a4%87-%e5%88%97%e8%a1%a8)
    - [设备-详情](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85)
    - [设备-详情-设备事件](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e8%ae%be%e5%a4%87%e4%ba%8b%e4%bb%b6)
    - [设备-详情-推流地址](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e6%8e%a8%e6%b5%81%e5%9c%b0%e5%9d%80)
    - [设备-详情-设备配置](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e8%ae%be%e5%a4%87%e9%85%8d%e7%bd%ae)
    - [设备-详情-历史采集(图片和视频)](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e5%8e%86%e5%8f%b2%e9%87%87%e9%9b%86%e5%9b%be%e7%89%87%e5%92%8c%e8%a7%86%e9%a2%91)
    - [设备-详情-历史采集-查看告警图片](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e5%8e%86%e5%8f%b2%e9%87%87%e9%9b%86-%e6%9f%a5%e7%9c%8b%e5%91%8a%e8%ad%a6%e5%9b%be%e7%89%87)
    - [设备-详情-告警记录](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e5%91%8a%e8%ad%a6%e8%ae%b0%e5%bd%95)
    - [设备-详情-查看告警](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e6%9f%a5%e7%9c%8b%e5%91%8a%e8%ad%a6)
    - [设备-详情-关闭告警](#%e8%ae%be%e5%a4%87-%e8%af%a6%e6%83%85-%e5%85%b3%e9%97%ad%e5%91%8a%e8%ad%a6)
    - [设备-地图](#%e8%ae%be%e5%a4%87-%e5%9c%b0%e5%9b%be)
    - [设备-地图-获取所有设备](#%e8%ae%be%e5%a4%87-%e5%9c%b0%e5%9b%be-%e8%8e%b7%e5%8f%96%e6%89%80%e6%9c%89%e8%ae%be%e5%a4%87)
    - [设备-地图-获取所有工程](#%e8%ae%be%e5%a4%87-%e5%9c%b0%e5%9b%be-%e8%8e%b7%e5%8f%96%e6%89%80%e6%9c%89%e5%b7%a5%e7%a8%8b)
  - [实体](#%e5%ae%9e%e4%bd%93)
    - [Engineering](#engineering)
    - [EngineeringStatus](#engineeringstatus)
    - [Alert](#alert)
    - [AlertSource](#alertsource)
    - [AlertType](#alerttype)
    - [AlertStatus](#alertstatus)
    - [Cruise](#cruise)
    - [Preset](#preset)
    - [User](#user)
    - [UserRole](#userrole)
    - [Worker](#worker)
    - [WorkerStatus](#workerstatus)

## 约定

测试服务器地址: `https://edgeai.jiangxing.cn/`

未特殊注明，`POST`、`PUT` 请求的 `Content-Type` 为 `application/json`。服务端响应默认为 json。

时间采用 Unix 时间戳表示，即 从格林威治时间1970年01月01日00时00分00秒起至对应时间的总秒数

用户使用 Cookie 保存登录状态，Cookie 名为： `jiangxing_login_ticket_app`，值由登录接口获取。

## 用户登录

**简要描述**

- 用户登录

**请求方式和请求URL**

- POST

- https://edgeai.jiangxing.cn/api/v2/guard/login

**请求参数**

| 参数名   | 类型   | 说明                      | 例子                               |
| -------- | ------ | ------------------------- | ---------------------------------- |
| username | string | 必填                      | `admin`                            |
| password | string | 必填, MD5哈希，字母转小写 | `21232f297a57a5a743894a0e4a801fc3` |

**例子**

```HTTP
POST /api/v2/guard/login HTTP/1.1
Host: edgeai.jiangxing.cn
Content-Type: application/json

{
	"username": "admin",
	"password": "21232f297a57a5a743894a0e4a801fc3"
}
```

**返回**

200

```json
{
    "data": {
        "create_time": 1577006608,
        "id": "5dff361038ab908f3ca2ae71",
        "name": "admin",
        "remark": "Super Administrator",
        "reset": true,
        "role": "admin",
        "ticket": "t32ZwSJxXCj3rXt3HuAy6tfZ7w9d5aUgVfscji0lL2NrY5/7PCECBI7+XSe4qviQ",
        "update_time": 1577006608,
        "user_id": 0
    },
    "desc": "success"
}
```

[`User`](#User)

| 字段名        | 说明                                       |
| ------------- | ------------------------------------------ |
| `name`        | 用户名                                     |
| `ticket`      | 此次登录使用的 ticket，默认有效期为 3 天。 |
| `create_time` | 时间戳，用户创建时间                       |
| `update_time` | 时间戳，用户资料最后一次更新时间           |
| `user_id`     | 用户在系统中的 uid                         |
| `role`        | 用户的角色                                 |
| `remark`      | 用户在前端界面展示时，显示的名称           |

401 密码错误

```json
{
    "desc":"invalid password"
}
```

401 用户错误

```json
{
    "desc":"user not found"
}
```

## 主页

### 工程

#### 获取工程数量


**简要描述**

- 获取工程的基本数量

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/engineering/quantity

**返回参数**

| 参数名        | 类型 | 说明     | 补充   |
| ------------- | ---- | -------- | ------ |
| all_count     | int  | 工程总数 |
| being_count   | int  | 正在施工 |
| overdue_count | int  | 已逾期   |
| nostart_count | int  | 未开始   |
| today_count   | int  | 今日工程 | 未用到 |
| e_list   | EngineeringList  | 工程列表 |
| e_list[$]    |  [`Engineering`](#Engineering)  | 工程 ID |
| e_list[$].id   | string  | 工程 ID |
| e_list[$].name   | string  | 工程名 |
| e_list[$].starttime   | 时间戳  | 工程开始时间 |
| e_list[$].status   | [`EngineeringStatus`](#EngineeringStatus)  | 工程状态

**例子**

```HTTP
GET /api/v2/guard/engineering/quantity HTTP/1.1
Host: edgeai.jiangxing.cn
Cookie: jiangxing_login_ticket_app="t32ZwSJxXCj3rXt3HuAy6tfZ7w9d5aUgVfscji0lL2NrY5/7PCECBI7+XSe4qviQ"
```

**返回**

200

```json
{
    "data": {
        "all_count": 5,
        "being_count": 0,
        "e_list": [
            {
                "id": "5e05e2d6dd3cd961c90f92e2",
                "name": "测试",
                "starttime": 1577376000,
                "status": "finished"
            },
            {
                "id": "5e016b48c520b90034e7244d",
                "name": "12.24",
                "starttime": 1577289600,
                "status": "finished"
            },
            {
                "id": "5e0185f8c520b90034e72536",
                "name": "时间的颜色",
                "starttime": 1577116800,
                "status": "finished"
            },
            {
                "id": "5dff7c4c81efe031e5ebbc19",
                "name": "还我蔚蓝",
                "starttime": 1577030400,
                "status": "finished"
            },
            {
                "id": "5dff5d1d2d60f48da79be124",
                "name": "12.22",
                "starttime": 1576944000,
                "status": "finished"
            }
        ],
        "nostart_count": 0,
        "overdue_count": 0,
        "today_count": 0
    },
    "desc": "success"
}
```


#### 获取施工数量趋势图

[缺少接口]

#### 获取施工告警趋势图

[缺少接口]

### 告警

#### 获取告警类型


**简要描述**

- 获取现有的告警类型

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/type

**返回参数**

| 参数名 | 类型   | 说明                   |
| ------ | ------ | ---------------------- |
| type   | string | 前端请求后端使用的字段 |
| label  | string | 页面显示的字段         |

**返回**

200

```json
{
    "data": [
        {
            "label": "未宣读工作票",
            "type": "read_work_tickets"
        },
        {
            "label": "入侵电子围栏",
            "type": "fence"
        },
        {
            "label": "未佩戴安全帽",
            "type": "helmets"
        },
        {
            "label": "未佩戴绝缘手套",
            "type": "insulated_gloves"
        },
        {
            "label": "未安装接地棒",
            "type": "ground_rods"
        },
        {
            "label": "烟火",
            "type": "fire"
        }
    ],
    "desc": "success"
}
```

#### 获取告警数量

**简要描述**

- 不同告警类型的告警数量

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/history

**请求参数**

| 参数名     | 类型   | 说明     | 补充                                        |
| ---------- | ------ | -------- | ------------------------------------------- |
| alert_type | [`AlertType`](#AlertType) | 告警类型 | 使用/api/v2/guard/alert/type 接口的type字段 |
| status     | string | 状态     |
| from       | string | 起始时间 | utc 时间戳                                  |
| until      | string | 终是时间 | utc 时间戳                                  |



**返回参数**

| 参数名            | 类型   | 说明           |
| ----------------- | ------ | -------------- |
| read_work_tickets | string | 未宣读工作票   |
| fence             | string | 入侵电子围栏   |
| helmets           | string | 未佩戴安全帽   |
| insulated_gloves  | string | 未佩戴绝缘手套 |
| ground_rods       | string | 未安装接地棒   |
| fire              | string | 烟火           |

**返回**

200

```json
{
    "data": {
        "alert_type": {
            "fence": 31,
            "fire": 1,
            "ground_rods": 382,
            "helmets": 120,
            "insulated_gloves": 120,
            "read_work_tickets": 384
        }
    },
    "desc": "success"
}
```

#### 获取最近告警图片

**简要描述**

- 告警列表， 告警列表根据时间排序(最新的在最前面)， 图片可以通过
https://edgeai.jiangxing.cn/media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-51-03.jpg 获取到。

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview

**请求参数**

| 参数名 | 类型 | 说明                         | 补充 |
| ------ | ---- | ---------------------------- | ---- |
| offset | int  | 起始索引                     |
| limit  | int  | 从起始索引开始，返回几个数据 |


**返回参数**

| 参数名        | 类型   | 说明           | 补充                               |
| ------------- | ------ | -------------- | ---------------------------------- |
| affirmed      | bool   | 告警是否被查看 | False 未被查看                     |
| alert_source  | string | 告警来源       |                                    |
| alert_type    | string | 告警类型       | 参考上文                           |
| detect_result | dict   | AI检测结果     | 只需要将person用框框起来           |
| host_id       | string | 告警设备ID     |
| img_url       | string | 图片地址       |
| starttime     | int    | 告警时间       |
| status        | [`AlertStatus`](#AlertStatus) | 告警状态       | opening 和 closed                  |
| update_time   | int    | 更新事件       | 例如: 告警的查看事件 或者 关闭事件 |

**返回**

200

```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```

#### 获取告警数量柱状图

[缺少接口]

### 设备

#### 获取设备总数


**简要描述**

- 返回设备数量

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/worker/quantity

**返回参数**

| 参数名            | 类型 | 说明    |
| ----------------- | --- | --------| 
| not_alive_count   | int | 断开数量 |
| alive_count       | int | 正常数量 |
| electricity_count | int | 电量异常 |
| flow_count        | int | 流量异常 |
| card_count        | int | SD卡异常 |

**返回**

200

```json
{
    "data": {
        "alive_count": 1,
        "card_count": 1,
        "electricity_count": 1,
        "flow_count": 0,
        "not_alive_count": 0
    },
    "desc": "success"
}
```

#### 获取设备利用率

[缺少接口]

## 实时监测


**简要描述**

- 获取前几张图片

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/monitor/history

**请求参数**

| 参数名         | 类型   | 说明      |
| -------------- | ---    | -------- | 
| from           | string | 起始时间  | utc 时间戳
| until          | string | 终是时间  | utc 时间戳
| engineering_id | string | 工程_ID   |
| offset         | int    | 起始索引  |
| limit          | int    | 从起始索引开始，返回几个数据 |
| device_searc   | string | 设备名称的搜索 |

**返回参数**

| 参数名            | 类型   | 说明      |
| --------------    | ---    | -------- | 
| title              | string | 该字段不为空，表示该图片是告警图片
| detect_result      | dict   | 如果 title 不为空，则画里面的框
| coordinate         | string | 如果 title 是 fence, 则绘制该框
| img_src            | string | 图片地址
| worker_info   | [`Worker`](#Worker) | 设备信息
| worker_info.name   | string | 设备名称
| worker_info.address| string | 设备地址
| worker_info.engineering| [`Engineering`](#Engineering) | 该设备现在所属的工程
| worker_info.engineering.name| string | 该设备现在所属的工程名称
| worker_info.engineering.name| string | 该设备现在所属的工程单位

**返回**

200
```json
{
    "data":{
        "data":[
            {
                "coordinate":{

                },
                "detect_result":{

                },
                "host_id":"J018ec20df",
                "img_src":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/07-41-09.jpg",
                "time":1577432469,
                "title":"read_work_tickets",
                "worker_info":{
                    "name":"移动警卫兵-二次演示-2号机",
                    "engineering": {
                        "id": "5e05b98dd4b84bc22d401672",
                        "name": "问问",
                        "unit": "问问"
                    },
                    "address":"广东省深圳市宝安区海天路",
                    "id":"J018ec20df",
                    "password":"123456",
                    "position":{
                        "latitude":2232.955294,
                        "longitude":11353.053698
                    },
                    "status":"normal"
                }
            }
        ],
        "total":6416
    },
    "desc":"success"
}
```

### 云台控制


**简要描述**

- 根据ID， 获取设备的信息

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/worker/info?id=J018ec20df

**请求参数**

| 参数名  | 类型   | 说明      |
| ------ | ---    | -------- | 
| id     | string | 设备ID  |

**返回参数**

[`Worker`](#Worker)

| 参数名               | 类型   | 说明     
| -------------------- | ---    | --------  
| name                 | string | 设备名称
| address              | string | 设备地址
| engineering.name     | string | 该设备现在所属的工程名称
| engineering.unit     | string | 该设备现在所属的工程单位(即施工队)
| engineering.starttime| int    | 施工时间

**返回**

200
```json
{
    "data":{
        "address":"广东省深圳市宝安区海天路",
        "engineering":{
            "id":"5e05b98dd4b84bc22d401672",
            "name":"问问",
            "unit":"问问",
            "starttime": 1577376000
        },
        "fence":{
            "coordinate":{
                "xmax":"1920.0000000000002",
                "xmin":"21.098901098901102",
                "ymax":"1021.0549450549452",
                "ymin":"20.96703296703289"
            },
            "status":false
        },
        "group_worker_list":[
            "测试分组"
        ],
        "id":"J018ec20df",
        "name":"移动警卫兵-二次演示-2号机",
        "password":"123456",
        "platform":"arm64v8",
        "position":{
            "latitude":2232.955294,
            "longitude":11353.053698
        },
        "status":"normal"
    },
    "desc":"success"
}
```

#### 云台控制-移动


**简要描述**

- 根据ID，移动球机

**请求方式和请求URL**

- POST

- https://edgeai.jiangxing.cn/api/v2/guard/camera/move

**请求参数**

| 参数名     | 类型   | 说明     | 补充     |
| --------- | -------| -------- | ------- |
| worker_id | string | 设备ID   | 
| option    | string | 操作选项  | move、stop、set_home 或 goto_home
| config    | string | move 的时候生效 | 

```
### 移动 timeout 决定移动的时间， pan tilt 表示旋转角度
左 {"pan": -0.1, "tilt": 0, "zoom": 0, "timeout": 0.1}
右 {"pan": 0.1, "tilt": 0, "zoom": 0, "timeout": 0.1}
上 {"pan": 0, "tilt": 0.1, "zoom": 0, "timeout": 0.1}
下 {"pan": 0, "tilt": -0.1, "zoom": 0, "timeout": 0.1}
左上 {"pan": -0.1, "tilt": 0.1, "zoom": 0, "timeout": 0.1}
左下 {"pan": -0.1, "tilt": -0.1, "zoom": 0, "timeout": 0.1}
右上 {"pan": 0.1, "tilt": 0.1, "zoom": 0, "timeout": 0.1}
右下 {"pan": 0.1, "tilt": -0.1, "zoom": 0, "timeout": 0.1}

### 变倍 timeout 的大小决定变倍一次的程度
+ {"pan": 0, "tilt": 0, "zoom": 1, "timeout": 0.1}
- {"pan": 0, "tilt": 0, "zoom": -1, "timeout": 0.1}
```

例如:
```json
{
    "worker_id":"J018ec20df",
    "option":"stop",
    "config":{
        "pan":0.4,
        "tilt":0,
        "zoom":0,
        "timeout":0.5
    },
}
```

**返回参数**

| 参数名      | 类型| 说明     
| -------- ---|----| --------  
| cruise.data |list| 巡航路径列表
| cruise.total|int | 巡航路径总数
| preset.data |list| 预置点列表
| preset.total|int | 预置点总数


**返回**

200
```json
{
    "data":"",
    "desc":"success"
}
```


#### 云台控制-预置位操作-和-巡航路径


**简要描述**

- 返回预置位列表和巡航路径列表

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/camera/cruise

**请求参数**

| 参数名     | 类型   | 说明     |
| --------- | -------| -------- | 
| worker_id | string | 设备ID   |

**返回**

200
```json
{
    "data":{
        "cruise":{
            "data":[
                {
                    "create_time":1576813643,
                    "id":"5dfc444bbd6272e74f74a066",
                    "name":"test",
                    "route":[
                        {
                            "id":"5e0486464f482c4c850408ce",
                            "is_home":false,
                            "name":"jack",
                            "sleep_time":5,
                            "set_id":2
                        },
                        {
                            "id":"5e05c8af94ecf3b3a2ff10f8",
                            "is_home":false,
                            "name":"name",
                            "set_id":3
                        },
                        {
                            "id":"5e05c8dc94ecf3b3a2ff10fa",
                            "is_home":false,
                            "name":"演的金",
                            "set_id":4
                        }
                    ],
                    "status":"stop",
                    "update_time":1577437423,
                    "worker_id":"J018ec20df"
                }
            ],
            "total":1
        },
        "preset":{
            "data":[
                {
                    "id":"5e0486464f482c4c850408ce",
                    "is_home":false,
                    "name":"jack",
                    "set_id":2
                },
                {
                    "id":"5e05c8af94ecf3b3a2ff10f8",
                    "is_home":false,
                    "name":"name",
                    "set_id":3
                },
                {
                    "id":"5e05c8dc94ecf3b3a2ff10fa",
                    "is_home":false,
                    "name":"演的金",
                    "set_id":4
                }
            ],
            "total":3
        }
    },
    "desc":"success"
}
```


**简要描述**

- 到达某个预置位或进行巡航

**请求方式和请求URL**

- POST

- https://edgeai.jiangxing.cn/api/v2/guard/camera/cruise_move

**请求参数**

| 参数名     | 类型   | 说明     |
| --------- | -------| -------- | 
| worker_id | string | 设备ID   |
| preset_id | string | 预制点ID |
| cruise_id | string | 巡航ID |

**返回**

200
```
到某个预制点
{"worker_id":"J018ec20df","preset_id":"5e0486464f482c4c850408ce"}

{
    "data":{
        "preset_id":"5e0486464f482c4c850408ce",
        "worker_id":"J018ec20df"
    },
    "desc":"success"
}

进行巡航
{"worker_id":"J018ec20df","cruise_id":"5e05c98e94ecf3b3a2ff1101"}
```

**简要描述**

- 停止巡航

**请求方式和请求URL**

- DELETE

- https://edgeai.jiangxing.cn/api/v2/guard/camera/cruise_move

**请求参数**

| 参数名     | 类型   | 说明     |
| --------- | -------| -------- | 
| worker_id | string | 设备ID   |

**返回**

200
```

请求停止巡航

{"worker_id":"J018ec20df","cruise_id":"5e05c98e94ecf3b3a2ff1101"}

{
    "data":"",
    "desc":"success"
}
```


**简要描述**

- 手动拍照

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/camera/capture
**请求参数**

| 参数名     | 类型   | 说明     |
| --------- | -------| -------- | 
| worker_id | string | 设备ID   |

**返回**

200
```json
{
    "data":{
        "image":"/9j/4AAQSkZV",
        "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/09-26-38.jpg"
    },
    "desc":"success"
}
```

## 工程管理

### 工程列表

**简要描述**

- 显示工程列表和总数

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/engineering/management

**请求参数**

| 参数名     | 类型   | 说明     |
| --------- | -------| -------- | 
| offset | int    | 起始索引  |
| limit  | int    | 从起始索引开始，返回几个数据 |
| status | string | 工程状态, 有四种状态: notstart、being、finished、overdue
| from   | int    | 起始时间
| until  | int    | 终止时间
| search | string | 根据施工名称搜索
   
   

**返回参数**


| 参数名    | 类型   | 说明     |
| -------- | -------| -------- | 
| name     | string | 工程名称 |
| address  | string |  施工地址|
| starttime| int    | 施工时间 |
| status   | string | 工程状态, 有四种状态: notstart、being、finished、overdue|
| worker_list | list | 属于该工程的设备列表|
| worker_list[0].name | string | 设备名称 |
   

**返回**

200
```json
{
    "data": {
        "data": [
            {
                "address": "威威呃",
                "create_time": 1577433485,
                "endtime": 1577376000,
                "id": "5e05b98dd4b84bc22d401672",
                "name": "问问",
                "starttime": 1577376000,
                "status": "being",
                "total_alert_count": 45,
                "total_running_time": 1826,
                "unit": "问问",
                "update_time": 1577440308,
                "worker_list": [
                    {
                        "address": "广东省深圳市宝安区海天路",
                        "card": {
                            "precent": 8.955990233709347,
                            "total": 14662287360,
                            "used": 0
                        },
                        "elec": {
                            "precent": 0.18,
                            "total": 15000,
                            "used": 0
                        },
                        "flow": {
                            "precent": 100,
                            "total": 10,
                            "used": 0
                        },
                        "name": "移动警卫兵-二次演示-2号机",
                        "position": {
                            "latitude": 2232.955294,
                            "longitude": 11353.053698
                        },
                        "worker_id": "J018ec20df"
                    }
                ]
            }
            ......
        ],
        "total": 13
    },
    "desc": "success"
}
```

### 工程概述


#### 工程详情

**简要描述**

- 显示工程详情

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/engineering/management

**请求参数**

| 参数名 | 类型   | 说明     |
| ----- | -------| -------- | 
| id    | string | 工程的ID
   
   

**返回参数**


| 参数名    | 类型   | 说明     |
| -------- | -------| -------- | 
| name     | string | 工程名称 |
| address  | string |  施工地址|
| starttime| int    | 施工时间 |
| status   | string | 工程状态, 有四种状态: notstart、being、finished、overdue|
| worker_list | list | 属于该工程的设备列表|
| worker_list[0].name | string | 设备名称 |
| 工程的最新采集| string | [没有接口]
| worker_list[0].card.used| int | 设备总耗电量 = used / total
| worker_list[0].flow.used| int | 使用流量 = used / total
| worker_list[0].card.used| int | 设备SD卡容量 = used / total


**返回**

200
```json
{
    "data": {
        "address": "123123",
        "create_time": 1576654240,
        "endtime": 1577548800,
        "goal": "12312",
        "id": "5df9d5a02c67dfaedb98b0c3",
        "name": "123213",
        "starttime": 1577548800,
        "status": "overdue",
        "total_alert_count": 0,
        "total_running_time": 0,
        "unit": "123123",
        "update_time": 1577684813,
        "worker_list": [
            {
                "card": {
                    "precent": 7.707240352435705,
                    "total": 14662287360,
                    "used": 0
                },
                "elec": {
                    "precent": 3.3570701932858595,
                    "total": 983,
                    "used": 0
                },
                "flow": {
                    "precent": 99.99241605401039,
                    "total": 1073741824,
                    "used": 81432
                },
                "worker_id": "J018ec20df"
            }
        ]
    },
    "desc": "success"
}
```


#### 工程详情 - 告警总览

**简要描述**

- 某个工程的不同告警类型的数量

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/history

**请求参数**

| 参数名         | 类型   | 说明     |
| -----         | -------| -------- | 
| engineering_id| string | 工程的ID
   
   

**返回参数**

| 参数名            | 类型    | 说明          |
| ----------------  | ------ | ------------- | 
| read_work_tickets | string | 未宣读工作票   |
| fence             | string | 入侵电子围栏   |
| helmets           | string | 未佩戴安全帽   |
| insulated_gloves  | string | 未佩戴绝缘手套 |
| ground_rods       | string | 未安装接地棒   |
| fire              | string | 烟火          | 

**返回**

200
```json
{
    "data": {
        "alert_type": {
            "fence": 1,
            "fire": 1,
            "ground_rods": 44,
            "helmets": 29,
            "insulated_gloves": 29,
            "read_work_tickets": 44
        }
    },
    "desc": "success"
}
```


### 工程-告警记录


**简要描述**

- 某个工程的告警列表

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview

**请求参数**

| 参数名         | 类型   | 说明       |
| -----         | -------| --------- |  
| offset        | int    | 起始索引  |
| limit         | int    | 从起始索引开始，返回几个数据 |
| engineering_id| string | 工程的ID   |
| status        | string | 告警状态筛选|
| alert_type    | string | 告警类型筛选|
| from       | string | 起始时间    | utc 时间戳
| until      | string | 终是时间    | utc 时间戳


**返回参数**

| 参数名             | 类型    | 说明          | 补充                  |
| -------------      | ------ | ------------- | --------------------- |
| affirmed           | bool   | 告警是否被查看 | False 未被查看         |
| alert_source       | string | 告警来源       |                      |
| alert_type         | string | 告警类型      | 参考上文               |
| detect_result      | dict   | AI检测结果    | 只需要将person用框框起来|
| host_id            | string | 告警设备ID    |
| img_url            | string | 图片地址      | 
| starttime          | int    | 告警事件      | 
| status             | string | [`AlertStatus`](#AlertStatus)      | opening 和 closed     |
| update_time        | int    | 更新事件      | 例如: 告警的查看事件 或者 关闭事件| 
| worker.address     | string | 告警地址      | 也是设备地址
| engineering.name   | string | 工程名称      | 
| engineering.address| string | 工程地址      | 
| engineering.unit   | string | 工程单位      | 也是施工队
| id                 | string | 告警的ID      |关闭告警的时候使用

**返回**

200
```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389,
                "worker": {
                    "address": "广东省深圳市宝安区海天路",
                }
                "engineering": {
                    "address": "12.24",
                    "name": "12.24",
                    "unit": "12.24",
                },
                id: "5e05d1e2196201b0699d30ff"
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```


### 工程-告警记录-关闭告警


**简要描述**

- 关闭某个告警

**请求方式和请求URL**

- DELETE

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview

**请求参数**

| 参数名 | 类型  | 说明       |
| ----- | ------| --------- |  
| id    | string| 告警的ID  |


**返回参数**

| 参数名             | 类型    | 说明          | 补充                  |
| -------------      | ------ | ------------- | --------------------- |
| alert_source       | string | 告警来源       |                      |
| alert_type         | string | 告警类型      | 参考上文               |
| detect_result      | dict   | AI检测结果    | 只需要将person用框框起来|
| host_id            | string | 告警设备ID    |
| img_url            | string | 图片地址      | 
| starttime          | int    | 告警事件      | 
| status             | string | 告警状态      | opening 和 closed     |
| update_time        | int    | 更新事件      | 此处使用
| worker.address     | string | 告警地址      | 也是设备地址
| engineering.name   | string | 工程名称      | 
| engineering.address| string | 工程地址      | 
| engineering.unit   | string | 工程单位      | 也是施工队
| operator           | string | 关闭告警的人  | 此处使用

**返回**

200
```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389,
                "worker": {
                    "address": "广东省深圳市宝安区海天路",
                }
                "engineering": {
                    "address": "12.24",
                    "name": "12.24",
                    "unit": "12.24",
                }，
                "operator":"admin",
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```

### 工程-历史采集


**简要描述**

- 查看某工程的历史图片， 如果该图片显示告警

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/monitor/history

**请求参数**

| 参数名         | 类型   | 说明      |
| -------------- | ---    | -------- | 
| from           | string | 起始时间  | utc 时间戳
| until          | string | 终是时间  | utc 时间戳
| engineering_id | string | 工程_ID   |
| offset         | int    | 起始索引  |
| limit          | int    | 从起始索引开始，返回几个数据 |
| device_searc   | string | 设备名称的搜索 |

**返回参数**

| 参数名            | 类型   | 说明      |
| --------------    | ---    | -------- | 
| title              | string | 该字段不为空，表示该图片是告警图片
| detect_result      | dict   | 如果 title 不为空，则画里面的框
| coordinate         | string | 如果 title 是 fence, 则绘制该框
| img_src            | string | 图片地址
| worker_info.name   | string | 设备名称
| worker_info.address| string | 设备地址
| worker_info.engineering.name| string | 该设备现在所属的工程名称
| worker_info.engineering.name| string | 该设备现在所属的工程单位

**返回**

200
```json
{
    "data":{
        "data":[
            {
                "coordinate":{

                },
                "detect_result":{

                },
                "host_id":"J018ec20df",
                "img_src":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/07-41-09.jpg",
                "time":1577432469,
                "title":"read_work_tickets",
                "worker_info":{
                    "name":"移动警卫兵-二次演示-2号机",
                    "engineering": {
                        "id": "5e05b98dd4b84bc22d401672",
                        "name": "问问",
                        "unit": "问问"
                    },
                    "address":"广东省深圳市宝安区海天路",
                    "id":"J018ec20df",
                    "password":"123456",
                    "position":{
                        "latitude":2232.955294,
                        "longitude":11353.053698
                    },
                    "status":"normal"
                }
            }
        ],
        "total":6416
    },
    "desc":"success"
}
```

## 告警管理


**简要描述**

- 告警列表， 告警列表根据时间排序(最新的在最前面)， 图片可以通过
https://edgeai.jiangxing.cn/media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-51-03.jpg 获取到。

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview

**请求参数**

| 参数名         | 类型   | 说明       |
| -----         | -------| --------- |  
| offset        | int    | 起始索引  |
| limit         | int    | 从起始索引开始，返回几个数据 |
| status        | string | 告警状态筛选|
| alert_type    | string | 告警类型筛选|
| from       | string | 起始时间    | utc 时间戳
| until      | string | 终是时间    | utc 时间戳


**返回参数**

| 参数名             | 类型    | 说明          | 补充                  |
| -------------      | ------ | ------------- | --------------------- |
| affirmed           | bool   | 告警是否被查看 | False 未被查看         |
| alert_source       | string | 告警来源       |                      |
| alert_type         | string | 告警类型      | 参考上文               |
| detect_result      | dict   | AI检测结果    | 只需要将person用框框起来|
| host_id            | string | 告警设备ID    |
| img_url            | string | 图片地址      | 
| starttime          | int    | 告警事件      | 
| status             | string | 告警状态      | opening 和 closed     |
| update_time        | int    | 更新事件      | 例如: 告警的查看事件 或者 关闭事件| 
| worker.address     | string | 告警地址      | 也是设备地址
| engineering.name   | string | 工程名称      | 
| engineering.address| string | 工程地址      | 
| engineering.unit   | string | 工程单位      | 也是施工队
| id                 | string | 告警的ID      |关闭告警的时候使用

**返回**

200
```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389,
                "worker": {
                    "address": "广东省深圳市宝安区海天路",
                }
                "engineering": {
                    "address": "12.24",
                    "name": "12.24",
                    "unit": "12.24",
                },
                id: "5e05d1e2196201b0699d30ff"
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```

## 设备管理

### 设备-列表


**简要描述**

- 设备的列表

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/worker/group_operate

**请求参数**

| 参数名  | 类型   | 说明       |
| -----  | -------| --------- |  
| offset | int    | 起始索引  |
| limit  | int    | 从起始索引开始，返回几个数据 |

**返回参数**

| 参数名  | 类型   | 说明    | 补充 |
| ------ | ------ | ------- | --- |
| name   | string | 设备名称 | 
| status | string | 设备状态 | normal or abnormal
| address| string | 设备地址 | 
| engineering.name| string | 工程名称 |
| engineering.unit| string | 工程的单位 | 也叫施工队
| card.precent| float | 剩余SD卡容量
| flow.precent| float | 剩余流量
| elec.precent| float | 剩余电量

**返回**

200
```json
{
    "data":{
        "total":1,
        "worker_list":[
            {
                "name":"移动警卫兵-二次演示-2号机",
                "status":"abnormal",
                "address":"深圳",
                "engineering":{
                    "id":"5e09a7c24e8424d82ae9c4bc",
                    "name":"1234234",
                    "starttime":1577635200,
                    "unit":"2342342"
                },
                "card":{
                    "precent":8.955990233709347
                },
                "elec":{
                    "precent":0.18
                },
                "flow":{
                    "precent":100
                }
            }
        ]
    },
    "desc":"success"
}

```

### 设备-详情


**简要描述**

- 设备详细信息

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/worker/info

**请求参数**

| 参数名 | 类型   | 说明   |
| ----- | -------| ------|  
| id    | string | 设备ID|

**返回参数**

| 参数名       | 类型   | 说明    | 补充 |
| ------      | ------ | ------- | --- |
| name        | string | 设备名称 | 
| status      | string | 设备状态 | normal or abnormal
| address     | string | 设备地址 | 
| id          | string | 设备编号 | 
| wakeup_time | int | 上次启动时间
| card.precent| float | 剩余SD卡容量
| flow.precent| float | 剩余流量
| elec.precent| float | 剩余电量

**返回**

200
```json
{
    "data":{
        "4g_flow":10,
        "address":"",
        "alert_total":0,
        "card":{
            "precent":8.955990233709347,
            "total":14662287360,
            "used":0
        },
        "card_status":"abnormal",
        "coordinates":null,
        "create_time":1577014745,
        "elec":{
            "precent":0.18,
            "total":15000,
            "used":0
        },
        "elec_abnormal":"normal",
        "elec_status":"abnormal",
        "engineering":{
            "id":"5e09a7c24e8424d82ae9c4bc",
            "name":"1234234",
            "starttime":1577635200,
            "unit":"2342342"
        },
        "fence":{
            "coordinate":{
                "xmax":"1920.0000000000002",
                "xmin":"21.098901098901102",
                "ymax":"1021.0549450549452",
                "ymin":"20.96703296703289"
            },
            "status":false
        },
        "flow":{
            "precent":100,
            "total":10,
            "used":0
        },
        "flow_status":"normal",
        "group_worker_list":[
            "测试分组"
        ],
        "hostname":"J018ec20df",
        "id":"J018ec20df",
        "ip":"10.208.20.33",
        "is_new":false,
        "is_registered":true,
        "name":"移动警卫兵-二次演示-2号机",
        "organization_id":"ffffffffffffffffffffffff",
        "password":"123456",
        "platform":"arm64v8",
        "position":{
            "latitude":2232.955294,
            "longitude":11353.053698
        },
        "register_time":1575365626,
        "running_total":123,
        "status":"abnormal",
        "update_time":1577014745,
        "wakeup_time":1576909004
    },
    "desc":"success"
}

```

### 设备-详情-设备事件

**简要描述**

- 设备事件

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview?limit=5&offset=0&event_type=sys

**请求参数**

| 参数名    | 类型   | 说明   |
| ----------| -------| ------|  
| offset    | int    | 起始索引  |
| limit     | int    | 从起始索引开始，返回几个数据 |
| from      | string | 起始时间| utc 时间戳
| until     | string | 终是时间| utc 时间戳
| worker_id | string | 设备ID|
| event_type| string | 告警类型| 这里必须是sys

**返回参数**

| 参数名    | 类型    | 说明          | 补充                  |
| ----------| ------ | ------------- | --------------------- |
| affirmed  | bool   | 事件是否被查看 | False 未被查看         |
| alert_type| string | 事件类型      | sys               |
| host_id   | string | 事件设备ID    |
| title     | string | 事件名称      | 
| starttime | int    | 事件时间      | 
| total     | int    | 事件总数      | 

**返回**

200

```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_type":"sys",
                "host_id":"J018ec20df",
                "title":"SD卡容量告警",
                "worker": {
                    "name": "移动警卫兵-二次演示-2号机"
                }
            }
            .....
        ],
        "total":195
    },
    "desc":"success"
}
```

### 设备-详情-推流地址

**简要描述**

- 设备的推流地址

**请求方式和请求URL**

- POST

- https://edgeai.jiangxing.cn/api/v2/guard/camera/stream

**请求参数**

| 参数名    | 类型   | 说明   |
| ----------| -------| ------|  
| worker_ids| list   | 设备id列表  |

**返回参数**

| 参数名        | 类型  | 说明   
| --------------| ---- | ----- | 
| data.worker_id|string| 流地址 |

**返回**

200

```json
{
    "data":{
        "J018ec20df":"rtmp://127.0.0.1:30035/live/j018ec20df-iotedge-camera0"
    },
    "desc":"success"
}

```
200 异常的结果
```json
{
    "data":{
        "J018ec20df":""
    },
    "desc":"success"
}

```


### 设备-详情-设备配置

**简要描述**

- 设备的配置

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/worker/config
**请求参数**

| 参数名| 类型  | 说明   |
| ------| ------| ------|  
| id    | string| 设备ID|


**返回参数**

| 参数名                      | 类型  | 说明                                 |
| ----------------------------| ---- | ------------------------------------ | 
| data.image.upload.only_alert| bool | True 仅上次告警图片, False 上次所有图片 |
| data.video.upload.only_alert| bool | True 仅上次告警视频, False 上次所有视频 |

**返回**

200

```json
{
    "data":{
        "image":{
            "upload":{
                "only_alert":false
            }
        },
        "video":{
            "upload":{
                "only_alert":false
            }
        }
    },
    "desc":"success"
}

```


### 设备-详情-历史采集(图片和视频)

**简要描述**

- 设备的历史采集

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/monitor/history
**请求参数**


| 参数名   | 类型   | 说明      |
| ------   | ---    | -------- | 
| from     | string | 起始时间  | utc 时间戳
| until    | string | 终是时间  | utc 时间戳
| offset   | int    | 起始索引  |
| limit    | int    | 从起始索引开始，返回几个数据 |
| worker_id| string | 设备ID |
| video    | string | 是否选择告警视频 | 如果请求视频， 该自动为true, 否则不需要该字段

**返回参数**

| 参数名            | 类型   | 说明      |
| --------------    | ---    | -------- | 
| title              | string | 该字段不为空，表示该图片是告警图片
| detect_result      | dict   | 如果 title 不为空，则画里面的框
| coordinate         | string | 如果 title 是 fence, 则绘制该框
| img_src            | string | 图片地址
| time               | int    | 图片时间
| worker_info.name   | string | 设备名称
| worker_info.address| string | 设备地址
| worker_info.engineering.name| string | 该设备现在所属的工程名称
| worker_info.engineering.name| string | 该设备现在所属的工程单位

**返回**

200
```json
{
    "data":{
        "data":[
            {
                "coordinate":{

                },
                "detect_result":{

                },
                "host_id":"J018ec20df",
                "img_src":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/07-41-09.jpg",
                "time":1577432469,
                "title":"read_work_tickets",
                "worker_info":{
                    "name":"移动警卫兵-二次演示-2号机",
                    "engineering": {
                        "id": "5e05b98dd4b84bc22d401672",
                        "name": "问问",
                        "unit": "问问"
                    },
                    "address":"广东省深圳市宝安区海天路",
                    "id":"J018ec20df",
                    "password":"123456",
                    "position":{
                        "latitude":2232.955294,
                        "longitude":11353.053698
                    },
                    "status":"normal"
                }
            }
        ],
        "total":6416
    },
    "desc":"success"
}
```


### 设备-详情-历史采集-查看告警图片

**简要描述**

- 设备的历史采集

- [没有告警视频的接口]

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview
**请求参数**


| 参数名   | 类型   | 说明      |
| ------   | ---    | -------- | 
| from     | string | 起始时间  | utc 时间戳
| until    | string | 终是时间  | utc 时间戳
| offset   | int    | 起始索引  |
| limit    | int    | 从起始索引开始，返回几个数据 |
| worker_id| string | 设备ID |

**返回参数**

| 参数名        | 类型    | 说明          | 补充                  |
| ------------- | ------ | ------------- | --------------------- |
| affirmed      | bool   | 告警是否被查看 | False 未被查看         |
| alert_source  | string | 告警来源       |                      |
| alert_type    | string | 告警类型      | 参考上文               |
| detect_result | dict   | AI检测结果    | 只需要将person用框框起来|
| host_id       | string | 告警设备ID    |
| img_url       | string | 图片地址      | 
| starttime     | int    | 告警事件      | 
| status        | string | 告警状态      | opening 和 closed     |
| update_time   | int    | 更新事件      | 例如: 告警的查看事件 或者 关闭事件| 

**返回**

200

```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```


### 设备-详情-告警记录

**简要描述**

- 告警记录

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview
**请求参数**


| 参数名   | 类型   | 说明      |
| ------   | ---    | -------- | 
| from     | string | 起始时间  | utc 时间戳
| until    | string | 终是时间  | utc 时间戳
| offset   | int    | 起始索引  |
| limit    | int    | 从起始索引开始，返回几个数据 |
| worker_id| string | 设备ID |

**返回参数**

| 参数名        | 类型    | 说明          | 补充                  |
| ------------- | ------ | ------------- | --------------------- |
| affirmed      | bool   | 告警是否被查看 | False 未被查看         |
| alert_source  | string | 告警来源       |                      |
| alert_type    | string | 告警类型      | 参考上文               |
| detect_result | dict   | AI检测结果    | 只需要将person用框框起来|
| host_id       | string | 告警设备ID    |
| img_url       | string | 图片地址      | 
| starttime     | int    | 告警事件      | 
| status        | string | 告警状态      | opening 和 closed     |
| update_time   | int    | 更新事件      | 例如: 告警的查看事件 或者 关闭事件| 

**返回**

200

```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```


### 设备-详情-查看告警

**简要描述**

- 设备的历史采集

**请求方式和请求URL**

- PUT

- https://edgeai.jiangxing.cn/api/v2/guard/alert/overview
**请求参数**


| 参数名| 类型   | 说明      |
| ------| ------| -------- | 
| id    |string | 告警的ID  |

**返回参数**

| 参数名        | 类型    | 说明          | 补充                  |
| ------------- | ------ | ------------- | --------------------- |
| affirmed      | bool   | 告警是否被查看 | False 未被查看         |
| alert_source  | string | 告警来源       |                      |
| alert_type    | string | 告警类型      | 参考上文               |
| detect_result | dict   | AI检测结果    | 只需要将person用框框起来|
| host_id       | string | 告警设备ID    |
| img_url       | string | 图片地址      | 
| starttime     | int    | 告警事件      | 
| status        | string | 告警状态      | opening 和 closed     |
| update_time   | int    | 更新事件      | 例如: 告警的查看事件 或者 关闭事件| 

**返回**

200

```json
{
    "data":{
        "data":[
            {
                "affirmed":false,
                "alert_source":"AI",
                "alert_type":"insulated_gloves",
                "detect_result":{
                    "person":[
                        {
                            "class":"person",
                            "prob":"0.298341641059",
                            "xmax":"1864",
                            "xmin":"1367",
                            "ymax":"777",
                            "ymin":"0"
                        }
                    ]
                },
                "host_id":"J018ec20df",
                "img_url":"media/104ecd7b-00d6-4bfc-bde4-2bca4d6fb75d/image/2019-12-27/05-43-02.jpg",
                "starttime":1577425389,
                "status":"opening",
                "update_time":1577425389
            }
            .....
        ],
        "total":1095
    },
    "desc":"success"
}
```


### 设备-详情-关闭告警

**简要描述**

- 查看工程的关闭告警接口



### 设备-地图

**简要描述**

- 设备地图

**请求方式和请求URL**

- PUT

- https://edgeai.jiangxing.cn/api/v2/guard/worker/map

**请求参数**


| 参数名        | 类型   | 说明     |
| ------        | ------| ------ | 
| engineering_id|string | 工程ID  |
| group_id      |string | 分组ID  |

**返回参数**

| 参数名       | 类型   | 说明       | 补充 |
| ------      | ------ | -----------|--- |
| name        | string | 设备名称    | 
| address     | string | 设备地址    | 
| worker_id   | string | 设备编号    | 
| position    | string | 设备的经纬度 | 
| group_worker_list| string | 设备分组 | 
| engineering| string | 当前所属工程信息 | 

**返回**

200

```json
{
    "data": [
        {
            "address": "广东省深圳市宝安区海天路",
            "engineering": {
                "id": "5e09a7c24e8424d82ae9c4bc",
                "name": "1234234",
                "starttime": 1577635200,
                "unit": "2342342"
            },
            "group_worker_list": [
                "测试分组"
            ],
            "name": "移动警卫兵-二次演示-2号机",
            "position": {
                "latitude": 2232.955294,
                "longitude": 11353.053698
            },
            "worker_id": "J018ec20df"
        }
    ],
    "desc": "success"
}
```


### 设备-地图-获取所有设备

**简要描述**

- 获取所有设备

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/worker/all


### 设备-地图-获取所有工程

**简要描述**

- 获取所有工程

**请求方式和请求URL**

- GET

- https://edgeai.jiangxing.cn/api/v2/guard/engineering/all

----

## 实体

### Engineering

工程

- `id`: string, 工程 ID
- `name`: string, 工程名
- `starttime`: 时间戳, 工程开始时间
- `status`: [`EngineeringStatus`](#EngineeringStatus), 工程状态
- total_alert_count, int,  工程告警总数
- unit, string, 施工单位(又名施工队)
- total_running_time: int, 总工程市场， 单位(秒)

### EngineeringStatus

工程状态，字符串枚举

- `"notstart"`:  未开始
- `"being"`:  正在施工
- `"finished"`: 已完成
- `"overdue"`: 已逾期

### Alert

告警

- id: string, 告警ID
- starttime: 时间戳, 告警时间
- affirmed: bool, 是否被查看, true被查看
- alert_source: [AlertSource](#AlertSource), 告警来源
- alert_type: AlertType, 告警类型
- detect_result: dict, AI检测结果
- host_id, string, 告警设备ID
- img_url, string, 图片地址
- status, [AlertStatus](#AlertStatus), 告警状态
- update_time，时间戳, 告警更新事件， 告警关闭时间

### AlertSource

告警来源，字符串枚举

- "AI": ai告警
- ”Super Administrator“, 手动告警用户

### AlertType

告警类型，字符串枚举， 不要写死, 使用请求获取

- "read_work_tickets": "未宣读工作票"

- "fence": "入侵电子围栏"
- "helmets": "未佩戴安全帽"
- "insulated_gloves": "未佩戴绝缘手套"
- "ground_rods": "未安装接地棒"
- "fire": "烟火"

### AlertStatus

告警状态，字符串枚举

- `"opening"`: 告警未关闭
- `"closed"`: 告警已关闭

### Cruise

巡航路径

- id: string, 巡航ID
- name, string, 巡航名称
- worker_id, string, 巡航的设备ID
- route, list, 巡航的具体信息
- route.id, string, 预置位的ID
- route.sleep_time, int, 在该点的停留时间

### Preset

预置点

- id: string, 预制点ID
- name, stirng, 预制点名称
- set_id, int, 预制点的实际位置
- worker_id, sting, 预制点的设备ID
- is_home, bool，是否是复位点

### User

用户

- id, string, 用户ID
- name, string, 用户名称
- password, string, 用户密码

- user_id, int, 用户编号
- role, [UserRole](#UserRole), 用户交色
- remark, string, 用户标签

### UserRole

- "admin": 系统管理员
- "viewer": 观察者
- "operator": 操作员

### Worker

设备

- id, string, 设备ID
- address, string, 设备地址
- name, string, 设备名称
- status, [WorkerStatus](#WorkerStatus)，设备状态
- elec_status, [WorkerStatus](#WorkerStatus),  电量状态
- flow_status, [WorkerStatus](#WorkerStatus), 流量状态
- card_status, [WorkerStatus](#WorkerStatus), SD状态

- position.longitude, 经度
- position.latitude, 纬度

### WorkerStatus

设备状态，字符串枚举

- `"normal"`: 正常
- `"abnormal"`: 异常
