# 注意：确保 utils 和 config 目录与 app.py 在同一级目录
try:
    from utils.command_utils import generate_command  # 确保导入路径正确
    from utils.feature_utils import get_vendor_features, get_config_tips
    from config.device_templates import device_templates, get_common_config_types
except ImportError as e:
    raise ImportError(f"缺少必要模块，请检查项目结构: {e}")

def render():
    st.title("高级网络设备命令生成器")
    st.markdown("支持华为、锐捷、新华三设备配置生成与对比 | 包含深度OSPF/BGP配置及常用网络功能")
    st.markdown("作者：zgy | 公众号：小朱学网络 | 2790266896@qq.com")

    st.subheader("单设备配置生成")
    col1, col2 = st.columns(2)

    with col1:
        vendor = st.selectbox("选择设备厂商", list(device_templates.keys()))

    with col2:
        config_options = list(device_templates[vendor].keys())
        config_type = st.selectbox("选择配置类型", config_options)

    current_config = device_templates[vendor][config_type]
    params = current_config["params"]

    user_inputs = {}
    st.subheader("配置参数")
    cols = st.columns(2)
    col_index = 0

    for param, default_value in params.items():
        with cols[col_index % 2]:
            if isinstance(default_value, list) and any(isinstance(i, str) for i in default_value):
                if default_value and default_value[0] == "":
                    user_inputs[param] = st.selectbox(
                        f"{param} (可选)",
                        options=default_value,
                        key=f"{vendor}_{config_type}_{param}"
                    )
                else:
                    user_inputs[param] = st.selectbox(
                        f"选择 {param}",
                        options=default_value,
                        key=f"{vendor}_{config_type}_{param}"
                    )
            else:
                user_inputs[param] = st.text_input(
                    f"输入 {param}",
                    value=default_value,
                    key=f"{vendor}_{config_type}_{param}"
                )
        col_index += 1

    if st.button("生成命令", type="primary"):
        command = generate_command(vendor, config_type, user_inputs)
        st.subheader("生成的命令")
        st.code(command, language="bash")
        st.download_button(
            label="复制命令",
            data=command,
            file_name=f"{vendor}_{config_type}_config.txt",
            mime="text/plain"
        )

    st.markdown("---")
    st.subheader("📖 使用指南")
    st.write("""...""")  # 可从原始文件中提取说明部分填充