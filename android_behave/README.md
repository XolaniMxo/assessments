
# ANDROID AUTOMATION TESTING


**Prerequisites**
=================


# Install Appium


**Steps to install Appium**
===========================

Install node.js without using sudo-

Download latest nodejs https://nodejs.org/download/release/latest/

Install it under/usr/local

    *cd /usr/local
    
Check the installation using:

    * node -v

Install Java, jdk and jre-

    * sudo apt-get update
    * sudo apt-get install default-jre
    * sudo apt-get install default-jdk
    //to install oracle jdk
    * sudo add-apt-repository ppa:webupd8team/java
    * sudo apt-get update
    * sudo apt-get install oracle-java8-installer

 Set JAVA HOME path
 
     //open bashrc file 
     * gedit ~/.bashrc
     * export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
     * export PATH=${PATH}:${JAVA_HOME}/bin
     //run following command to verify the path
     * echo $JAVA_HOME
     * echo $PATH
    
 Download android studio and set the ANDROID HOME path
 
 To open android studio open terminal and install android android sdk
 
     * cd android-studio/bin ./studio.sh
   
  Once android sdk is installed, Set ANDROID HOME path using:
     
     * gedit /.bashrc
     * //add following lines at the end of the file and then save
     * export ANDROID_HOME=/home/user_name/Android/Sdk
     * export PATH=$PATH:/home/user_name/Android/Sdk/tools
     * export PATH=$PATH:/home/user_name/Android/Sdk/platform-tools
  
  Install appium globally
 
     * npm install -g appium
     
 Install appium-doctor to troubleshoot errors
 
     * npm install -g appium-doctor
 
# Install Genymotion (Android Emulator)
    

# Install Python Pip


		* sudo apt-get install python-pip python-dev build-essential 
		* sudo -H pip install --upgrade pip 

# Install Python  Virtualenv

		* sudo -H pip install --upgrade virtualenv 

# Install toolium

		* sudo -H pip install toolium
		* sudo -H pip install git+https://github.com/behave/behave
		
STEPS TO RUN THE TEST ON UBUNTU
================================

# Create a directory on your machine that you will be working from

Clone the github repository into your working directory

		* git clone https://github.com/Xolani-Mxoxozi/Automation-Testing-Demo.git
		
To be able to run the demo, you must run the demo from the parent folder
========================================================================

# open the demo in terminal

		* Working directory

# Run the command 

		* behave android_behave




