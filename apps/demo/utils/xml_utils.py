import xml.etree.cElementTree as ET

"""
    xml相关操作
"""


# 获取xml str中指定path的值
# 若不存在则返回空str
def xml_get_value(xml_str: str, path: str) -> str:
    ele = ET.fromstring(xml_str).find(path)
    if ele is None:
        return ""
    return ele.text

