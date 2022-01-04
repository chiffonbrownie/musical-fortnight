# layout of photo server


## Problem
What am i trying to solve
* be able to have a server accept clients over a networkand be able to log meta data about a client,  any media they send as well as what other clients they interact with


## Requirements
### what should it do
server 
* run
* display colorful startup message (bc why not)
* log data about startup
* check if errors occured on previous run and print to stdout
* accepts clients
* print out data of clients upon login
* allow users to login with distinct username
* remove user if they error out / log out
* loop if nondistinct login given
* allow user to select other user to send media with file name(s) and metadata

client
* connect to server
* check user names
* login
* allow user to select source folder
* allow user to select destination folder
* allow user to select one photo or multiple or folder with recursive option

### what it shouldn't do
* 

### potential issues
* 


## test set
* small batch of photos


## bonus features
### tests
* allow for automatic testing of results to confirm if i did anything right

### others
* allow installation of extensible code to provide more / other functionality
* provide cli option for client to script out transfer
    * use unique login based on some local hashed value as login name to prevent loop of present usernames