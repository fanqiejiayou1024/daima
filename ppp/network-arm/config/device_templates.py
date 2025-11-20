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
                "shutdown": ["", "shutdown"]
            }
        },
        "VLAN配置": {
            "template": "vlan {vlan_id}\n description {description}",
            "params": {
                "vlan_id": ["10", "20", "30"],
                "description": "销售部VLAN"
            }
        },
        # ... 其他模板保持不变 ...
    },
    "锐捷": {
        # ... 同上 ...
    },
    "新华三": {
        # ... 同上 ...
    }
}

def get_common_config_types():
    all_types = [set(device_templates[vendor].keys()) for vendor in device_templates]
    common = set.intersection(*all_types)
    core_types = {"接口配置", "VLAN配置", "OSPF配置", "BGP配置", "VRRP配置"}
    return list(common | core_types)
