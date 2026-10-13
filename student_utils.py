# -*- coding: utf-8 -*-
"""实验01 配套模块：学生成绩记录解析。

本模块提供 parse_student()，把 students.txt 中的一行文本
解析成 {"name": ..., "score": ...} 字典；无效记录抛出 ValueError。
"""


def parse_student(line):
    """解析一行 "name,score" 文本，返回字典。

    参数:
        line (str): 形如 "Alice,85" 的一行文本。

    返回:
        dict: {"name": str, "score": int}

    异常:
        ValueError: 字段数量不对 / 姓名为空 / 成绩不是整数 / 成绩超出 0~100。
    """
    # 1) 去掉首尾空白
    line = str(line).strip()

    # 2) 按英文逗号切分
    parts = line.split(",")

    # 3) 检查字段数量
    if len(parts) != 2:
        raise ValueError(
            f"字段数量错误：期望 2 个字段(name,score)，实际 {len(parts)} 个 -> {line!r}"
        )

    name, score_text = parts[0].strip(), parts[1].strip()

    # 4) 检查姓名是否为空
    if not name:
        raise ValueError(f"姓名为空 -> {line!r}")

    # 5) 成绩转换为整数
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是合法整数：{score_text!r} -> {line!r}") from None

    # 6) 检查成绩范围
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100 范围：{score} -> {line!r}")

    return {"name": name, "score": score}
