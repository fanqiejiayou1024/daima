import streamlit as st
from utils.command_utils import generate_command
from utils.feature_utils import get_vendor_features, get_config_tips
from config.device_templates import device_templates, get_common_config_types

def render():
    st.title("多厂商命令对比")

    common_configs = get_common_config_types()
    config_type = st.selectbox("选择要对比的配置类型", common_configs)

    st.markdown("---")
    st.subheader("参数配置")

    vendor_params = {}
    tabs = st.tabs(list(device_templates.keys()))

    for idx, vendor in enumerate(device_templates):
        with tabs[idx]:
            if config_type not in device_templates[vendor]:
                st.warning(f"{vendor} 不支持 {config_type} 配置")
                vendor_params[vendor] = None
                continue

            st.markdown(f"### {vendor} 参数设置")
            params = device_templates[vendor][config_type]["params"]
            vendor_params[vendor] = {}

            for param, default_value in params.items():
                if isinstance(default_value, list) and any(isinstance(i, str) for i in default_value):
                    if default_value and default_value[0] == "":
                        vendor_params[vendor][param] = st.selectbox(
                            f"{param} (可选)",
                            options=default_value,
                            key=f"compare_{vendor}_{param}"
                        )
                    else:
                        vendor_params[vendor][param] = st.selectbox(
                            f"选择 {param}",
                            options=default_value,
                            key=f"compare_{vendor}_{param}"
                        )
                else:
                    vendor_params[vendor][param] = st.text_input(
                        f"输入 {param}",
                        value=default_value,
                        key=f"compare_{vendor}_{param}"
                    )

    if st.button("生成对比命令", type="primary"):
        commands = {}
        for vendor in device_templates:
            if vendor_params.get(vendor) and config_type in device_templates[vendor]:
                commands[vendor] = generate_command(vendor, config_type, vendor_params[vendor])

        st.markdown("---")
        st.subheader("命令对比结果")

        cols = st.columns(len(commands))
        for idx, (vendor, command) in enumerate(commands.items()):
            with cols[idx]:
                st.markdown(f"**{vendor}**")
                st.code(command, language="bash")
                st.download_button(
                    label=f"复制{vendor}命令",
                    data=command,
                    file_name=f"{vendor}_{config_type}.txt",
                    mime="text/plain",
                    key=f"dl_{vendor}"
                )

        st.markdown("---")
        st.subheader("命令差异分析")

        diff_data = []
        for vendor, cmd in commands.items():
            diff_data.append({
                "厂商": vendor,
                "命令特点": get_vendor_features(vendor, config_type, cmd),
                "配置建议": get_config_tips(vendor, config_type)
            })

        if len(set(cmd for cmd in commands.values())) > 1:
            st.success("检测到命令语法差异：")
            st.table(diff_data)
        else:
            st.info("所有厂商命令语法相同")
