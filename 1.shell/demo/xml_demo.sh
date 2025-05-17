#!/usr/bin/env bash
#########################################################################
# File Name: xml_demo.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 17 May 2025 02:26:38 PM CST
#########################################################################

# 示例文件路径
XML_FILE="demo.xml"

echo "===== XML 示例 ====="

# 1. 创建并写入 XML 文件
cat <<EOF > $XML_FILE
<person>
  <name>Alice</name>
  <age>30</age>
  <isStudent>false</isStudent>
  <address city="New York" zip="10001"/>
  <hobbies>
    <hobby>coding</hobby>
    <hobby>reading</hobby>
  </hobbies>
  <courses>
    <course id="1">
      <name>Math</name>
    </course>
    <course id="2">
      <name>History</name>
    </course>
  </courses>
</person>
EOF
echo "✅ 创建 XML 文件完成！"

# 2. 读取整个文件（格式化）
echo -e "\n🔍 读取整个文件:"
xmlstarlet fo --indent-spaces 2 $XML_FILE || {
    echo "格式化失败，原始内容："
    cat $XML_FILE
}

# 3. 读取特定节点文本
echo -e "\n🔍 读取特定节点文本:"
echo "名字: $(xmlstarlet sel -t -v "/person/name" $XML_FILE)"
echo "城市属性: $(xmlstarlet sel -t -v "/person/address/@city" $XML_FILE)"

# 4. 修改节点文本
echo -e "\n✏️ 修改节点文本（年龄改为 31）:"
xmlstarlet ed -L -u "/person/age" -v "31" $XML_FILE
xmlstarlet sel -t -v "/person/age" $XML_FILE

# 5. 修改属性
echo -e "\n✏️ 修改属性（zip 改为 10002）:"
xmlstarlet ed -L -u "/person/address/@zip" -v "10002" $XML_FILE
xmlstarlet sel -t -v "/person/address/@zip" $XML_FILE

# 6. 添加新节点
echo -e "\n➕ 添加节点（国家）:"
xmlstarlet ed -L -s "/person" -t elem -n "country" -v "USA" $XML_FILE
xmlstarlet sel -t -v "/person/country" $XML_FILE

# 7. 删除节点
echo -e "\n❌ 删除节点（isStudent）:"
xmlstarlet ed -L -d "/person/isStudent" $XML_FILE
echo "删除后文件内容："
xmlstarlet fo --indent-spaces 2 $XML_FILE || cat $XML_FILE

# 8. XPath 查询（遍历课程）
echo -e "\n🔄 遍历课程列表:"
xmlstarlet sel -t -m "/person/courses/course" -v "concat('课程ID: ', @id, ', 名称: ', name)" -n $XML_FILE
