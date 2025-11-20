# app.py

import streamlit as st
import pages.single_vendor as single_vendor
import pages.multi_vendor as multi_vendor

# 必须第一个调用 Streamlit 命令
st.set_page_config(page_title="网络命令生成器", layout="wide", page_icon="🌐")

# 添加自定义CSS以隐藏选择器
st.markdown(
    """
    <style>
        .css-1v3fvcr {display: none;} /* 隐藏选择器 */
    </style>
    """,
    unsafe_allow_html=True,
)

# 页面选择器（虽然被隐藏，但仍然保持其功能）
mode = st.sidebar.radio("选择应用模式", ["单厂商配置生成", "多厂商命令对比"], key="mode_selector")

if mode == "单厂商配置生成":
    single_vendor.render()
else:
    multi_vendor.render()