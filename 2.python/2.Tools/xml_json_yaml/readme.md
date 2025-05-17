## **1. XML 文件格式详解**
### **基本规则**
- **标签结构**：`<tag>content</tag>` 或自闭合标签 `<tag/>`。
- **属性**：`<tag attr1="value1" attr2="value2">`。
- **必须有一个根元素**。
- **文件扩展名**：`.xml`

### **常见场景示例**
#### **(1) 简单文档**
```xml
<person>
  <name>Alice</name>
  <age>30</age>
  <isStudent>false</isStudent>
</person>
```

#### **(2) 带属性的标签**
```xml
<book id="101" lang="en">
  <title>XML Guide</title>
  <price currency="USD">29.99</price>
</book>
```

#### **(3) 嵌套结构**
```xml
<company>
  <employee>
    <id>1</id>
    <name>Alice</name>
    <department name="Engineering"/>
  </employee>
  <employee>
    <id>2</id>
    <name>Bob</name>
    <department name="HR"/>
  </employee>
</company>
```

#### **(4) 混合内容（文本+标签）**
```xml
<message>
  This is a <b>mixed-content</b> example with <link url="https://example.com">a link</link>.
</message>
```

#### **(5) 数组等价物**
```xml
<fruits>
  <fruit>apple</fruit>
  <fruit>banana</fruit>
  <fruit>orange</fruit>
</fruits>
```

#### **(6) 命名空间（Namespace）**
```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="book" type="xs:string"/>
</xs:schema>
```

#### **(7) CDATA 区块（避免转义）**
```xml
<code>
  <![CDATA[
    if (a < b && b > c) {
      console.log("Hello World!");
    }
  ]]>
</code>
```

#### **(8) 注释与处理指令**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- 这是一个注释 -->
<root>
  <?custom-pipeline process="transform"?>
  <data>value</data>
</root>
```

---

## **2. JSON 文件格式详解**
### **基本规则**
- **键值对结构**：`"key": value`，键必须是**双引号包裹的字符串**。
- **数据类型**：
  - 字符串（`"text"`）
  - 数字（`42`、`3.14`）
  - 布尔值（`true`/`false`）
  - 数组（`[1, 2, 3]`）
  - 对象（`{"key": "value"}`）
  - `null`
- **文件扩展名**：`.json`

### **常见场景示例**
#### **(1) 简单对象**
```json
{
  "name": "Alice",
  "age": 30,
  "isStudent": false
}
```

#### **(2) 嵌套对象**
```json
{
  "person": {
    "name": "Bob",
    "address": {
      "city": "Beijing",
      "postalCode": "100000"
    }
  }
}
```

#### **(3) 数组**
```json
{
  "fruits": ["apple", "banana", "orange"],
  "matrix": [[1, 2], [3, 4]]
}
```

#### **(4) 混合复杂结构**
```json
{
  "employees": [
    {
      "id": 1,
      "name": "Alice",
      "skills": ["Java", "Python"],
      "meta": {
        "hireDate": "2020-01-15",
        "fullTime": true
      }
    },
    {
      "id": 2,
      "name": "Bob",
      "skills": ["SQL"],
      "meta": {
        "hireDate": "2021-03-22",
        "fullTime": false
      }
    }
  ]
}
```

#### **(5) 特殊值**
```json
{
  "nullableField": null,
  "escapedChars": "Line1\nLine2",
  "unicode": "\u03A9",  // Unicode 字符 Ω
  "scientificNumber": 1.23e+5
}
```

#### **(6) JSON 注释（非标准扩展）**
```json
{
  "//comment": "JSON 标准不支持注释，但某些解析器允许这种 hack",
  "name": "Alice"
}
```

---


## **3. YAML 文件格式详解**
### **基本规则**
- **缩进结构**：使用空格（通常2或4个）表示层级，**不支持Tab缩进**
- **键值对**：`key: value`（冒号后需空格）
- **数据类型**：
  - 字符串（可无引号，含特殊字符时用`""`或`''`）
  - 数字（整数/浮点数）、布尔值（`true`/`false`）
  - 数组（`-`开头或`[]`语法）
  - 对象（嵌套键值对）
  - `null`（用`null`或`~`表示）
  - 时间（`2023-01-01`自动识别）
- **文件扩展名**：`.yaml` 或 `.yml`
- **注释**：以 `#` 开头

---

### **常见场景示例**
#### **(1) 简单键值对**
```yaml
name: Alice
age: 30
is_student: false
birthday: 1990-01-15  # 日期类型
```

#### **(2) 嵌套对象**
```yaml
person:
  name: Bob
  address:
    city: Beijing
    postal_code: "100000"  # 数字作为字符串需引号
```

#### **(3) 数组**
```yaml
# 短横线语法
fruits:
  - apple
  - banana
  - orange

# 行内语法（类似JSON）
matrix: [[1, 2], [3, 4]]
```

#### **(4) 混合复杂结构**
```yaml
employees:
  - id: 1
    name: Alice
    skills: ["Java", "Python"]
    meta:
      hire_date: 2020-01-15
      full_time: true

  - id: 2
    name: Bob
    skills:
      - SQL
    meta:
      hire_date: 2021-03-22
      full_time: false
```

#### **(5) 特殊值处理**
```yaml
# 多行字符串
description: |
  This is a
  multi-line
  string.

# 保留换行的字符串
bio: >
  This will fold
  into one line.

# 特殊类型标记
binary_data: !!binary SGVsbG8=  # Base64编码
pi: !!float 3.14
timestamp: !!str 2025-05-20    # 强制转为字符串
```

#### **(6) 锚点与引用**
```yaml
defaults: &defaults
  api_version: v1
  timeout: 30s

service:
  <<: *defaults  # 合并锚点内容
  endpoint: /api
```

---

## **3. YAML vs JSON vs XML 对比**
| **特性**          | XML                      | JSON                      | YAML                      |
|-------------------|--------------------------|---------------------------|---------------------------|
| **可读性**        | ⭐⭐（标签冗余）         | ⭐⭐⭐（结构严谨）        | ⭐⭐⭐⭐⭐（自然语言风格）|
| **注释支持**      | ✅                       | ❌                        | ✅                        |
| **数据类型扩展**  | ❌                       | ❌                        | ✅（时间/二进制/锚点）    |
| **适合场景**      | 文档标记/严格验证        | API数据交换               | 配置文件/复杂数据结构     |


| **场景**              | **XML 示例**                              | **JSON 示例**            | **YAML 示例**                     |
|-----------------------|-------------------------------------------|--------------------------|-----------------------------------|
| **简单键值对**        | `<name>Alice</name>`                      | `{"name": "Alice"}`      | `name: Alice`                     |
| **多层嵌套**          | `<a><b><c>1</c></b></a>`                  | `{"a": {"b": {"c": 1}}}` | `a:  b:  c: 1`（缩进表示层级）    |
| **数组/列表**         | `<ids><id>1</id><id>2</id></ids>`         | `{"ids": [1, 2, 3]}`     | `ids:  - 1  - 2  - 3`             |
| **属性 vs 字段**      | `<book id="123" price="20"/>`             | 无属性概念               | 无属性概念，键值对替代：<br>`book:  id: 123  price: 20` |
| **元数据与混合内容**  | 直接支持（如 `<text>Hello <b>World</b></text>`） | 需额外字段存储    | 支持多行文本和混合内容：<br>`text: \|  Hello **World**` |
| **二进制数据**        | CDATA 或 Base64                           | Base64 编码字符串        | `!!binary` 标签：<br>`data: !!binary SGVsbG8=` |
| **注释**              | `<!-- 注释 -->`                           | 不支持（需 hack）        | `# 注释`                          |
| **特殊数据类型**      | 需自定义扩展                              | 仅基础类型               | 原生支持（时间/二进制/锚点等）：<br>`date: 2023-01-01` |



---

## **4. 特殊场景处理**
### **XML 特殊场景**
- **空标签表示**：
  ```xml
  <empty1></empty1>
  <empty2/>  <!-- 推荐写法 -->
  ```
- **属性 vs 子元素**（设计选择）：
  ```xml
  <!-- 方案1：属性 -->
  <book id="101" title="XML Guide"/>

  <!-- 方案2：子元素 -->
  <book>
    <id>101</id>
    <title>XML Guide</title>
  </book>
  ```

### **JSON 特殊场景**
- **大数字问题**：JSON 无法安全表示 64 位整数（如 `2^53 +1`），需转为字符串。
  ```json
  {"bigInt": "9007199254740993"}
  ```
- **日期格式**：无原生日期类型，通常用 ISO 字符串。
  ```json
  {"createdAt": "2023-01-01T12:00:00Z"}
  ```

### **YAML 特殊场景**
1. **多文档支持**：用 `---` 分隔多个YAML文档
   ```yaml
   ---
   config:
     env: dev
   ---
   data:
     items: [1, 2, 3]
   ```

2. **强制类型转换**：
   ```yaml
   number_as_str: !!str 42
   ```

3. **JSON兼容性**：YAML 1.2 是 JSON 的超集，所有合法JSON都是合法YAML

---

## **5. 何时选择哪种格式？**
- **选 XML**：
  - 需要文档标记（如 HTML/SVG）。
  - 企业级数据交换（如 SOAP、银行系统）。
  - 需要严格模式验证（XSD/DTD）。

- **选 JSON**：
  - API 数据传输（如 RESTful API）。
  - 配置文件（如 `package.json`）。
  - 需要快速解析和简洁性的场景。

- **选 YAML**：
  - **配置文件**（如Docker Compose/Kubernetes）
  - **需要人类可读**的复杂数据结构
  - **需要注释**的场合

  **慎用场景**：
  - 高性能API通信（JSON更高效）
  - 需要严格模式验证（XML的XSD更强大）

