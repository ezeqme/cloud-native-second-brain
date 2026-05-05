---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Networking"]
speakers: ["Peter ONeill", "Ambassador Labs"]
sched_url: https://kccncna2021.sched.com/event/lV6A/from-network-engineer-to-k8s-developer-lessons-learned-via-telepresence-peter-oneill-ambassador-labs
youtube_search_url: https://www.youtube.com/results?search_query=From+Network+Engineer+to+K8s+Developer%3A+Lessons+Learned+via+Telepresence+CNCF+KubeCon+2021
slides: []
status: parsed
---

# From Network Engineer to K8s Developer: Lessons Learned via Telepresence - Peter ONeill, Ambassador Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]]
- País/cidade: United States / Los Angeles
- Speakers: Peter ONeill, Ambassador Labs
- Schedule: https://kccncna2021.sched.com/event/lV6A/from-network-engineer-to-k8s-developer-lessons-learned-via-telepresence-peter-oneill-ambassador-labs
- Busca YouTube: https://www.youtube.com/results?search_query=From+Network+Engineer+to+K8s+Developer%3A+Lessons+Learned+via+Telepresence+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre From Network Engineer to K8s Developer: Lessons Learned via Telepresence.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6A/from-network-engineer-to-k8s-developer-lessons-learned-via-telepresence-peter-oneill-ambassador-labs
- YouTube search: https://www.youtube.com/results?search_query=From+Network+Engineer+to+K8s+Developer%3A+Lessons+Learned+via+Telepresence+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Vfs0vKU10dA
- YouTube title: From Network Engineer to K8s Developer: Lessons Learned via Telepresence - Peter ONeill, Ambassador
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/from-network-engineer-to-k8s-developer-lessons-learned-via-telepresenc/Vfs0vKU10dA.txt
- Transcript chars: 25327
- Keywords: network, actually, networking, working, application, connect, cluster, running, information, simple, forward, troubleshooting, little, specific, native, command, engineer, terminal

### Resumo baseado na transcript

i think we are we are good to go okay welcome everyone thank you for showing up i really appreciate it uh so my name is peter um this is me i'm a community advocate uh for the the oppa project open policy agent i work for styra uh today i'm not talking about those though i'm talking about telepresence uh and kind of just from network engineer to k-8 developer right my journey moving from a network engineer into cades developer and kind of the skills and knowledge that whatever problem was being reported is not here right so okay so that seems fine right maybe maybe i need to dive in a little bit deeper let's uh so let's go back to our port forward here and say okay the service the service wasn't wasn't where my problem was like let's let's take a look at at one of these pods or let's look a little bit closer closer into the application so we'll do ak get i'll see see what's running see what exists uh so then

### Excerpt da transcript

i think we are we are good to go okay welcome everyone thank you for showing up i really appreciate it uh so my name is peter um this is me i'm a community advocate uh for the the oppa project open policy agent i work for styra uh today i'm not talking about those though i'm talking about telepresence uh and kind of just from network engineer to k-8 developer right my journey moving from a network engineer into cades developer and kind of the skills and knowledge that transfers along with that right because network engineering is a lot of troubleshooting following a network path step by step and kind of a lot of that transfers through into kubernetes because you're always trying to go piece by piece to see where things have broken so as i said i'm peter o'neill you can find me just about everywhere at peter o'neill jr tweet me connect with me on linkedin i'd love to hear from you cool so let's start off right simple networking path here once upon a time websites networking very simple you have your home network right connected to your isp connected to some unknown number of middle hops eventually to your your website's isp right very simple networking path and then you have a very simple uh troubleshooting procedure right like this is this is troubleshooting before cloud native right like so you have your your simple your simple website hosted on a public ip probably served on port 80 unencrypted right maybe it's a simple html website right troubleshooting consists of can i ping this house does netcat say that the port is open and available to connect to does nslookup resolve to the right address right like is is dns working for the site right and then your typical your typical fix for this is either you fix dns or you trace route to the end you figure out which hop the path stops at and then you call your isp and say hey fix this it's broken i'm a network engineer and i can see exactly where the path broke right so very simple right then we then we move into the cloud native application right now we have a lot more things right you're hosted in a big cloud provider you might have hosted dns you might have some elastic ips assigned to multiple high availability load balancers you're serving on 443 you're doing tls termination right you're passing this all through into kubernetes which then might hit api gateways and ingresses going through a service message a lot going on now right so so we we we've increased complexity quite a bit right and so now it's no
