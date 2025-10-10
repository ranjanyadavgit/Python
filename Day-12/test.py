def update_server_config(file_path,key,value):

  #READ the existing content of the server existing file
  with open("file_path","r") as file:
    lines=files.readlines()

 #update the configuration value for the specified key
with open("file_path","w") as file:
   for line in lines:
     #check if the line starts with the specified key
     if key in line
      file.write(key + "=" + value + "\n")
     else
      # keep the file as it is
      file.write(line)

# update_server_config(server_config_file, key_to_update,new_value)
 update_server_config(file_path,"MAX_CONNECTIONS","3000")   
