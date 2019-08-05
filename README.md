## 看酷安

**前言：爬取的所有数据都是在用户主页公开显示的，为避免对酷安服务器造成压力，主要在夜间延时爬取**



刷B站的时候经常能看到B站各种排行及分布，也有好几个专门监测B站的网站比如 https://www.kanbilibili.com/ , www.biliob.com 等,这都是许多爬虫在不停地工作。

此时我寻思着每天刷酷安的次数也不比B站少啊，然后就有了这个简单的统计。

**爬取的原理：**

  对于酷安来说，每位用户都有一个uid，这个uid应该是随着注册时间递增的，所以粗暴的方法就是从起始uid开始遍历到最后。但是同所有社区一样，每个社区都有大量0关注0粉丝的 *僵尸号* ，爬取这样的用户是没有意义的且浪费资源的。此外，如果社区的用户id不是规律递增的或者是根据用户名确定的url（如知乎），那么此爬取方式将不可行。

  **所以采用如下方法：**

  每一位用户都有其关注列表和粉丝列表，所以从一位酷安大V开始，获取其关注和粉丝列表，然后对列表中每一位用户执行相同的操作，然后再对相同的url进行去重防止重复爬取，但是那么理论上是可以将所有关注及粉丝非0的用户获取到的。ps:我在酷安随机抽取了一些用户查询，未发现遗漏

![原理](https://raw.githubusercontent.com/amchii/CoolApk/master/coolapk/cool.gif)

爬取的数据如下：

- 地区分布
  - [省份分布](https://amchii.github.io/CoolApk/coolapk/province/)
- 性别分布
  - [性别分布](https://amchii.github.io/CoolApk/coolapk/gender)
  - [性别占比随地区](https://amchii.github.io/CoolApk/coolapk/gender/gender_by_province/)
- 等级分布及排行
  - [等级分布](https://amchii.github.io/CoolApk/coolapk/level/)
  - [top1-25](https://amchii.github.io/CoolApk/coolapk/level/top100/top1-25/)
  - [top26-50](https://amchii.github.io/CoolApk/coolapk/level/top100/top26-50/)
  - [top51-100](https://amchii.github.io/CoolApk/coolapk/level/top100/top51-100/)
  - [top100_CSV](https://github.com/amchii/CoolApk/blob/master/coolapk/level/top100/top100.csv)
- 粉丝排行
  - [粉丝排行](https://amchii.github.io/CoolApk/coolapk/fans/)
- 开发应用数量top250
  - [CSV](https://github.com/amchii/CoolApk/blob/master/coolapk/developer/developer.csv)
- 动态数top100
  - [CSV](https://github.com/amchii/CoolApk/blob/master/coolapk/feed/feed_top100.csv)