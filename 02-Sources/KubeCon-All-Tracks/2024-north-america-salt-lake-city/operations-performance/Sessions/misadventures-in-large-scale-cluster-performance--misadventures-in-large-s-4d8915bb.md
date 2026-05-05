---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Shane Corbett", "AWS", "Dima Ilchenko", "Lacework"]
sched_url: https://kccncna2024.sched.com/event/1i7md/misadventures-in-large-scale-cluster-performance-shane-corbett-aws-dima-ilchenko-lacework
youtube_search_url: https://www.youtube.com/results?search_query=Misadventures+in+Large+Scale+Cluster+Performance+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Misadventures in Large Scale Cluster Performance - Shane Corbett, AWS & Dima Ilchenko, Lacework

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Shane Corbett, AWS, Dima Ilchenko, Lacework
- Schedule: https://kccncna2024.sched.com/event/1i7md/misadventures-in-large-scale-cluster-performance-shane-corbett-aws-dima-ilchenko-lacework
- Busca YouTube: https://www.youtube.com/results?search_query=Misadventures+in+Large+Scale+Cluster+Performance+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Misadventures in Large Scale Cluster Performance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7md/misadventures-in-large-scale-cluster-performance-shane-corbett-aws-dima-ilchenko-lacework
- YouTube search: https://www.youtube.com/results?search_query=Misadventures+in+Large+Scale+Cluster+Performance+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wvpWmWzOPiQ
- YouTube title: Misadventures in Large Scale Cluster Performance - Shane Corbett, AWS & Dima Ilchenko, Lacework
- Match score: 0.781
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/misadventures-in-large-scale-cluster-performance/wvpWmWzOPiQ.txt
- Transcript chars: 30873
- Keywords: control, workload, cluster, controller, scalability, number, second, storage, reconcile, latency, server, seconds, itself, scheduler, volume, objects, minutes, change

### Resumo baseado na transcript

today we start our misadventure off unfortunately with a betrayal I trusted you kubernetes when you told me that this was the kubernetes scalability numbers I took that on Blind Faith so much so that when I started with the cloud provider that I work for and they were like who are we going to find dumb enough to take scalability issues all day I looked that man in the eye and I told him I'm that dumb he looked at me quickly agreed and that became my full-time job

### Excerpt da transcript

today we start our misadventure off unfortunately with a betrayal I trusted you kubernetes when you told me that this was the kubernetes scalability numbers I took that on Blind Faith so much so that when I started with the cloud provider that I work for and they were like who are we going to find dumb enough to take scalability issues all day I looked that man in the eye and I told him I'm that dumb he looked at me quickly agreed and that became my full-time job but quickly there was a problem I would go out to customers as small as 5,000 nodes and I was experiencing the slowness sometimes even crashes meanwhile on the other end of the spectrum I go out to customers had 6,000 nodes running just fine something was wrong now I knew nodes wouldn't be the me best measure of scale cuz they come in all different sizes and usually it's a mix but that was okay because pods pods will tell me what's the best but I would have 10,000 pods that wouldn't talk to the control plane and be longlived and not to have 10,000 pods that might only live for 15 minutes on a spark job and then another in another hour another 10,000 and that's where I would get the crashes okay so wait a minute so nodes and pods don't correlate in any way to if something's going to scale successfully this is a dis disaster gang ever since I was a little Shane I had one dream that was going to grow up one day and I was going to get paid money to nerd Flex on people but now that dream is lying in tatters we've got to figure out how are we going to get to the bottom of kubernetes scalability and with the stage set in the most ridiculous way possible we are going to go all the way down the rabbit hole to understand the true nature of kubernetes scalability my late night crowd are you ready to hit this really hard let me hear it all right it's the late night crowd right there I love it all right gang I had let we start our journey off with the clue it's that spark job I have 10,000 pods I dumped them all on the scheduler that's when I was getting the slowness same number of PODS same number same exact cluster I batch it out just a little bit over time runs is fine it's almost like the rate of change that I'm pushing to the control plane at any point in time seems to be somehow related to kubernetes scalability and that makes a lot of sense if you look at the discrete components in kubernetes each one has its own unique mechanism that controls that rate of change set that value too high we're going to c
