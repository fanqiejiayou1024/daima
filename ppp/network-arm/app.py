import streamlit as st
import pages.single_vendor as single_vendor
import pages.multi_vendor as multi_vendor

# 必须第一个调用 Streamlit 命令
st.set_page_config(page_title="网络命令生成器", layout="wide", page_icon="🌐")

# 页面选择器
mode = (st.sidebar.radio
        ("选择应用模式", ["单厂商配置生成", "多厂商命令对比"], key="mode_selector"))

if mode == "单厂商配置生成":
    single_vendor.render()
else:
    multi_vendor.render()
