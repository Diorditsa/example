def pretty_log_browser(log_dict):
    log_var = ""
    if log_dict is None:
        return "can't grab logs console, she must be empty"
    else:
        for item in log_dict:
            log_var += f"\n{str(item)}"
        return log_var