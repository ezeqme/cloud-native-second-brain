---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Randy Abernethy", "RX-M LLC"]
sched_url: https://kccnceu2022.sched.com/event/ytrV/kubernetes-networking-101-randy-abernethy-rx-m-llc
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Networking+101+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes Networking 101 - Randy Abernethy, RX-M LLC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Randy Abernethy, RX-M LLC
- Schedule: https://kccnceu2022.sched.com/event/ytrV/kubernetes-networking-101-randy-abernethy-rx-m-llc
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Networking+101+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes Networking 101.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrV/kubernetes-networking-101-randy-abernethy-rx-m-llc
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Networking+101+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cUGXu2tiZMc
- YouTube title: Kubernetes Networking 101 - Randy Abernethy, RX-M LLC
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-networking-101/cUGXu2tiZMc.txt
- Transcript chars: 80551
- Keywords: cluster, create, ingress, traffic, little, network, running, networking, mesh, container, deployment, balancer, install, address, another, virtual, controller, everything

### Resumo baseado na transcript

alrighty i believe it is time for us to kick this off so we have so much to cover i'm going to go ahead and start feel free to keep on coming if you're waiting in line there's lots of seats up front here so yeah welcome welcome my name is randy abernathy i'm a managing partner at rxm and this is kubernetes networking 101. left yeah oh cool all right all right i just started the kubernetes install on my well i just grabbed a sheet just like you guys so i'm ssh din i'm running the kubernetes install it's installing docker first we're using docker that's the runtime example we're going to look at next there's the service bucket where services live there's some other buckets but this is the most important one and then name spaces are a thing in kubernetes right if i want dev and production if i want team flavors in kubernetes right and of course i mean as you guys know there's there's a lot more to know but the lab does start you down the road hopefully is you know pulling away the veil on some of the more confusing bits and example of configuring a gateway that's a custom resource definition it's not part of kubernetes but kubernetes gives you the ability to create your own resource definitions like this one and this one gives you the ability then to do things like inject headers and

### Excerpt da transcript

alrighty i believe it is time for us to kick this off so we have so much to cover i'm going to go ahead and start feel free to keep on coming if you're waiting in line there's lots of seats up front here so yeah welcome welcome my name is randy abernathy i'm a managing partner at rxm and this is kubernetes networking 101. so um let me just see a quick show of hands how many people would consider themselves very savvy kubernetes networking people all right so everybody else if you saw someone raise their hand you got questions you know where to go right those people um so yeah this is going to be a super fun tutorial we have 90 minutes we have a ton of stuff to cover and i'll just give you a quick intro to the format um we've stood up uh hundreds of machines in a cloud provider who shall remain nameless since they wouldn't sponsor us um and so you guys can um ssh into the box that you were um provided on this sheet now i realize that we're on conference wi-fi right we all know what that means it's probably really banging great wi-fi but there's 200 300 people trying to use it all at the same time so the best thing that we could do is instead of you downloading all sorts of packages and and containers and stuff that would be really slow you can just ssh to these cloud instances and send a few characters back and forth every once in a while it's the lowest bandwidth thing that we can come up with for a session like this it's also really great because if you completely thrash this computer your laptop is still fine right so don't worry right it's a virtual machine and if you do completely thrash this computer we have spares so um i have three um folks helping me today um chris ilion and valentin and chris is by the way doing a talk at sixteen hundred coop cuddle said what which is gonna be super awesome so i would go to that if i were you um but those guys are gonna come around and help with questions so if you have a question raise your hand those guys will be scanning the room they'll come to you they can give you a new machine if you need it we got spares they can help you get unstuck if you're working on a part of the tutorial that isn't working we've tested it a bunch of times so i feel pretty good about if you read the tutorial steps carefully and do them the way that they say it's going to work so hopefully we won't have too many problems but we're here to help if you have any questions at all feel free to ask yeah a question ah great great question so
