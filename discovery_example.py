#All necessary imports are taken from the pm4py package
import pm4py

#Import the running example from the term paper; Can be every other OCEL file
ocel = pm4py.read_ocel_xml("running_example.xmlocel")

#Print the log to see everything is loaded and formatted correctly
print(ocel.get_extended_table())

#Discovery the object-centric Petri net from our running example
model = pm4py.discover_oc_petri_net(ocel)

#Let's have a look at the discovered model
pm4py.view_ocpn(model)


#To use traditional Petri net discovery algorithms, we need to flatten the OCEL log for each object type
flatten_ticket = pm4py.ocel_flattening(ocel, "ticket")

flatten_agent = pm4py.ocel_flattening(ocel, "agent")

flatten_meeting = pm4py.ocel_flattening(ocel, "meeting")

#Let's discover and show Petri nets for each object type
net, initial, final = pm4py.discovery.discover_petri_net_inductive(flatten_ticket)
pm4py.vis.view_petri_net(net, initial, final)

net, initial, final = pm4py.discovery.discover_petri_net_inductive(flatten_agent)
pm4py.vis.view_petri_net(net, initial, final)

net, initial, final = pm4py.discovery.discover_petri_net_inductive(flatten_meeting)
pm4py.vis.view_petri_net(net, initial, final)