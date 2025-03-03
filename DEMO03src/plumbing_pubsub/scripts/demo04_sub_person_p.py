#! /usr/bin/env python
import rospy
from plumbing_pubsub.msg import Person
"""
   订阅方：订阅人的消息
      1.导包;
      2.初始化ROS节点;
      3.创建订阅者对象;
      4.处理订阅的数据;
      5.spin()。

"""
def doPerson(p):
    rospy.loginfo("小伙子的数据:%s,%d,%.2f",p.name,p.age,p.height)

if __name__=="__main__":
    #2.初始化ROS节点;
    rospy.init_node("daYe")
    #3.创建订阅者对象;
    sub = rospy.Subscriber("jiaoSheTou",Person,doPerson)
    #4.处理订阅的数据;
    #5.spin()。
    rospy.spin()
 
    pass 