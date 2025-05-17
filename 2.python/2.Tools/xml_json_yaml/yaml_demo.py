#!/usr/bin/env python
#########################################################################
# File Name: yaml_demo.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 17 May 2025 04:05:50 PM CST
#########################################################################

import yaml
from datetime import datetime

def yaml_demo():
    # 1. 创建复杂数据结构
    data = {
        "name": "Alice",
        "age": 30,
        "isStudent": False,
        "address": {
            "city": "New York",
            "zip": "10001"
        },
        "hobbies": ["coding", "reading"],
        "courses": [
            {"id": 1, "name": "Math", "active": True},
            {"id": 2, "name": "History", "active": False}
        ],
        "meta": {
            "createdAt": datetime.now().isoformat(),  # 时间格式化
            "tags": None  # YAML 中为 null
        }
    }

    # 2. 写入 YAML 文件
    with open("demo.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print("✅ YAML 文件写入完成！")

    # 3. 读取 YAML 文件
    try:
        with open("demo.yaml", "r", encoding="utf-8") as f:
            loaded_data = yaml.safe_load(f)

        print("\n🔍 读取整个文件:")
        print(yaml.dump(loaded_data, allow_unicode=True, sort_keys=False))

        # 4. 访问字段
        print("\n🔍 访问嵌套字段:")
        print(f"城市: {loaded_data['address']['city']}")
        print(f"第一个课程: {loaded_data['courses'][0]['name']}")

        # 5. 修改数据
        loaded_data["age"] = 31
        loaded_data["courses"].append({"id": 3, "name": "Physics", "active": True})

        # 6. 删除字段
        loaded_data.pop("isStudent", None)

        # 7. 写回文件
        with open("demo_updated.yaml", "w", encoding="utf-8") as f:
            yaml.dump(loaded_data, f, allow_unicode=True, sort_keys=False)
        print("\n🔄 修改后的文件已保存为 demo_updated.yaml")

    except FileNotFoundError:
        print("❌ 文件不存在！")
    except yaml.YAMLError as e:
        print(f"❌ YAML 解析错误: {e}")

if __name__ == "__main__":
    yaml_demo()

