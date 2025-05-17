#!/usr/bin/env python
#########################################################################
# File Name: xml_demo.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 17 May 2025 02:51:54 PM CST
#########################################################################

import xml.etree.ElementTree as ET
from xml.dom import minidom

def xml_demo():
    # 1. 创建根元素
    root = ET.Element("person", attrib={"id": "1001"})

    # 2. 添加子元素和属性
    name = ET.SubElement(root, "name")
    name.text = "Alice"
    
    age = ET.SubElement(root, "age")
    age.text = "30"

    address = ET.SubElement(root, "address", attrib={"city": "New York", "zip": "10001"})

    # 3. 添加数组等价结构
    hobbies = ET.SubElement(root, "hobbies")
    ET.SubElement(hobbies, "hobby").text = "coding"
    ET.SubElement(hobbies, "hobby").text = "reading"

    # 4. 添加嵌套复杂结构
    courses = ET.SubElement(root, "courses")
    course1 = ET.SubElement(courses, "course", attrib={"id": "1"})
    ET.SubElement(course1, "name").text = "Math"
    ET.SubElement(course1, "active").text = "true"

    # 5. 添加 CDATA 区块（修正部分）
    bio = ET.SubElement(root, "bio")
    bio.append(ET.Comment("这里是 CDATA 示例"))
    
    # 创建 DOM 文档并添加 CDATA
    dom = minidom.Document()
    cdata = dom.createCDATASection("This is <b>HTML</b> content!")
    
    # 将 ElementTree 转换为 minidom 节点以添加 CDATA
    xml_str = ET.tostring(root, encoding="utf-8")
    dom_root = minidom.parseString(xml_str).documentElement
    bio_dom = dom_root.getElementsByTagName("bio")[0]
    bio_dom.appendChild(cdata)

    # 6. 格式化并写入文件
    with open("demo.xml", "w", encoding="utf-8") as f:
        f.write(dom_root.toprettyxml(indent="  "))
    print("✅ XML 文件写入完成！")

    # 7. 读取和解析 XML
    try:
        tree = ET.parse("demo.xml")
        root = tree.getroot()

        print("\n🔍 读取整个文件:")
        print(minidom.parseString(ET.tostring(root)).toprettyxml())

        # 8. XPath 查询
        print("\n🔍 XPath 查询结果:")
        for course in root.findall(".//course"):
            print(f"课程ID: {course.get('id')}, 名称: {course.find('name').text}")

        # 9. 修改数据
        root.find("age").text = "31"
        new_course = ET.SubElement(root.find("courses"), "course", attrib={"id": "3"})
        ET.SubElement(new_course, "name").text = "Physics"

        # 10. 删除节点
        for hobby in root.find("hobbies").findall("hobby"):
            if hobby.text == "reading":
                root.find("hobbies").remove(hobby)

        # 11. 写回文件
        tree.write("demo_updated.xml", encoding="utf-8", xml_declaration=True)
        print("\n🔄 修改后的文件已保存为 demo_updated.xml")

    except FileNotFoundError:
        print("❌ 文件不存在！")
    except ET.ParseError:
        print("❌ XML 解析错误！")

if __name__ == "__main__":
    xml_demo()
