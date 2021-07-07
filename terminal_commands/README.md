#README
#Revised Sniper Algorithm

* Our sniper alog for the trading bot is located at agent/sniper. You could
check it out.


# README
# user permission for kdb, proxy server and agent
## Project structure
### Files
* Our working dir: /home/azureuser/submissions/TeamDnew/robothon-teamD/
* Default KDB data output dir: /home/azureuser/ifs/data/ 
  
  Output path can be modified in configs in python_q_new/utils.py and rabbitmq_receiver/rabbitmq_receiver_config.py
  
#### python_q_new/
* start.sh: automated script to bring up Q ports, proxy server, and RabbitMQ listener 
* end.sh: automated script to save current session data to disk and close down Q ports, proxy server and RabbitMQ listener 
* q_device_server.py, multithread_q_server.py: The Q Device Server that functions like a proxy layer between users and q servers
* test_command.py: Send query commands to proxy server interactively 
* example_save_pnl_rutvik.py: sample code for trading bots to save offline pnl through proxy server
* example_save_pnl.py: sample code for trading bots to save pnl through proxy server
* example_select.py: demo select queries supported by the proxy server
* set_tables.py: script to set current data on proxy server to disk 
* Config file: utils.py

#### rabbitmq_receiver/
* rabbitmq_receiver.py:The RabbitMQ listener. It captures trades data passing exchanges in RabbitMQ, and sends queries to proxy server to create/update/set tables. 
* Config file: rabbitmq_receiver_config.py
* Define table names and columns: init_tables.txt 

## Troubleshooting (Please Read First!)
* Our test proxy server is not in a isolated environment. It will receive **message leaked from running rabbitmq**. You can still do this test at any time, but if you do not want to affect the running rabbitmq, please do this test when rabbitmq is free. 
* Our test proxy server will occupy the corresponding ports: 2060, 2070-2072(kdb), 1234-1235(proxy server). Please make sure that these ports are free when testing. 
* **Attention!** If you find this error,
    ```
    AttributeError: 'NoneType' object has no attribute 'axes'
    ```
    You need to reboot the conda environment for proxy server. That is, run ```conda deactivate``` (maybe 1-2 times) until you go to base environment then run ```conda activate cudf4``` again.
* The ```robothon``` package may not install protobuf and raises error. Please run ```pip install protobuf``` if that happens.
* Currently rabbitmq receiver also needs the username and password to connect to the proxy server. Please check that if proxy server cannot receive message from rabbitmq receiver.
* For one "pickle protocol" error, we manually set the pickle protocol to 4 instead of -1. You can rollback to -1 if you solve the error.

# 1. Test kdb user permission
* Please run ```conda activate cudf4``` and then **test_kdb_permission.ipynb** for interactive test or **test_kdb_permission.py** for normal test in **python_q_new/**.
* The expected result is that the first connection is built and the next two connections are refused for wrong username and password.

# 2. Test proxy server user permission
## Step 1: Setup
* Open 2 terminals to connect to the server. In terminal 1, run ```conda activate cudf4``` to activate environment.
* Store username and md5 encrypted password in ```userpass.txt``` in **python_q_new/**. The existing user is "test:test".
* Run ```./start.sh``` in **python_q_new/** to setup kdb instances, proxy server and rabbitmq receiver.
## Step 2: Function test
### Select
* In terminal 2, activate cudf4 environment and run ```python example_select.py --username test --password test``` to test "select" function in **python_q_new/**.
* The result should have outputs for DEMO1 and DEMO2. DEMO3 DEMO4 should have 'Permission denied' error if you don't have access to history data.
### Upsert
* In terminal 2, run ```python example_save_pnl.py --username test --password test``` to test pnl "upsert" function in **python_q_new/**.
* The result should have correct outputs for operations.
* (Optional) In terminal 2, run ```python example_save_pnl_rutvik.py --username test --password test``` to test off_pnl "upsert" function in **python_q_new/**.
## Step 3: Permission test
* In terminal 2, run the following codes with differnt username and password in **python_q_new/**.
    ```
    python example_select.py  
    python example_save_pnl.py
    python example_save_pnl_rutvik.py # Optional
    ```
* The result should show "Connection denied".
## Step 4: Closing servers
* In terminal 1, run ``` ./end.sh ``` in **python_q_new/** to shutdown servers. The output will show "Permission denied" since we have no permission to save data. Please wait for it until it kills all processes.

# 3. Test agent store user permission remotely
## Step 1: Setup server and remote client
* On the server, run ```conda activate cudf4``` to activate environment.
* Store username and md5 encrypted password in ```userpass.txt``` in **python_q_new/**. The existing user is "test:test".
* Run ```./start.sh``` to setup kdb instances, proxy server and rabbitmq receiver in **python_q_new/**.
* On the remote client, Run ```pip install --index-url http://70.37.98.174:8889/simple/ robothon2021 --trusted-host 70.37.98.174``` to install robothon package.
* Run ```robothon <your_directory>```. It will create 3 files: executionbot.py, simplebot.py, config.py.
## Step 2: Test
* On the remote client, change the port of kdb in ```<your_directory>/config.py``` to **2060**. Change the username and password to "test" and "test". Change the mode to **"remote"**.
* Run ```python executionbot.py```.
* After the agent is done, on the server, run ```python test_store_permission.py``` to see stored records in **python_q_new/**.
* The result should have correct outputs for operations.
## Step 3: Closing servers
* On the server, run ``` ./end.sh ``` to shutdown servers in **python_q_new/**. The output will show "Permission denied" since we have no permission to save data. Please wait for it until it kills all processes.
