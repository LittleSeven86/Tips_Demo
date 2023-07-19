# Charles使用教程

## 简介
Charles是一个HTTP代理服务器,HTTP监视器,反转代理服务器，当浏览器连接Charles的代理访问互联网时，Charles可以监控浏览器发送和接收的所有数据。它允许一个开发者查看所有连接互联网的HTTP通信，这些包括request, response和HTTP headers （包含cookies与caching信息）

## 主要功能
- 支持SSL代理。可以截取分析SSL的请求。
- 支持流量控制。可以模拟慢速网络以及等待时间（latency）较长的请求。
- 支持AJAX调试。可以自动将json或xml数据格式化，方便查看。
- 支持AMF调试。可以将Flash Remoting 或 Flex Remoting信息格式化，方便查看。
- 支持重发网络请求，方便后端调试。
- 支持修改网络请求参数。
- 支持网络请求的截获并动态修改。
- 检查HTML，CSS和RSS内容是否符合W3C标准。

## 官方网站
官网地址：[https://www.charlesproxy.com/](https://www.charlesproxy.com/)
![Charles官网](https://img-blog.csdnimg.cn/112a40f8898846f2ae9574e3d8b328f6.png)
## Mac安装步骤

 - 从官网下载对应的安装包后，直接点击安装即可
 ![Charles安装步骤](https://img-blog.csdnimg.cn/e97ef44cedcc4d34980f0e6b6167d343.png)
## 注册

```python
 Name: https://zhile.io； 
 Key: 48891cf209c6d32bf4
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/4652a369b1cd48daacdb128b414e1d20.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/61468d97cebc46c9ac6ae8dcbf96bde3.png)
## 安装证书
 - 在`SSL Proxying`中点击` Install Charles Root Certificate`安装证书
![在这里插入图片描述](https://img-blog.csdnimg.cn/6e4806215e6949c6be1acc92d9e3e9f3.png)
 - 刚安装的Charles Root Certificate会在证书管理器中显示但尚未被信任，此时需要手动设为信任
![在这里插入图片描述](https://img-blog.csdnimg.cn/be02bbf0881143cbbd6ff2f41574df1b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/5c3661d87c6d4d41bb4a781c44ab5ccb.png)
 - 授权以后就会在证书显示此证书为受此账户信任 ![在这里插入图片描述](https://img-blog.csdnimg.cn/f531756a682b41e2b01f9fe54b081e75.png)
## Proxy菜单设置
![在这里插入图片描述](https://img-blog.csdnimg.cn/1a32ae0f7d0e4ed2ab28f81acb127a1e.png)
### Recording Settings
`Recording Settings `和 `Start/Stop Recording `配合使用，在`Start Recording` 的状态下，可以通过 `Recording Settings` 配置 Charles 的会话记录行为，界面有三个选项卡：
 - Option：通过 Recording Size Limits 限制记录数据的大小。当 Charles 记录时，请求、响应头和响应体存储在内存中，或写入磁盘上的临时文件。有时，内存中的数据量可能会变得太多，Charles 会通知您并停止录制。在这种情况下，您应该清除 Charles 会话以释放内存，然后再次开始录制。在录制设置中，您可以限制 Charles 将记录的最大大小; 这根本不会影响你的浏览，Charles 仅会停止录制
 - Include：只有与配置的地址匹配的请求才会被录制。
 - Exclude：只有与配置的地址匹配的请求不会被录制。
 - Include 和 Exclude 选项卡的操作相同，选择 Add，然后填入需要监控的Procotol、Host 和 Port等信息，这样就达到了过滤的目的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/179062cc05dc4a679e7439a305e03f79.png)
### Throttle Settings
`Throttle Settings `和 `Start/Stop Throttling` 配合使用，在 `Start Throttling` 的状态下，可以通过 `Throttle Settings` 配置 Charles 的网速模拟配置。`Throttle Settings` 的视图如下图所示：![在这里插入图片描述](https://img-blog.csdnimg.cn/63c208356d8c4446a6183405e32c6637.png)
### Breakpoint Settings
`Breakpoint Settings` 和 `Enable/Disable Breakpoints` 配合使用，在 `Enable Breakpoints `的状态下，可以通过 `Breakpoint Settings `配置 Charles 的断点模式。`Breakpoint Settings `的视图如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/19f397fba5b54d498e423202741e2485.png#pic_center)
### Web Interface Settings
`Web Interface Settings` 表示 Web 界面设置。Charles 有一个 Web 界面，可以让您从浏览器控制 Charles，或使用 Web 界面作为 Web 服务使用外部程序，在 `External Proxy Settings` 视图中勾选 `Enable the web interface` 选项启用 Web 界面。可以允许匿名访问，也可以配置用户名和密码。
在这里插入图片描述
https://zhuanlan.zhihu.com/p/581082996