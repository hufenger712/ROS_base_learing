#! /usr/bin/env python

# 现象：当不配置 CMakeLists.txt 执行 python 文件抛出异常：
#/usr/bin/env: “python”: 没有那个文件或目录
#原因：当前 noetic 使用的是python3
#解决：
#    1.直接声明解释器为python3(不建议)
#    2.通过软连接将 python 链接到 python3(建议)：sudo ln -s /usr/bin/python3 /usr/bin/python3 (建议)

#导包
import rospy 
#入口
if __name__=="__main__":
    #初始化ros节点
    rospy.init_node("hello_p2")
    #输出日志
    rospy.loginfo("hello vscode! 这是python!2222222")
    