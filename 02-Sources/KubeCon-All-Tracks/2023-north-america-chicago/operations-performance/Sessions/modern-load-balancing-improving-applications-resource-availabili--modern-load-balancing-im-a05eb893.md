---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Antonio Ojea", "Gerrit DeWitt", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2s6/modern-load-balancing-improving-applications-resource-availability-and-performance-antonio-ojea-gerrit-dewitt-google
youtube_search_url: https://www.youtube.com/results?search_query=Modern+Load+Balancing%2C+Improving+Application%27s+Resource+Availability+and+Performance+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Modern Load Balancing, Improving Application's Resource Availability and Performance - Antonio Ojea & Gerrit DeWitt, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Antonio Ojea, Gerrit DeWitt, Google
- Schedule: https://kccncna2023.sched.com/event/1R2s6/modern-load-balancing-improving-applications-resource-availability-and-performance-antonio-ojea-gerrit-dewitt-google
- Busca YouTube: https://www.youtube.com/results?search_query=Modern+Load+Balancing%2C+Improving+Application%27s+Resource+Availability+and+Performance+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Modern Load Balancing, Improving Application's Resource Availability and Performance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2s6/modern-load-balancing-improving-applications-resource-availability-and-performance-antonio-ojea-gerrit-dewitt-google
- YouTube search: https://www.youtube.com/results?search_query=Modern+Load+Balancing%2C+Improving+Application%27s+Resource+Availability+and+Performance+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NlO4uhhQiRw
- YouTube title: Modern Load Balancing, Improving Application's Resource Availability... Antonio Ojea & Gerrit DeWitt
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/modern-load-balancing-improving-applications-resource-availability-and/NlO4uhhQiRw.txt
- Transcript chars: 34088
- Keywords: balancer, connection, application, packet, traffic, network, external, health, tracking, policy, seconds, cluster, packets, little, forward, number, serving, balancing

### Resumo baseado na transcript

hello hello everybody well thank you for coming and my name is Antonio and work at Google I'm kubernetes contributor and JY networking developer I'm going to present with Git about modern law balancing improving application resource availability and performance hi everybody I'm Garrett uh I'm here today uh with Antonio thank you all for for having us and glad to see a good turnout here uh I was joking I said maybe no one would show up so that was sort of a little fear that I had but

### Excerpt da transcript

hello hello everybody well thank you for coming and my name is Antonio and work at Google I'm kubernetes contributor and JY networking developer I'm going to present with Git about modern law balancing improving application resource availability and performance hi everybody I'm Garrett uh I'm here today uh with Antonio thank you all for for having us and glad to see a good turnout here uh I was joking I said maybe no one would show up so that was sort of a little fear that I had but uh hopefully today we'll we'll have a good Deep dive I play a network uh engineer on TV uh work in support engineering at at Google um yeah so why don't we we can get started okay the the way that we are going to organize the talk and I'm going to do a brief summary of touching several to topics about what is lo balancing what problems load balancing soles and G is going to do a more deep dive into the actual problem of load balancing and H cases so the first question is why do you need a load balancer right or why why do when should I need a Lo balancer if you have just an application that is running and you don't care about availability or performance or you don't care about service Discovery for sure you don't need a load balancer but if this is your situation that you care about these things L balance is going to be your best friend in this in this in this journey so before going into the L balancer topic let's do a first stoping what is the networking stack how the application work right so you can see in this diagram you can see two host the host has processor right the processes run and they want to communicate between each other so they send a packet open a socket the packet goes through an application layer this all are abstraction right then the application layer assembles the the TCP packet the TCP packet goes to an IP IP packet and then it creates an packet that goes through the network right and magically this packet happens to appear in the the networking stack of the second host and do the reverse path it start going up on the application ledes and finally go to the other process so what we we have is how how the hell get the packet to the other Pro right because there is some cloud with some devices that are able to get this packets and forward to the right place right and one of these virtual devices is a network Lo balancer uh a network Lo balancer what it simply does is just it gets the pcket and magically is able to forward the packet to another destination
