#!/usr/bin/env bash
#########################################################################
# File Name: json_demo.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 17 May 2025 02:25:53 PM CST
#########################################################################

# 示例文件路径
JSON_FILE="demo.json"

echo "===== JSON 示例 ====="

# 1. 创建并写入 JSON 文件
cat <<EOF > $JSON_FILE
{
  "name": "Alice",
  "age": 30,
  "isStudent": false,
  "address": {
    "city": "New York",
    "zip": "10001"
  },
  "hobbies": ["coding", "reading"],
  "courses": [
    {"id": 1, "name": "Math"},
    {"id": 2, "name": "History"}
  ]
}
EOF
echo "✅ 创建 JSON 文件完成！"

# 2. 读取整个文件
echo -e "\n🔍 读取整个文件:"
jq '.' $JSON_FILE

# 3. 读取特定字段
echo -e "\n🔍 读取特定字段:"
echo "名字: $(jq -r '.name' $JSON_FILE)"
echo "城市: $(jq -r '.address.city' $JSON_FILE)"
echo "第一个爱好: $(jq -r '.hobbies[0]' $JSON_FILE)"

# 4. 修改字段
echo -e "\n✏️ 修改字段（年龄改为 31）:"
jq '.age = 31' $JSON_FILE > tmp.json && mv tmp.json $JSON_FILE
jq '.age' $JSON_FILE

# 5. 添加字段
echo -e "\n➕ 添加字段（国家）:"
jq '.country = "USA"' $JSON_FILE > tmp.json && mv tmp.json $JSON_FILE
jq '.country' $JSON_FILE

# 6. 删除字段
echo -e "\n❌ 删除字段（isStudent）:"
jq 'del(.isStudent)' $JSON_FILE > tmp.json && mv tmp.json $JSON_FILE
jq '.' $JSON_FILE

# 7. 遍历数组
echo -e "\n🔄 遍历课程列表:"
jq -r '.courses[] | "课程ID: \(.id), 名称: \(.name)"' $JSON_FILE
