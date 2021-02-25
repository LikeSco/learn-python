from jinja2 import PackageLoader, Environment, FileSystemLoader
from os import path
import json

readFile = "db.json"
writeFile = "myPage.html"

currentDir = path.dirname(__file__)
resourcePath = path.join(currentDir, readFile)
outputPath = path.join(currentDir, writeFile)

with open(resourcePath, "r", encoding='utf_8_sig') as readfs:
    val = readfs.read()
    readfs.close()
tasks = json.loads(val)

# 创建一个加载器, jinja2 会从这个目录中加载模板
loader = FileSystemLoader(currentDir)

# # 用加载器创建一个环境, 有了它才能读取模板文件
env = Environment(loader=loader)
# # 获取一个模板文件
template = env.get_template('myTemplate.html')
my_html = template.render(yqms=tasks)  # 渲染

with open(outputPath, "w", encoding="utf-8") as write_fs:
    write_fs.write(my_html)
    write_fs.close()
