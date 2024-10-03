# Security-Event-Simulation-and-Analysis
Setting Up a Home Lab with Elastic SIEM and Kali Linux: A Step-by-Step Guide
In this guide, we’ll walk through creating a Security Information and Event Management (SIEM) lab using Elastic Stack on the Elastic Cloud and a Kali Linux virtual machine (VM). This project is great for hands-on learning. This hands-on experience allowed me to dive into the world of security monitoring, event logging, and incident response using a practical, real-world environment. Here's a brief overview of the process I followed and the key learnings I gathered along the way.

1. Creating an Elastic Cloud Deployment
I began by setting up a free Elastic account to create a cloud-based deployment of Elasticsearch. After selecting the appropriate deployment size and region, I configured the environment to serve as the backbone for the SIEM setup. This allowed me to leverage Elastic’s powerful search and analytics features for security event monitoring.
To begin, I registered at https://cloud.elastic.co/registration and logged into the Elastic Cloud console.
Clicked on Create Deployment and waited for the process to complete.
Upon setup completion, I clicked Continue to finalize the deployment.


2. Setting Up a Kali Linux Virtual Machine
Next, I configured a Kali Linux VM using Oracle VirtualBox, a platform I’m comfortable with. Kali’s robust suite of security tools made it the ideal operating system for generating test events and monitoring network activity. This environment played a crucial role in simulating attacks and forwarding the corresponding logs to Elastic.

3. Installing the Elastic Agent to Collect Logs
To capture and forward security events from Kali to Elastic SIEM, I installed the Elastic Agent on the VM. This lightweight agent effectively gathered and transmitted security-related data, such as those generated during Nmap scans, directly to Elastic for analysis.
   Once the agent was installed, I confirmed it was properly forwarding logs by checking its status by using command: sudo systemctl status elastic-agent.service 




     Add integration> Elastic defend>Add Elastic defend> complete all the information

    ![img3.1](/Images/3.1.png)
    ![img3.1](/Images/3.2.png)
    ![img3.1](/Images/3.3.png)
     After installing the Elastic Agent, I was directed to a page with commands that I copied and executed in the Kali terminal.
     ![img3.1](/Images/3.4.png)


4. Generating Security Events Using Nmap
To simulate real-world network traffic, I ran a series of Nmap scans on the Kali machine. This generated various security events like open port detections, operating system information, and service details. These events provided valuable insights into network behavior, which were then reflected in the SIEM for analysis.
5. Querying Security Events in the SIEM
Once the data was flowing, I used Elastic's powerful search capabilities to query the logs. For example, I ran queries to detect Nmap scan activities and other processes running with elevated privileges. This helped me understand how Elastic SIEM logs events in real time and how to quickly filter through massive amounts of data to isolate critical security events.
To review security events and run queries, I navigated to the "Logs" section, found under the "Observations" tab on the left panel. This area became a hub for monitoring live data, allowing me to filter through logs and pinpoint key security incidents. It felt like diving into the heartbeat of the system, where every event—whether a scan, a login, or a service activity—was recorded in real time. With the tools available, I could easily isolate critical data and analyze the network's activity as it unfolded.

    ![img3.1](/Images/5.1.png)
    ![img3.1](/Images/5.2.png)




6. Building a Custom Dashboard
To visualize the collected security data, I created a custom dashboard in the Elastic web portal. This involved designing charts that plotted event counts over time, providing a clear, graphical representation of security incidents. The dashboard allowed me to monitor trends and spot anomalies, enhancing my ability to interpret and present security metrics.
Click on the menu icon in the top-left corner, then navigate to “Analytics” and select “Dashboards.”

    ![img3.1](/Images/6.1.png)




    To create a new dashboard, click "Create dashboard" and then "Create Visualization." Choose either “Area” or “Line” as your preferred visualization type. For the configuration, set the visualization to 
    "Area," use "Timestamp" for the horizontal axis, and "Count" for the vertical axis.
    Once you're satisfied with the settings, click the “Save” button to store the visualization and finalize the remaining configurations.

    ![img3.1](/Images/6.2.png)





7. Setting Alerts for Security Incidents
Finally, I configured alerts within the SIEM to trigger notifications when specific conditions, such as Nmap scans, were detected. By creating custom rules, I set up real-time alerts that would notify me of potential security threats, a crucial aspect of incident response in a professional setting.



    Click on the menu icon in the top-left corner, then navigate to “Security” and select “Alerts.” In the top-right corner, click on “Manage rules.”
    Next, go to "Manage rules" > "Create new rule" > "Define rule" > "Custom query."
    After configuring the remaining settings, click "Continue."
    Finally, click the “Create and enable rule” button to activate the alert.
    For instance, I created an Nmap alert, which triggers whenever an Nmap scan event is detected, executing the designated action automatically.

    ![img3.1](/Images/7.1.png)





















