# clanbattleretire

这是一个使用hoshino自带的clanbattle v2的数据生成离职报告和会战报告的hoshino插件。

注意：本插件会读取clanbattlev2插件的数据库，因程序故障导致数据损坏的一切责任不由开发者承担。

## 安装说明：

此插件适用于hoshino V2。安装步骤如下：

- 将clanbattleretire文件夹放入modules文件夹中
- 在```config/__bot__.py```的模块列表里加入clanbattleretire
- 根据目录下的requirements.txt安装依赖。依赖包括：sqlite3, pandas, numpy, matplotlib
- 重启hoshino

## 使用方法：

- [离职报告]：生成一张离职报告
- [会战报告]：生成一张本期会战报告

每次生成报告后有30分钟的冷却时间，可以在__init__.py中调整。

不同服务器上显示效果可能有细微不同，请尝试微调__init__.py里的坐标参数。

## 鸣谢

- 倚栏待月——基础代码编写
- 明见——背景图片与字体提供
- qq3193377836
- 魔法の書——增强显示效果

## 开源

本插件以GPL-v3协议开源。