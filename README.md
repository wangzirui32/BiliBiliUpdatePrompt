# BiliBili UP主更新提示器
<p>
<img src="https://img.shields.io/static/v1?label=Project&message=BiliBili Update Prompt&color"/>
<img src="https://img.shields.io/static/v1?label=Program&message=Python&color=blue"/>
<img src="https://img.shields.io/static/v1?label=Python&message=3.9.5&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=Version&message=1.0.0&color=red"/>
</p>
这个项目可以帮助你监控UP主的更新情况，可以下载`out\app.dist\app.zip`，运行其中的`app.exe`，也可以下载源码并用`pip`安装依赖包，运行app.py。
在`config.json`中可以自定义配置，内容如下：

```json
{
 "user_id": "1513364019", 
 "interval": "10", 
 "pop_up_prompt": true
}
```
参数解释：
```
user_id: UP主id
interval: 设置每隔几秒检查一次更新，建议不要低于5秒
pop_up_prompt: 更新时是否弹窗提示
```
目前项目处于测试阶段，后续会持续改进并优化exe编译。