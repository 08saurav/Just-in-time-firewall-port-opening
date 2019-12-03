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

client.py -simple code to send data to another ec2 instance(server)

server.py - simple code to recieve data from client 

this work done by us for checking firewall restrictions and firewall implementations 
this firewall we made will accept through only ssh services and limit the parallel access and limit to sertain ip at the same time 

using this we can just stop any unauthorized ip to acess to our document 
