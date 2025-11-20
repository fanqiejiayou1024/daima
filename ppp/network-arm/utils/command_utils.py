from config.device_templates import device_templates

def generate_command(vendor, config_type, params):
    template = device_templates[vendor][config_type]["template"]
    for param, value in params.items():
        if isinstance(value, list) and value and value[0] == "":
            template = template.replace("{" + param + "}", "")
        else:
            if isinstance(value, list):
                value = value[0]
            template = template.replace("{" + param + "}", str(value))
    template = "\n".join([line for line in template.splitlines() if line.strip()])
    return template
