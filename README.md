# HoshinoBot (customized)

HoshinoBot的个人修改版。安装和部署指南请移步[原项目地址](https://github.com/Ice-Cirno/HoshinoBot)。

本项目**不提供**资源文件。

## 简介

本项目对原版机器人进行了少许修改。**这些修改可能导致与原版机器人部分功能不兼容**。修改包括：

- 在[语料库](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/groupmaster/chat.py)中加入更多应答；
- 在[资源库接口](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/R.py)中添加ResRec类以处理语音；
- 在[广播](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/botmanage/broadcast.py)中添加“单个群发消息”功能；
- 修改[每日签到](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/priconne/login_bonus.py)访问印章图片的位置，支持印章图片集的热更新；加入重置签到情况的功能；
- 在[反滥用](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/groupmaster/anti_abuse.py)中加入临时屏蔽指定群消息（和解除该屏蔽）的功能；
- 出于搞笑效果，增加[角色数据库](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/hoshino/modules/priconne/_pcr_data.py)中内容；**注意**：卡池信息及额外的资源文件并未上传；
- 等等

## 开源

本项目按GPL-v3协议开源。您可以任意复制、使用、修改、署名该作品及衍生作品，但若要向非开发者分发这些作品，则需要以GPL-v3协议开源。详情请阅读[开源协议](https://github.com/iamwyh2019/custom-HoshinoBot/blob/master/LICENSE)。

## 部署

本项目代码与使用中的机器人代码实时同步更新，但出于安全原因，所有配置文件都不会公开。这可能导致部署困难。因此，我们建议您**不直接使用**本项目代码，而是访问[原项目地址](https://github.com/Ice-Cirno/HoshinoBot)进行部署。

## 更新

目前的更新方向是将原项目中重要的且被写死的参数改成变量，增加修改接口，以实现参数热更新。现在可热更新的参数有：

- 重置每日签到情况
- 更新印章库里的印章列表
- 设置查询拆法时显示的最大作业数

除此之外，还会尝试增加新的查询功能，例如查询角色站位和技能循环。目前未实现。