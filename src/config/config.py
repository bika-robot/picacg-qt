BaseUrl = "http://68.183.234.72/"            # 获得ip列表接口
Url = "https://picaapi.picacomic.com/"       # 域名
ApiKey = "C69BAF41DA5ABD1FFEDC6D2FEA56B"     # apiKey
AppChannel = "3"
Version = "2.2.1.3.3.4"                      # 版本号
BuildVersion = "45"
Accept = "application/vnd.picacomic.com.v1+json"
Agent = "okhttp/3.8.1"
Platform = "android"
ImageQuality = "original"      # 画质，original, low, medium, high
Uuid = "defaultUuid"


ThreadNum = 10                 # 线程
DownloadThreadNum = 5          # 下载线程
ChatSavePath = "chat"
SavePathDir = "commies"        # 下载目录
ResetCnt = 5                   # 下载重试次数

IsUseCache = True              # 是否使用cache
CachePathDir = "cache"         # cache目录
# CacheExpired = 24 * 60 * 60  # cache过期时间24小时
PreLoading = 10                # 预加载5页
PreLook = 4                    # 预显示

IsLoadingPicture = True

UpdateUrl = "https://github.com/tonquer/picacg-qt/releases/latest"
UpdateUrlBack = "https://hub.fastgit.org/tonquer/picacg-qt/releases/latest"
UpdateUrl2 = "https://github.com/tonquer/picacg-qt/releases"
UpdateUrl2Back = "https://hub.fastgit.org/tonquer/picacg-qt/releases"

DatabaseUpdate = "https://raw.githubusercontent.com/bika-robot/picacg-database/main/version.txt"
DatabaseDownload = "https://raw.githubusercontent.com/bika-robot/picacg-database/main/data/"

DatabaseUpdate2 = "https://gitee.com/bika-robot/picacg-database/raw/main/version.txt"
DatabaseDownload2 = "https://gitee.com/bika-robot/picacg-database/raw/main/data/"
UpdateVersion = "v1.2.8"

# waifu2x
CanWaifu2x = True
ErrorMsg = ""

Encode = 0             # 当前正在使用的索引
EncodeGpu = ""

Format = "jpg"
Waifu2xPath = "waifu2x"

ThemeText = "dark"  # 主题
ThemeIndex = 0  # 主题·
CurrentSetTheme = 0

IsTips = 1

# ISSUES
Issues = "https://github.com/tonquer/picacg-qt/issues"

# 代理与分流相关
ProxyUrl = "https://github.com/tonquer/picacg-qt/discussions/48"

# Waifu2x相关
Waifu2xUrl = "https://github.com/tonquer/picacg-qt/discussions/76"

Address = ['104.20.180.50', '104.20.181.50']  # 分类2，3 Ip列表
ImageServer = 'storage.wikawika.xyz'          # 分流2，3 使用的图片服务器

ApiDomain = [
    "picaapi.picacomic.com",
]

ImageDomain = [
    "storage.wikawika.xyz",
    "storage1.picacomic.com",
    "img.tipatipa.xyz",
    "img.picacomic.com",
    "pica-pica.wikawika.xyz",
    "www.picacomic.com"
]