import streamlit as st
from copy import deepcopy
("作者：zgy | 公众号：小朱学网络 | 2790266896@qq.com")
# 扩展设备命令模板 - 包含华为、锐捷、新华三
device_templates = {
    "华为": {
        "接口配置": {
            "template": "interface {interface}\n description {description}\n ip address {ip} {mask}\n vlan-type dot1q {vlan}\n {shutdown}",
            "params": {
                "interface": ["GigabitEthernet0/0/1", "GigabitEthernet0/0/2", "GigabitEthernet0/0/3"],
                "description": "服务器接口",
                "ip": "192.168.1.1",
                "mask": "255.255.255.0",
                "vlan": "10",
                "shutdown": ["", "shutdown"]  # 新增接口状态控制
            }
        },
        "VLAN配置": {
            "template": "vlan {vlan_id}\n description {description}",
            "params": {
                "vlan_id": ["10", "20", "30"],
                "description": "销售部VLAN"
            }
        },
        "静态路由": {
            "template": "ip route-static {network} {mask} {next_hop} {preference}",
            "params": {
                "network": "10.0.0.0",
                "mask": "255.0.0.0",
                "next_hop": "192.168.1.254",
                "preference": ["", "preference 100"]  # 新增路由优先级
            }
        },
        "OSPF配置": {
            "template": "router id {router_id}\nospf {process_id} router-id {router_id}\n area {area}\n  network {network} {wildcard}\n {authentication} {summary} {passive_interface}",
            "params": {
                "process_id": "1",
                "router_id": "1.1.1.1",
                "area": "0",
                "network": "192.168.1.0",
                "wildcard": "0.0.0.255",
                "authentication": ["", "authentication-mode simple {password}"],  # 认证配置
                "summary": ["", "abr-summary {summary_network} {summary_mask}"],  # 路由汇总
                "passive_interface": ["", "silent-interface {interface}"],  # 被动接口
                "password": "Huawei@123",  # OSPF密码
                "summary_network": "192.168.0.0",  # 汇总网络
                "summary_mask": "255.255.0.0",  # 汇总掩码
                "interface": "Loopback0"  # 被动接口
            }
        },
        "BGP配置": {
            "template": "bgp {as_number}\n router-id {router_id}\n peer {peer_ip} as-number {peer_as}\n {ebgp_multihop} {route_reflector} {aggregate}",
            "params": {
                "as_number": "65001",
                "router_id": "1.1.1.1",
                "peer_ip": "10.1.1.1",
                "peer_as": "65002",
                "ebgp_multihop": ["", "peer {peer_ip} ebgp-max-hop {hop_count}"],  # EBGP多跳
                "route_reflector": ["", "peer {peer_ip} reflect-client"],  # 路由反射器
                "aggregate": ["", "aggregate {aggregate_network} {aggregate_mask} detail-suppressed"],  # 路由聚合
                "hop_count": "5",  # 跳数
                "aggregate_network": "10.0.0.0",  # 聚合网络
                "aggregate_mask": "255.0.0.0"  # 聚合掩码
            }
        },
        "VRRP配置": {
            "template": "interface {interface}\n vrrp vrid {vrid} virtual-ip {vip}\n vrrp vrid {vrid} priority {priority}\n {preempt} {track}",
            "params": {
                "interface": "GigabitEthernet0/0/1",
                "vrid": "10",
                "vip": "192.168.1.254",
                "priority": "100",
                "preempt": ["", "vrrp vrid {vrid} preempt-mode delay {delay}"],  # 抢占模式
                "track": ["", "vrrp vrid {vrid} track interface {track_interface} reduced {reduced_value}"],  # 接口跟踪
                "delay": "20",  # 抢占延迟
                "track_interface": "GigabitEthernet0/0/2",  # 跟踪接口
                "reduced_value": "30"  # 优先级减少值
            }
        },
        "MPLS配置": {
            "template": "mpls lsr-id {lsr_id}\nmpls\nmpls ldp\ninterface {interface}\n mpls\n mpls ldp\n {ldp_authentication}",
            "params": {
                "lsr_id": "1.1.1.1",
                "interface": "GigabitEthernet0/0/1",
                "ldp_authentication": ["", "mpls ldp authentication-mode md5 {ldp_password}"]  # LDP认证
            }
        },
        "ACL配置": {
            "template": "acl number {acl_number}\n rule {rule_id} permit {protocol} source {source_ip} {source_wildcard} destination {dest_ip} {dest_wildcard} {port}",
            "params": {
                "acl_number": ["2000", "3000", "4000"],  # 基本ACL/高级ACL
                "rule_id": "5",
                "protocol": ["ip", "tcp", "udp", "icmp"],
                "source_ip": "192.168.1.0",
                "source_wildcard": "0.0.0.255",
                "dest_ip": "10.0.0.0",
                "dest_wildcard": "0.255.255.255",
                "port": ["", "destination-port eq {port_number}"],  # 端口配置
                "port_number": "80"
            }
        },
        "NAT配置": {
            "template": "acl number {acl_number}\n rule 5 permit ip source {internal_network} {wildcard}\ninterface {interface}\n ip address {ip} {mask}\n nat outbound {acl_number} address-group {address_group}",
            "params": {
                "acl_number": "2000",
                "internal_network": "192.168.1.0",
                "wildcard": "0.0.0.255",
                "interface": "GigabitEthernet0/0/0",
                "ip": "100.1.1.1",
                "mask": "255.255.255.0",
                "address_group": "1"
            }
        },
        "DHCP配置": {
            "template": "dhcp enable\ninterface {interface}\n dhcp select interface\n dhcp server dns-list {dns_server}\n dhcp server excluded-ip-address {start_ip} {end_ip}",
            "params": {
                "interface": "Vlanif10",
                "dns_server": "8.8.8.8",
                "start_ip": "192.168.1.1",
                "end_ip": "192.168.1.10"
            }
        }
    },
    "锐捷": {
        "接口配置": {
            "template": "interface {interface}\n description {description}\n ip address {ip} {mask}\n switchport access vlan {vlan}\n {shutdown}",
            "params": {
                "interface": ["GigabitEthernet 0/1", "GigabitEthernet 0/2", "GigabitEthernet 0/3"],
                "description": "办公网络接口",
                "ip": "172.16.1.1",
                "mask": "255.255.255.0",
                "vlan": "100",
                "shutdown": ["", "shutdown"]
            }
        },
        "VLAN配置": {
            "template": "vlan {vlan_id}\n name {name}",
            "params": {
                "vlan_id": ["100", "200", "300"],
                "name": "技术部_VLAN"
            }
        },
        "OSPF配置": {
            "template": "router ospf {process_id}\n router-id {router_id}\n network {network} {wildcard} area {area}\n {authentication} {summary} {passive_interface}",
            "params": {
                "process_id": "1",
                "router_id": "2.2.2.2",
                "network": "192.168.0.0",
                "wildcard": "0.0.255.255",
                "area": "0",
                "authentication": ["",
                                   "area {area} authentication message-digest\n message-digest-key 1 md5 {password}"],
                "summary": ["", "area {area} range {summary_network} {summary_mask}"],
                "passive_interface": ["", "passive-interface {interface}"],
                "password": "Ruijie@123",
                "summary_network": "192.168.0.0",
                "summary_mask": "255.255.0.0",
                "interface": "Loopback0"
            }
        },
        "BGP配置": {
            "template": "router bgp {as_number}\n bgp router-id {router_id}\n neighbor {peer_ip} remote-as {peer_as}\n {ebgp_multihop} {route_reflector} {aggregate}",
            "params": {
                "as_number": "65001",
                "router_id": "2.2.2.2",
                "peer_ip": "10.2.2.2",
                "peer_as": "65002",
                "ebgp_multihop": ["", "neighbor {peer_ip} ebgp-multihop {hop_count}"],
                "route_reflector": ["", "neighbor {peer_ip} route-reflector-client"],
                "aggregate": ["", "aggregate-address {aggregate_network} {aggregate_mask} summary-only"],
                "hop_count": "5",
                "aggregate_network": "10.0.0.0",
                "aggregate_mask": "255.0.0.0"
            }
        },
        "VRRP配置": {
            "template": "interface {interface}\n vrrp {vrid}\n  virtual-address {vip}\n  priority {priority}\n {preempt} {track}",
            "params": {
                "interface": "GigabitEthernet 0/1",
                "vrid": "10",
                "vip": "172.16.1.254",
                "priority": "100",
                "preempt": ["", " preempt delay {delay}"],
                "track": ["", " track interface {track_interface} priority reduced {reduced_value}"],
                "delay": "20",
                "track_interface": "GigabitEthernet 0/2",
                "reduced_value": "30"
            }
        },
        "MPLS配置": {
            "template": "mpls\nmpls ldp\n router-id {lsr_id}\ninterface {interface}\n mpls ip\n {ldp_authentication}",
            "params": {
                "lsr_id": "2.2.2.2",
                "interface": "GigabitEthernet 0/1",
                "ldp_authentication": ["", "mpls ldp neighbor {neighbor_ip} password {ldp_password}"],
                "neighbor_ip": "10.2.2.3",
                "ldp_password": "RuijieMPLS"
            }
        },
        "端口安全": {
            "template": "interface {interface}\n switchport port-security\n switchport port-security maximum {max_mac}\n switchport port-security violation {violation}",
            "params": {
                "interface": "GigabitEthernet 0/1",
                "max_mac": "3",
                "violation": ["shutdown", "restrict", "protect"]
            }
        },
        "DHCP配置": {
            "template": "service dhcp\nip dhcp pool {pool_name}\n network {network} {mask}\n default-router {gateway}\n dns-server {dns_server}\n lease {days} {hours} {minutes}",
            "params": {
                "pool_name": "OFFICE_POOL",
                "network": "172.16.1.0",
                "mask": "255.255.255.0",
                "gateway": "172.16.1.254",
                "dns_server": "8.8.8.8",
                "days": "0",
                "hours": "8",
                "minutes": "0"
            }
        },
        "STP配置": {
            "template": "spanning-tree\nspanning-tree mode {stp_mode}\nspanning-tree priority {priority}",
            "params": {
                "stp_mode": ["pvst", "rapid-pvst", "mstp"],
                "priority": "4096"
            }
        }
    },
    "新华三": {
        "接口配置": {
            "template": "interface {interface}\n description {description}\n ip address {ip} {mask}\n port link-type trunk\n port trunk permit vlan {vlan}\n {shutdown}",
            "params": {
                "interface": ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "GigabitEthernet1/0/3"],
                "description": "核心交换机接口",
                "ip": "10.10.1.1",
                "mask": "255.255.255.0",
                "vlan": "10,20",
                "shutdown": ["", "shutdown"]
            }
        },
        "VLAN配置": {
            "template": "vlan {vlan_id}\n description {description}",
            "params": {
                "vlan_id": ["10", "20", "30"],
                "description": "管理VLAN"
            }
        },
        "OSPF配置": {
            "template": "ospf {process_id} router-id {router_id}\n area {area}\n  network {network} {wildcard}\n {authentication} {summary} {passive_interface}",
            "params": {
                "process_id": "1",
                "router_id": "3.3.3.3",
                "area": "0",
                "network": "10.10.0.0",
                "wildcard": "0.0.255.255",
                "authentication": ["", "authentication-mode {auth_mode} {password}"],
                "summary": ["", "abr-summary {summary_network} {summary_mask}"],
                "passive_interface": ["", "silent-interface {interface}"],
                "auth_mode": ["simple", "md5", "hmac-md5"],
                "password": "H3C@123",
                "summary_network": "10.10.0.0",
                "summary_mask": "255.255.0.0",
                "interface": "LoopBack0"
            }
        },
        "BGP配置": {
            "template": "bgp {as_number}\n router-id {router_id}\n peer {peer_ip} as-number {peer_as}\n {ebgp_multihop} {route_reflector} {aggregate}",
            "params": {
                "as_number": "65001",
                "router_id": "3.3.3.3",
                "peer_ip": "10.3.3.3",
                "peer_as": "65002",
                "ebgp_multihop": ["", "peer {peer_ip} ebgp-max-hop {hop_count}"],
                "route_reflector": ["", "peer {peer_ip} reflect-client"],
                "aggregate": ["", "aggregate {aggregate_network} {aggregate_mask} detail-suppressed"],
                "hop_count": "5",
                "aggregate_network": "10.0.0.0",
                "aggregate_mask": "255.0.0.0"
            }
        },
        "VRRP配置": {
            "template": "interface {interface}\n vrrp vrid {vrid} virtual-ip {vip}\n vrrp vrid {vrid} priority {priority}\n {preempt} {track}",
            "params": {
                "interface": "Vlan-interface10",
                "vrid": "10",
                "vip": "10.10.1.254",
                "priority": "100",
                "preempt": ["", "vrrp vrid {vrid} preempt-mode delay {delay}"],
                "track": ["", "vrrp vrid {vrid} track interface {track_interface} reduced {reduced_value}"],
                "delay": "20",
                "track_interface": "GigabitEthernet1/0/1",
                "reduced_value": "30"
            }
        },
        "MPLS配置": {
            "template": "mpls lsr-id {lsr_id}\nmpls ldp\ninterface {interface}\n mpls enable\n mpls ldp enable\n {ldp_authentication}",
            "params": {
                "lsr_id": "3.3.3.3",
                "interface": "GigabitEthernet1/0/1",
                "ldp_authentication": ["", "mpls ldp authentication md5 {ldp_password}"]
            }
        },
        "QoS配置": {
            "template": "traffic classifier {classifier_name} operator or\n if-match {match_condition}\ntraffic behavior {behavior_name}\n {action}\ntraffic policy {policy_name}\n classifier {classifier_name} behavior {behavior_name}\ninterface {interface}\n traffic-policy {policy_name} inbound",
            "params": {
                "classifier_name": "VOICE",
                "match_condition": ["dscp ef", "ip precedence 5"],
                "behavior_name": "PRIORITY",
                "action": "queue ef bandwidth percent 30",
                "policy_name": "QOS_POLICY",
                "interface": "GigabitEthernet1/0/1"
            }
        },
        "堆叠配置": {
            "template": "irf member {member_id} priority {priority}\nirf-port {irf_port}\n port group interface {interface1}\n port group interface {interface2}\nirf-port-configuration active",
            "params": {
                "member_id": "1",
                "priority": "32",
                "irf_port": "1/1",
                "interface1": "Ten-GigabitEthernet1/0/49",
                "interface2": "Ten-GigabitEthernet1/0/50"
            }
        },
        "日志配置": {
            "template": "info-center enable\ninfo-center loghost {log_server} facility {facility} level {level}",
            "params": {
                "log_server": "192.168.100.100",
                "facility": "local4",
                "level": ["informational", "warning", "error"]
            }
        }
    }
}


# 获取所有厂商共有的配置类型
def get_common_config_types():
    all_types = [set(device_templates[vendor].keys()) for vendor in device_templates]
    common = set.intersection(*all_types)
    # 确保OSPF、BGP等核心协议在对比列表中
    core_types = {"接口配置", "VLAN配置", "OSPF配置", "BGP配置", "VRRP配置"}
    return list(common | core_types)


# 生成命令函数
def generate_command(vendor, config_type, params):
    template = device_templates[vendor][config_type]["template"]
    # 处理可选参数
    for param, value in params.items():
        if isinstance(value, list) and value and value[0] == "":
            # 可选参数未选择
            template = template.replace("{" + param + "}", "")
        else:
            if isinstance(value, list):
                value = value[0]  # 取实际选择的值
            template = template.replace("{" + param + "}", str(value))
    # 清理多余的空行
    template = "\n".join([line for line in template.splitlines() if line.strip()])
    return template

# 获取厂商特点
def get_vendor_features(vendor, config_type, command):
    features = []

    if "华为" in vendor:
        features.append("命令层次使用空格缩进")
        features.append("配置视图使用模式切换")
        if "OSPF" in config_type:
            features.append("使用ospf进程视图配置")
        if "BGP" in config_type:
            features.append("BGP配置在bgp视图下")

    if "锐捷" in vendor:
        features.append("命令语法更接近Cisco")
        features.append("使用直接配置模式")
        if "OSPF" in config_type:
            features.append("OSPF全局配置模式")

    if "新华三" in vendor:
        features.append("命令风格类似华为但有差异")
        features.append("接口命名格式不同")
        if "OSPF" in config_type:
            features.append("OSPF配置使用router-id参数")

    # 添加特定协议特点
    if "OSPF" in config_type:
        features.append("支持区域认证和接口认证")
        features.append("支持路由汇总")

    if "BGP" in config_type:
        features.append("支持EBGP多跳")
        features.append("支持路由反射器")

    return "\n".join(f"- {f}" for f in features)


# 获取配置建议
def get_config_tips(vendor, config_type):
    tips = []

    if "OSPF" in config_type:
        tips.append("建议启用认证提高安全性")
        tips.append("合理使用被动接口减少不必要的LSA")

    if "BGP" in config_type:
        tips.append("EBGP会话建议配置最大跳数")
        tips.append("iBGP会话建议使用路由反射器或全连接")

    if "VRRP" in config_type:
        tips.append("配置抢占模式保证主备切换")
        tips.append("使用接口跟踪提高可靠性")

    if "ACL" in config_type:
        tips.append("ACL末尾隐含拒绝所有规则")
        tips.append("注意ACL应用方向(inbound/outbound)")

    return "\n".join(f"- {t}" for t in tips)


# 页面布局
st.set_page_config(page_title="网络命令生成器", layout="wide", page_icon="🌐")
st.title("高级网络设备命令生成器")
st.markdown("支持华为、锐捷、新华三设备配置生成与对比 | 包含深度OSPF/BGP配置及常用网络功能")
st.markdown("作者：zgy | 公众号：小朱学网络 | 2790266896@qq.com")
# 模式选择
mode = st.radio("选择模式", ["单厂商配置生成", "多厂商命令对比"], horizontal=True, key="mode_selector")

if mode == "单厂商配置生成":
    # 单厂商模式
    st.subheader("单设备配置生成")
    col1, col2 = st.columns(2)

    with col1:
        vendor = st.selectbox("选择设备厂商", list(device_templates.keys()))

    with col2:
        config_options = list(device_templates[vendor].keys())
        config_type = st.selectbox("选择配置类型", config_options)

    # 获取当前配置模板
    current_config = device_templates[vendor][config_type]
    params = current_config["params"]

    # 动态生成输入控件
    user_inputs = {}
    st.subheader("配置参数")
    cols = st.columns(2)  # 双列布局提高空间利用率
    col_index = 0

    for param, default_value in params.items():
        with cols[col_index % 2]:
            if isinstance(default_value, list) and any(isinstance(i, str) for i in default_value):
                # 下拉选择或可选参数
                if default_value and default_value[0] == "":
                    # 可选参数（带空选项）
                    user_inputs[param] = st.selectbox(
                        f"{param} (可选)",
                        options=default_value,
                        key=f"{vendor}_{config_type}_{param}"
                    )
                else:
                    # 常规下拉框
                    user_inputs[param] = st.selectbox(
                        f"选择 {param}",
                        options=default_value,
                        key=f"{vendor}_{config_type}_{param}"
                    )
            else:
                # 文本输入
                user_inputs[param] = st.text_input(
                    f"输入 {param}",
                    value=default_value,
                    key=f"{vendor}_{config_type}_{param}"
                )
        col_index += 1

    # 生成命令
    if st.button("生成命令", type="primary", key="generate_button"):
        command = generate_command(vendor, config_type, user_inputs)

        st.subheader("生成的命令")
        st.code(command, language="bash")

        # 复制按钮
        st.download_button(
            label="复制命令",
            data=command,
            file_name=f"{vendor}_{config_type}_config.txt",
            mime="text/plain",
            key="download_button"
        )

else:
    # 多厂商对比模式
    st.subheader("多厂商命令对比")

    # 获取共有配置类型
    common_configs = get_common_config_types()
    config_type = st.selectbox("选择要对比的配置类型", common_configs)

    st.markdown("---")
    st.subheader("参数配置")

    # 为每个厂商创建参数输入
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

    # 生成对比命令
    if st.button("生成对比命令", type="primary", key="compare_button"):
        st.markdown("---")
        st.subheader("命令对比结果")

        commands = {}
        for vendor in device_templates:
            if vendor_params.get(vendor) and config_type in device_templates[vendor]:
                commands[vendor] = generate_command(vendor, config_type, vendor_params[vendor])

        # 并排显示命令
        cols = st.columns(len(commands))
        for idx, (vendor, command) in enumerate(commands.items()):
            with cols[idx]:
                st.markdown(f"**{vendor}**")
                st.code(command, language="bash")

                # 为每个厂商添加复制按钮
                st.download_button(
                    label=f"复制{vendor}命令",
                    data=command,
                    file_name=f"{vendor}_{config_type}.txt",
                    mime="text/plain",
                    key=f"dl_{vendor}"
                )

        # 添加差异对比
        st.markdown("---")
        st.subheader("命令差异分析")

        # 收集所有命令
        all_commands = [f"{vendor}:\n{cmd}" for vendor, cmd in commands.items()]

        # 显示差异
        if len(set(all_commands)) > 1:
            st.success("检测到命令语法差异：")

            # 创建差异对比表格
            diff_data = []
            for vendor, cmd in commands.items():
                diff_data.append({
                    "厂商": vendor,
                    "命令特点": get_vendor_features(vendor, config_type, cmd),
                    "配置建议": get_config_tips(vendor, config_type)
                })

            st.table(diff_data)
        else:
            st.info("所有厂商命令语法相同")



# 使用说明
st.markdown("---")
st.subheader("📖 使用指南")
st.write("""
1. **单厂商模式**：
   - 选择设备厂商和配置类型
   - 填写配置参数（可选参数留空则不生成）
   - 生成并复制命令

2. **多厂商对比模式**：
   - 选择要对比的配置类型
   - 为每个厂商设置参数
   - 查看命令差异和配置建议

3. **新增配置类型**：
   - OSPF增强：认证、路由汇总、被动接口
   - BGP增强：EBGP多跳、路由反射器、路由聚合
   - VRRP增强：抢占模式、接口跟踪
   - 常用功能：ACL、NAT、DHCP、端口安全、STP、堆叠、日志
""")

# 配置类型说明 - 扩展部分
with st.expander("📚 高级配置说明", expanded=False):
    st.markdown("""
    ## 深度协议配置指南

    ### OSPF高级配置
    **认证机制**：
    - 简单认证：适用于低安全环境，密码明文传输
    - MD5认证：推荐用于生产环境，提供消息完整性验证
    - HMAC-MD5：增强型加密认证，防止重放攻击

    **区域优化**：
    - 末节区域(Stub)：禁止AS外部LSA，减少路由表大小
    - 完全末节区域(Totally Stubby)：禁止AS外部和区域间LSA
    - NSSA区域：允许引入有限的外部路由

    **性能调优**：
    - SPF智能定时器：控制SPF计算频率，减少CPU波动
    - LSA生成间隔：限制LSA更新频率，避免网络震荡
    - 邻居状态检测：BFD联动实现毫秒级故障检测

    ---

    ### BGP高级配置
    **路由策略**：
    - 路由映射(Route-map)：实现复杂路由过滤和属性修改
    - AS路径过滤：防止非法AS路径的路由注入
    - 团体属性：标记路由实现策略联动

    **路由优化**：
    - 路由阻尼(Dampening)：抑制震荡路由，提高网络稳定性
    - 路由刷新(Route Refresh)：动态策略更新无需重置会话
    - 附加路径(Add-Path)：多路径传输提高可靠性

    **高可用设计**：
    - GR能力协商：优雅重启减少路由收敛时间
    - BFD检测：毫秒级邻居故障检测
    - 多跳会话保护：TTL安全检测防止会话劫持

    ---

    ### VRRP高可用增强
    **高级特性**：
    - 虚拟MAC地址：0000-5E00-01xx (xx=VRID)
    - 认证支持：简单文本或MD5认证
    - 多网关负载均衡：不同VLAN使用不同VRID实现负载分担

    **监控增强**：
    - 上行链路质量检测：基于丢包率和延迟调整优先级
    - 对象跟踪：监控IP可达性和接口状态
    - 延迟抢占定时器：避免主备频繁切换

    ---

    ### MPLS深度配置
    **标签分发协议**：
    - LDP：基本标签分发，适合中小网络
    - RSVP-TE：流量工程，支持带宽预留和显式路径
    - MP-BGP：跨域VPN解决方案

    **VPN技术**：
    - L3VPN：基于MP-BGP的跨域三层VPN
    - L2VPN：VPLS/PW伪线技术实现二层互通
    - MPLS-TP：面向传输网的MPLS增强版

    **QoS集成**：
    - EXP字段映射：基于MPLS头部实现差分服务
    - 流量工程：带宽保证和链路保护
    - 层次化QoS：复杂业务流量整形

    ---

    ## 新增功能深度解析

    ### ACL高级应用
    **时间范围ACL**：
    - 基于时间段的访问控制
    - 工作日/非工作日策略分离
    - 周期性策略自动切换

    **自反ACL**：
    - 动态创建临时反向规则
    - 状态化会话跟踪
    - 增强安全性同时减少配置复杂度

    **基于用户的ACL**：
    - 结合身份认证系统
    - 动态用户策略分配
    - 终端无关的访问控制

    ---

    ### NAT高级应用
    **NAT64/DNS64**：
    - IPv6到IPv4的协议转换
    - 支持纯IPv6客户端访问IPv4资源
    - DNS协议扩展实现地址合成

    **NAT ALG应用层网关**：
    - 支持FTP、SIP等协议穿透
    - 动态端口协商解析
    - 嵌入式协议分析

    **双栈负载均衡**：
    - IPv4/IPv6双协议栈支持
    - 智能流量分配
    - 协议优先策略

    ---

    ### 数据中心特性
    **VXLAN配置**：
    - 基于VXLAN的Overlay网络
    - BGP EVPN控制平面
    - VTEP终端自动发现

    **堆叠技术对比**：
    | 特性        | 华为CSS/VS | 锐捷VSU | 新华三IRF2 |
    |-------------|------------|---------|------------|
    | 最大成员数   | 2-16       | 2-4     | 2-32       |
    | 分裂检测     | BFD/ARP    | BFD     | MAD检测    |
    | 配置同步     | 全量同步   | 增量同步| 全量同步   |
    | 升级方式     | 独立升级   | 统一升级| 统一升级   |

    **网络虚拟化**：
    - VDC虚拟设备上下文
    - VRF路由隔离
    - 服务链技术
    """)

# 配置示例扩展
with st.expander("💡 高级配置示例", expanded=False):
    st.markdown("""
    ## 多厂商高级配置示例

    ### OSPF多区域认证配置
    **华为**：
    ```bash
    router id 1.1.1.1
    ospf 1 router-id 1.1.1.1
     area 0
      authentication-mode md5 1 cipher Huawei@123
      network 10.1.0.0 0.0.255.255
     area 1
      authentication-mode hmac-md5 1 cipher Secure@2023
      network 10.2.0.0 0.0.255.255
      stub no-summary  # 完全末节区域
    ```

    **锐捷**：
    ```bash
    router ospf 1
     router-id 2.2.2.2
     area 0 authentication message-digest
     message-digest-key 1 md5 Ruijie@456
     network 172.16.0.0 0.0.255.255 area 0
     area 1 authentication
     area 1 stub no-summary
     network 172.17.0.0 0.0.255.255 area 1
    ```

    **新华三**：
    ```bash
    ospf 1 router-id 3.3.3.3
     area 0
      authentication-mode hmac-md5 1 cipher H3C@789
      network 192.168.0.0 0.0.255.255
     area 1
      authentication-mode simple 1 cipher Basic@Pass
      network 192.169.0.0 0.0.255.255
      nssa  # 次末节区域
    ```

    ---

    ### BGP路由策略配置
    **华为路由映射**：
    ```bash
    route-policy POLICY1 permit node 10
     if-match ip-prefix PREFIX1
     apply community 65001:100
    bgp 65001
     peer 10.1.1.1 route-policy POLICY1 export
    ip ip-prefix PREFIX1 index 10 permit 192.168.0.0 16
    ```

    **锐捷路由过滤**：
    ```bash
    ip as-path access-list 10 permit ^65002_
    route-map FILTER permit 10
     match as-path 10
    router bgp 65001
     neighbor 172.16.1.1 route-map FILTER in
    ```

    **新华三团体属性**：
    ```bash
    route-policy COMM_POLICY permit node 10
     apply community 65001:200
    bgp 65001
     peer 192.168.1.1 route-policy COMM_POLICY export
    ```

    ---

    ### VXLAN数据中心配置
    **华为EVPN VXLAN**：
    ```bash
    bridge-domain 10
     vxlan vni 10010
    evpn
     vpn-instance EVPN1 evpn
      route-distinguisher 100:1
      vpn-target 1:1 export-extcommunity
      vpn-target 1:1 import-extcommunity
    interface Nve1
     source 1.1.1.1
     vni 10010 head-end peer-list 2.2.2.2
    bgp evpn
     peer 2.2.2.2 as-number 65001
     peer 2.2.2.2 connect-interface Loopback0
    ```

    **新华三VXLAN集中网关**：
    ```bash
    interface Vsi-interface10
     ip address 10.10.10.1 255.255.255.0
     mac-address 0001-0001-0001
    vsi VSI10
     gateway vsi-interface 10
     vxlan 10010
    l2vpn
     bridge-group 1
      interface GigabitEthernet1/0/1
      interface GigabitEthernet1/0/2
    ```

    ---

    ### 安全防护配置示例
    **端口安全综合防护**：
    ```bash
    # 锐捷配置示例
    interface GigabitEthernet 0/1
     switchport port-security
     switchport port-security maximum 5
     switchport port-security violation restrict
     switchport port-security aging time 60
     switchport port-security aging type inactivity
     switchport port-security mac-address sticky
    ```

    **动态ARP检测(DAI)**：
    ```bash
    # 华为配置示例
    arp anti-attack validate dhcp enable
    arp anti-attack validate dhcp snooping enable
    vlan 10
     arp anti-attack validate check sender-mac
    ```

    **IP源防护(IPSG)**：
    ```bash
    # 新华三配置示例
    dhcp snooping enable vlan 10
    interface GigabitEthernet1/0/1
     ip verify source ip-address mac-address
     dhcp snooping binding record
    ```

    ---

    ### QoS高级配置
    **新华三层次化QoS**：
    ```bash
    traffic classifier VOICE operator and
     if-match dscp ef
    traffic classifier VIDEO operator and
     if-match dscp af41
    traffic behavior VOICE
     queue ef bandwidth pct 30
    traffic behavior VIDEO
     queue af bandwidth pct 40
    qos policy HQOS
     classifier VOICE behavior VOICE mode hierarchical
     classifier VIDEO behavior VIDEO mode hierarchical
    interface GigabitEthernet1/0/1
     qos apply policy HQOS inbound hierarchical
    ```

    **华为CBQoS**：
    ```bash
    traffic classifier VOICE
     if-match dscp ef
    traffic behavior VOICE
     queue ef bandwidth pct 30
    traffic policy CBQOS
     classifier VOICE behavior VOICE
    interface GigabitEthernet0/0/1
     traffic-policy CBQOS inbound
    ```

    ---

    ### 网络运维配置
    **NetFlow/sFlow监控**：
    ```bash
    # 锐捷sFlow配置
    sflow collector 192.168.100.100 6343
    sflow sampling-rate 1000
    sflow polling-interval 30
    interface GigabitEthernet 0/1
     sflow enable
    ```

    **Telemetry流式监控**：
    ```bash
    # 华为Telemetry配置
    telemetry
     destination-group NETMON
      ipv4-address 192.168.100.100 port 10001 protocol grpc
     sensor-group INTERFACE
      sensor-path huawei-ifm:ifm/interfaces/interface
     subscription SUB1
      sensor-group INTERFACE sample-interval 5000
      destination-group NETMON
    ```

    **日志统一管理**：
    ```bash
    # 新华三Syslog配置
    info-center enable
    info-center loghost 192.168.100.100 facility local5
    info-center source default loghost level warning
    info-center timestamp loghost date precision-time
    ```
    """)