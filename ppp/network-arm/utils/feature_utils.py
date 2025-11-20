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

    if "OSPF" in config_type:
        features.append("支持区域认证和接口认证")
        features.append("支持路由汇总")

    if "BGP" in config_type:
        features.append("支持EBGP多跳")
        features.append("支持路由反射器")

    return "\n".join(f"- {f}" for f in features)


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
