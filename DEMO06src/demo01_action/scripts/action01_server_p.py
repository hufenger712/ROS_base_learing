#! /usr/bin/env python
import rospy
import actionlib
from demo01_action.msg import *

"""
    需求:
        创建两个ROS 节点，服务器和客户端，
        客户端可以向服务器发送目标数据N(一个整型数据)服务器会计算 1 到 N 之间所有整数的和,
        这是一个循环累加的过程，返回给客户端，这是基于请求响应模式的，
        又已知服务器从接收到请求到产生响应是一个耗时操作,每累加一次耗时0.1s,
        为了良好的用户体验，需要服务器在计算过程中，
        每累加一次，就给客户端响应一次百分比格式的执行进度，使用 action实现。

    流程：
        1.导包；
        2.初始化ROS节点;
        3.单独封装一个类;
        4.类中创建 action 服务端对象；
        5.处理请求(a.解析目标值;b.发送连续反馈;c.响应最终结果)--回调函数;
        6.spin()回旋。

"""

# 4.类中创建 action 服务端对象；
# 5.处理请求(a.解析目标值;b.发送连续反馈;c.响应最终结果)--回调函数;
class MyAction:

    def __init__(self):
        # SimpleActionServer(name: Any, ActionSpec: Any, execute_cb: Any | None = None, auto_start: bool = True)
        self.server = actionlib.SimpleActionServer("addInts",AddIntsAction,self.cb,False)
        self.server.start()
        rospy.loginfo("服务端启动......")

    #回调函数
    #参数：目标值

    def cb(self,goal):
        # a.解析目标值;
        goal_num = goal.num
        rospy.loginfo("目标值：%d",goal_num)
        # b.发送连续反馈;
        rate = rospy.Rate(10)
        sum = 0  #接受求和结果变量
        rospy.loginfo("请求处理中.......")
        for i in range(1,goal_num+1):
            sum = sum + i
            rate.sleep()
            #发送连续反馈
            fb_obj = AddIntsFeedback()
            fb_obj.progress_bar = i/goal_num
            self.server.publish_feedback(fb_obj)
        # c.响应最终结果
        rospy.loginfo("响应最终结果：%d",sum)

        result = AddIntsResult()
        result.result = sum
        self.server.set_succeeded(result)


if __name__ == "__main__":
    # 2.初始化ROS节点;
    rospy.init_node("action_server_p")
    # 3.单独封装一个类;
    myaction = MyAction()
    # 6.spin()回旋。
    rospy.spin()
    pass