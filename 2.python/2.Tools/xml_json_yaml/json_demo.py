#!/usr/bin/env python
#########################################################################
# File Name: json_demo.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 17 May 2025 02:51:06 PM CST
#########################################################################

import json
from datetime import datetime

def json_demo():
    # 1. 创建复杂 JSON 数据
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
            "createdAt": datetime.now().isoformat(),  # 日期处理
            "tags": None  # None 会转为 null
        }
    }

    # 2. 写入 JSON 文件（含缩进格式化）
    with open("demo.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)  # 禁用 ASCII 转义
    print("✅ JSON 文件写入完成！")

    # 3. 读取 JSON 文件（含异常处理）
    try:
        with open("demo.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)

        print("\n🔍 读取整个文件:")
        print(json.dumps(loaded_data, indent=2, ensure_ascii=False))

        # 4. 访问字段
        print("\n🔍 访问嵌套字段:")
        print(f"城市: {loaded_data['address']['city']}")
        print(f"第一个课程: {loaded_data['courses'][0]['name']}")

        # 5. 修改数据
        loaded_data["age"] = 31
        loaded_data["courses"].append({"id": 3, "name": "Physics", "active": True})

        # 6. 删除字段
        del loaded_data["isStudent"]

        # 7. 写回文件
        with open("demo_updated.json", "w", encoding="utf-8") as f:
            json.dump(loaded_data, f, indent=2, ensure_ascii=False)
        print("\n🔄 修改后的文件已保存为 demo_updated.json")

    except FileNotFoundError:
        print("❌ 文件不存在！")
    except json.JSONDecodeError:
        print("❌ 文件不是有效的 JSON！")

if __name__ == "__main__":
    json_demo()
