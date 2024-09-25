def update_server_config(filepath, key, value):
    with open(filepath,"r") as file :
        lines = file.readlines()
    with open(filepath, "w") as file:
        for line in lines:
            if key in line :
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config_file = 'server.conf'
key_to_update = 'MAX_CONNECTIONS'
new_value = '100'

update_server_config(server_config_file,key_to_update,new_value)