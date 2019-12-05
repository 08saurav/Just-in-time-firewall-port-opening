# Just-in-time-firewall-port-opening
suggest a method to block third parties intruption using just-in-time firewall opening

Design a method to transfer data from one server to another
located in the same data center, physically close enough, in a secure manner. Use just-in-time
dynamically opened firewall connections and ports using on-the-spot whitelisting of a specified
(source) server on another (target) server, valid exactly for the time-window of the data transfer,
where the data is transferred using on-the-fly encryption negotiated between the server pair at
the runtime. Simulate transferring the request to open the data, using a different ad-hoc open
port, potentially over a (simulated) separate network (in real implementations, it will be a 5G or
some other random network) in order to prevent easy listening of the port opening
announcement by third parties.

# detailing about varoius approach while i made to reach my answer
1. with my basic knowledge i first think of client server code that i will implement and send to firewall that will send to actual server but this approach has various demerits such as encryption decrytion overhead and many other ways that is will open to attacker

client.py -simple code to send data to another ec2 instance(server)

server.py - simple code to recieve data from client 
2. we move to this approach using ssh  
this work done by us for checking firewall restrictions and firewall implementations 
this firewall we made will accept through only ssh services and limit the parallel access and limit to sertain ip at the same time 

using this we can just stop any unauthorized ip to acess to our document 

we are using ssh i.e scp command for secure and encrypted transmission of data to our server in this data is send through the ssh port encrypted while when when it recieved by srver it automatically decrypted and save to server

first i will create inbuilt agent for scp so it will use that agent to connect to ssh to server
In cloud i have mentioned all procedure of adding agent and send file to server
# work done by us is already shown to firdaus sir and all worked done according to him
