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
 ## 界面介绍
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/6ba3f788286c4eef826c8f6581cc9066.png)
 
 ### 查看数据包视图
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/3787884b9d284bbd88587077bc1fe0df.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/d864933068194ba6ae619a601887f019.png)
### 会话右键支持功能
#### 基础功能
![在这里插入图片描述](https://img-blog.csdnimg.cn/f11d4fd3cc3249c28f5bf9f88757f0ab.png)
#### Find in
![在这里插入图片描述](https://img-blog.csdnimg.cn/0c6dd3d85a4c46f49f9cf8143534865c.png)
#### 重复发起请求
![在这里插入图片描述](https://img-blog.csdnimg.cn/8617b233129d4fae8a722d9117b46d01.png)
#### Focus
Focus对应的便是Ignore，选中Ignore后，便不再展示响应的请求
![在这里插入图片描述](https://img-blog.csdnimg.cn/101e7a876674454d9813c4ca170ac212.png)
#### Clear
和`Clear Others`相反，Clear清除的是当前选中的请求，Clear Others清除的是除当前选中的以外所有请求
#### Breakpoints
断点调试，分为请求前断点，和响应前断点，需要在`Breakponit Settings`当中提前设置，下文有详细介绍，右键菜单栏中仅为开启或者关闭断点调试
#### No caching
禁用缓存，右键菜单栏仅为开启或者关闭，需要在`Tools-No caching`中去设置禁用缓存的具体地址
![在这里插入图片描述](https://img-blog.csdnimg.cn/4cbc29181aa8459793b9457bbccb5c71.png)
#### Block Cookies
禁用Cookies认证，右键菜单栏仅为开启或者关闭认证，详情需要在`Tools-Block Cookies`中去设置
原理为：
 - Cookie头部从请求中删除，防止将cookie值从客户端应用程序(例如Web浏览器)发送到远程服务器。
- Set-Cookie头将从响应中移除，从而防止客户端应用程序从远程服务器接收cookie的请求。
![在这里插入图片描述](https://img-blog.csdnimg.cn/3e1b42c9a5604017919db5cf05e9ad42.png)
#### Block List
将域名设置为黑名单，无法联网，详细可以在`Tools-Block List`中设置
![在这里插入图片描述](https://img-blog.csdnimg.cn/d98f95bf3a9e4a7cadde8dd14cdeff0c.png)
#### Allow List
和`Block List`相反，是仅允许选中的域名为白名单，其余域名的请求都会被拒绝
![在这里插入图片描述](https://img-blog.csdnimg.cn/9f038b72a0634bef951dd36960630716.png)
#### Client Process
客户端进程工具显示负责进行每个请求的本地客户端进程的名称，相当于监控本地发出的请求，都会被监控到，每个链接之前都会有一个短暂的延迟，需要在`Tools-Client Process`中设置对应的域名
#### Map Remote
重定向到另一个请求的返回值当作自己的返回值，可以在Session上右键Map Remote设定规则，或`Tools-->Map Remote`来管理所有的`Map Remote`
![](https://img-blog.csdnimg.cn/5c7161cdddb34d9eb0cb22c3a2ead3b5.png)
#### Map Local
 使用本地的一个文件的内容作为返回值 可以在Session上右键Map Local设定规则，或Tools-->Map Local管理所有的Map Local
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/c8af0d665a8142abbc3101672ffb340d.png)








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
### Reverse Proxies
 - 正向代理：帮助客户端进行发送请求，接收响应，代理端是客户端，正常使用Charles进行抓包
 - 反向代理：帮助服务器发送请求，接收响应，代理端是服务器，多用于请求发送到多台服务器的负载均衡
 - 设置：Local Port 本地端口，会随机生成一个可用的端口号，在此端口上进行反向代理
   
	 - Remote host/Remote port 作为代理目的地的远程主机和端口号，默认为HTTP的端口号80
	- Rewrite redirects：重写重定向，将客户端重定向到远程服务器的地址，重写为由客户端将响应信息直接发送给反向代理的本地地址，如果不选择，则重定向后的响应会直接发送给远程服务器，Charles将抓取不到响应信息
	- Preserve host in header fields：保留主机头
	- Listen on a specific address：监听特定的地址
![在这里插入图片描述](https://img-blog.csdnimg.cn/1453fb63e1b24f1a9cca05aadd5d0869.png)
### Port Forwarding
端口转发是转发一个网络端口从一个网络节点到另一个网络节点的行为，其使一个外部用户从外部经过一个被激活的NAT路由器到达一个在私有内部IP地址（局域网内部）上的一个端口![在这里插入图片描述](https://img-blog.csdnimg.cn/307c82c5e3f14db98c93e1e34597e3f8.png)
### Proxy Settings
设置代理端口
![在这里插入图片描述](https://img-blog.csdnimg.cn/07de7233c5ca4e1cbc23e7f14b5932a8.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/ca33440a48c347c0bd697d65226a3743.png)
### DNS Settings
通过将您自己的主机名指定给远程地址映射来欺骗DNS查找
引用：一般的开发流程中，在上线之前都需要在测试环境中先行进行验证，而此时手机客户端请求的域名是不太容易改变的，可以通过设置dns方式把域名转发到测试机上，具体设置`Tools->DNS Spoofing Settings`
官方文档上的介绍：
- 当请求通过Charles时，您的DNS映射将优先。
- 在DNS更改之前，DNS Spoofing可用于测试虚拟托管网站，因为您的浏览器将会像DNS更改一样运行。
- DNS更改通常需要长达24小时才能生效，并且没有DNS欺骗，DNS变更生效后，网站将会变得非常困难。
- 可以将主机名映射到IP地址或另一个主机名，这些名称将由Charles在DNS中查找以查找其IP地址
![在这里插入图片描述](https://img-blog.csdnimg.cn/fa5657259c10494a9eb839432709906c.png)
### Access Control Settings
- 访问账户设置，限制访问Charles的请求，本地默认可直接访问
- `Prompt to alow unauthorized connections`：勾选该设置，则未在列表中的ip访问Charles时，charles会弹出是否允许访问的提示信息，不勾选，则不会弹框提示，将直接屏蔽除列表内的ip访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/c3351a372cd34adea79c4c3a6782c81d.png)
### External Proxy Settings
用于需要使用网络上的代理服务器访问网络的场景，比如通过VPN访问外网，如果在一台服务器上同时打开VPN和Charles，Charles是无法生效的，此时需要配置该处
Web Proxy Server 设置VPN的Host和Port
Proxy server requires a password：配置身份验证和外部代理请求认证，如果没有配置，则Charles直接向服务器发送验证请求
Bypass external proxies for the following hosts：设置绕过外部代理直接进行请求的hosts
### Web Interface Settings
`Web Interface Settings` 表示 Web 界面设置。Charles 有一个 Web 界面，可以让您从浏览器控制 Charles，或使用 Web 界面作为 Web 服务使用外部程序，在 `External Proxy Settings` 视图中勾选 `Enable the web interface` 选项启用 Web 界面。可以允许匿名访问，也可以配置用户名和密码,可以访问[http://control.charles](http://control.charles)的Web界面，当查询运行时，您可以启用此功能并配置下面的访问控制；
![在这里插入图片描述](https://img-blog.csdnimg.cn/8f45ebb7959443b08ac68c08b4ad903a.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/72a4253f35504e02ae87ee158539280f.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/9b3c9e94460a496f8c6c26ac36efe008.png)
## Tools工具
![在这里插入图片描述](https://img-blog.csdnimg.cn/bd9d66aa860c42c2b4ca3f909ce6fe9a.png)
#### No caching Settings：无缓存设置
- 通过操纵控制缓存响应的HTTP头来防止缓存;只选择`Enable No Caching`，则禁止缓存所有，同时
- 选择Enable No Caching和`Only for selected locations`，则只禁止缓存列表中的请求Header
- 从请求中删除If-Modified-Since和If-None-Match头，添加Pragma：no-cache和Cache-control：no-cache。
- 从响应中删除Expires，Last-Modified和ETag标头，添加Expires：0和Cache-Control: no-cache
![在这里插入图片描述](https://img-blog.csdnimg.cn/da5c8edbe5974491b99e597b0db34661.png)
#### Rewrite重写工具，修改请求和响应的rule
访问所有[http://www.baidu.com](http://www.baidu.com)成功的接口，原本返回的status为200，目前通过重写返回的status，导致访问成功的status由200变成了401
![在这里插入图片描述](https://img-blog.csdnimg.cn/38ef77b4130f4aeb8ed9164e48baead7.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/9651df5544654b02afc56c25d2442842.png)
#### Mirror 镜像工具
访问指定请求时，将抓取到的文件克隆一份，并保存在指定目录下适合抓取少量文件，且只存储该文件下的资源，不会存储该文件引用的外部文件，传送到客户端的压缩或者编码的响应会被解码
![在这里插入图片描述](https://img-blog.csdnimg.cn/4f1069a35744483ea95a22da265471c3.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/9c325643ca2741cf948eceba25ef1cf1.png)
#### Auto Save：自动存储
设定时间间隔后，自动保存并清除抓取到的内容，适用于离开Charles监视长时间的网络活动，第一个保存间隔将缩短以满足自然小时内可间隔数为整数，比如您在10:02设置的间隔时间为5min，则第一次自动保存并清除抓取到的内容的时间为10:05，之后每隔5min保存并清除一次
![在这里插入图片描述](https://img-blog.csdnimg.cn/cb4194af4e204326a2f12bf3c2105fab.png)
#### Publish Gist Settings：Gist发布设置
可设置自己GitHub的账号，若是没有设置，则发布的代码段将会已匿名形式发布出去，并且无法进行删除；可设置发布的代码段的大小以及发布的形式是公开还是私密，推送后会在[https://gist.github.com/](https://gist.github.com/)查询到
![在这里插入图片描述](https://img-blog.csdnimg.cn/a92519e3ce734723a9f533a99aa21a01.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/29c4ca55324744e4ab3249c7ad3b54ff.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/de9b28b9b5c041459fdf73ae289d79c3.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/8674f2eef0ca44afabc1687f059a2aba.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/cf51bda19b864514aef916b313a20307.png)
### Windows
![在这里插入图片描述](https://img-blog.csdnimg.cn/f9e33e9cf0434ba4bdd35caca6ee16a3.png)
### Help
![在这里插入图片描述](https://img-blog.csdnimg.cn/f5fb96e233fc436e8b596625c2c7ec5c.png)
## 代理设置
### Windows代理设置
Charles默认代理本地服务器，如果抓取不到本地服务器，查看浏览器是否开启代理本地默认代理设置时是这样的(针对Google)：地址 `http=127.0.0.1:8888`;`https=127.0.0.1:8888`



