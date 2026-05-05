---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Networking", "SRE Reliability"]
speakers: ["Saadi Myftija", "Netlight"]
sched_url: https://kccnceu2024.sched.com/event/1YeRW/iot-and-websockets-in-k8s-operating-and-scaling-an-ev-charging-station-network-saadi-myftija-netlight
youtube_search_url: https://www.youtube.com/results?search_query=IoT+and+WebSockets+in+K8s%3A+Operating+and+Scaling+an+EV+Charging+Station+Network+CNCF+KubeCon+2024
slides: []
status: parsed
---

# IoT and WebSockets in K8s: Operating and Scaling an EV Charging Station Network - Saadi Myftija, Netlight

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Networking]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Saadi Myftija, Netlight
- Schedule: https://kccnceu2024.sched.com/event/1YeRW/iot-and-websockets-in-k8s-operating-and-scaling-an-ev-charging-station-network-saadi-myftija-netlight
- Busca YouTube: https://www.youtube.com/results?search_query=IoT+and+WebSockets+in+K8s%3A+Operating+and+Scaling+an+EV+Charging+Station+Network+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre IoT and WebSockets in K8s: Operating and Scaling an EV Charging Station Network.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRW/iot-and-websockets-in-k8s-operating-and-scaling-an-ev-charging-station-network-saadi-myftija-netlight
- YouTube search: https://www.youtube.com/results?search_query=IoT+and+WebSockets+in+K8s%3A+Operating+and+Scaling+an+EV+Charging+Station+Network+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CuiY1Vj-A5E
- YouTube title: IoT and WebSockets in K8s: Operating and Scaling an EV Charging Station Network - Saadi Myftija
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/iot-and-websockets-in-k8s-operating-and-scaling-an-ev-charging-station/CuiY1Vj-A5E.txt
- Transcript chars: 29714
- Keywords: database, connection, stations, basically, charging, station, little, websocket, architecture, spikes, platform, connections, reconnect, release, another, couple, earlier, happens

### Resumo baseado na transcript

okay I think we can start um hi everyone uh my name is s and today I'll will be talking about websockets and scalability challenges related to them um let me start with an image from an incident we had some time ago yeah um it was a long Friday we we had to stay until 2: a.m. uh but we eventually fixed the issue uh the alternative would have been to quit our jobs and move to another city we we didn't do that fortunately and we had a lot of learnings in this incident but most importantly it was a wakeup

### Excerpt da transcript

okay I think we can start um hi everyone uh my name is s and today I'll will be talking about websockets and scalability challenges related to them um let me start with an image from an incident we had some time ago yeah um it was a long Friday we we had to stay until 2: a.m. uh but we eventually fixed the issue uh the alternative would have been to quit our jobs and move to another city we we didn't do that fortunately and we had a lot of learnings in this incident but most importantly it was a wakeup call for us that we need to improve the scalability of our system and the reliability um you might be wondering what's what's happening here but before I go into more details um let me say a couple words about myself uh so I'm s I'm a software engineer and consultant at netlight netlight is a tech consulting company based in Europe um I focused mostly on cloud engineering uh Cloud architecture site reliability engineering and more recently I've also gotten interested in developer experience topics u in my free time I enjoy uh basketball photography and usually Fridays without pag duty calls um in this talk uh I'll be talking about uh electric vehicle charging just to set some context some Basics then then I will jump into websockets and scalability challenges and actual concrete problems that we we faced in our platform and finally our approach uh and how we addressed these uh challenges so let's start with the first one some context about uh EV charging um let's do a quick show of hand so how many of you have driven an electric car already what that's quite a lot more than half that's nice then maybe you are already familiar with with some of the frustrations with with charging electric cars let's take a look what that uh looks like so the EV driver would plug in their car into a charging station and the charging station is of course connected to the electrical grid but also it has an internet connection Via mobile carrier and it uses this internet connection to communicate to a system which is called a charging Point operator it communicates uh via OC PP messages it's just a a protocol that standardizes uh the how the messages should look like and the flow should look like it's an open standard and it makes it possible to operate uh stations from different vendors the charging Point operator is a system that companies that are interested in offering EV charging solutions would build and in the couple in the last couple of years I've been leading a platform
