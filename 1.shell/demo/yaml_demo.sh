#!/usr/bin/env bash
#########################################################################
# File Name: yaml_demo.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 17 May 2025 04:34:46 PM CST
#########################################################################

# 示例文件路径
YAML_FILE="demo.yaml"

echo "===== YAML 示例 ====="

# 1. 创建并写入 YAML 文件
cat <<EOF > $YAML_FILE
name: Alice
age: 30
isStudent: false
address:
  city: New York
  zip: "10001"
hobbies:
  - coding
  - reading
courses:
  - id: 1
    name: Math
  - id: 2
    name: History
EOF
echo "✅ 创建 YAML 文件完成！"

# 2. 读取整个文件
echo -e "\n🔍 读取整个文件:"
yq . $YAML_FILE

# 3. 读取特定字段
echo -e "\n🔍 读取特定字段:"
echo "名字: $(yq '.name' $YAML_FILE)"
echo "城市: $(yq '.address.city' $YAML_FILE)"
echo "第一个爱好: $(yq '.hobbies[0]' $YAML_FILE)"

# 4. 修改字段
echo -e "\n✏️ 修改字段（年龄改为 31）:"
yq -i '.age = 31' $YAML_FILE
yq '.age' $YAML_FILE

# 5. 添加字段
echo -e "\n➕ 添加字段（国家）:"
yq -i '.country = "USA"' $YAML_FILE
yq '.country' $YAML_FILE

# 6. 删除字段
echo -e "\n❌ 删除字段（isStudent）:"
yq -i 'del(.isStudent)' $YAML_FILE
yq . $YAML_FILE

# 7. 遍历数组
echo -e "\n🔄 遍历课程列表:"
yq -o=json '.courses[]' $YAML_FILE | jq -r '"课程ID: \(.id), 名称: \(.name)"'

