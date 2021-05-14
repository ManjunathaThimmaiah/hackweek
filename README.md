
Project sends AIOHTTP requests to sites to check the status of the the availibility and if the regex is provided it checks against the response body.
The collected stats will be sent through kafka producer. The kafka consumer reads the topic and writes requred data into the PostgresSQL database.

Architeture:


- Monitor any website
- Check - using regular expression - if a particular item is present on the site
- Publish website health stats (response_code, response_time etc) to Kafka
- Receive stats from Kafka and insert to database

### **Running project**
- #### Step 1: Clone repo
    First you need to clone the repo to your local

    - Clone with SSH:
        ```
        git@github.com:ManjunathaThimmaiah/hackweek.git
        ```
        OR

    - Clone with HTTPS:
        ```
        https://github.com/ManjunathaThimmaiah/hackweek.git
        ```
- #### **Step 2: Setting up envionment variables**
  

Add below DB config to the config file under services/common/config.py

    dbhost: str = ''
    dbport: int = ''
    dbname: str = ''
    dbuser: str = ''
    dbpass: str = ''

    
#### **Running code through python**
The application can be run directly through python after fullfilling the above mentioned configuration:


- **Set the python path**

    ```
    export PYTHONPATH="${PYTHONPATH}:/users/username/projectmainpath/"
    ```
 

- **Create and activate a virtual environment**

    Run this command to create a virtual environment
    ```
    python3 -m venv myproject
    ```
    Switch to virtual environemt by activating followed command
    ```
    source myproject/bin/activate
    ```
- **Install dependencies**

    Enter the project folder and run below command to install all dependencies
    ```
    pip install -r requirements.txt
    ```
- **Run Project** 
    To collect fresh stats from the webmonitoring run the kafka producer run the program:
    ```
    python3 aiven/application.py
    ```
 

### Start kafka consumer
Since project is under construction running kafka consumer needs little tweek and need to be run in different terminal by commenting aiven() method calling within applicatio.py and run

```
python3 aiven/application.py
```


### Project is very basic construction and below things can be considered


  - Exception handling, logger, tests needs attention

- The project can be dockerised

- Monitoring multiple websites

- Better documentation
