# -*- coding: utf-8 -*-
"""实验01 配套模块：学生成绩记录解析。"""

def parse_student(line):
    line = str(line).strip()
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误：期望 2 个，实际 {len(parts)} -> {line!r}")
    name, score_text = parts[0].strip(), parts[1].strip()
    if not name:
        raise ValueError(f"姓名为空 -> {line!r}")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是合法整数：{score_text!r}") from None
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100：{score}")
    return {"name": name, "score": score}
