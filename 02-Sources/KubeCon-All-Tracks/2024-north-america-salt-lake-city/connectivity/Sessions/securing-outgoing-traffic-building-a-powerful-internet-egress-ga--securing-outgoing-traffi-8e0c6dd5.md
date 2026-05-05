---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["AI ML", "Networking"]
speakers: ["Edie Yang", "Akshita Agarwal", "Airbnb"]
sched_url: https://kccncna2024.sched.com/event/1i7ps/securing-outgoing-traffic-building-a-powerful-internet-egress-gateway-for-reliable-connectivity-edie-yang-akshita-agarwal-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Outgoing+Traffic%3A+Building+a+Powerful+Internet+Egress+Gateway+for+Reliable+Connectivity+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Securing Outgoing Traffic: Building a Powerful Internet Egress Gateway for Reliable Connectivity - Edie Yang & Akshita Agarwal, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Edie Yang, Akshita Agarwal, Airbnb
- Schedule: https://kccncna2024.sched.com/event/1i7ps/securing-outgoing-traffic-building-a-powerful-internet-egress-gateway-for-reliable-connectivity-edie-yang-akshita-agarwal-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Outgoing+Traffic%3A+Building+a+Powerful+Internet+Egress+Gateway+for+Reliable+Connectivity+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Securing Outgoing Traffic: Building a Powerful Internet Egress Gateway for Reliable Connectivity.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ps/securing-outgoing-traffic-building-a-powerful-internet-egress-gateway-for-reliable-connectivity-edie-yang-akshita-agarwal-airbnb
- YouTube search: https://www.youtube.com/results?search_query=Securing+Outgoing+Traffic%3A+Building+a+Powerful+Internet+Egress+Gateway+for+Reliable+Connectivity+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zGN5eCJ-DxE
- YouTube title: Securing Outgoing Traffic: Building a Powerful Internet Egress Gateway for Re... E. Yang, A. Agarwal
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/securing-outgoing-traffic-building-a-powerful-internet-egress-gateway/zGN5eCJ-DxE.txt
- Transcript chars: 31745
- Keywords: gateway, client, traffic, listener, destination, egress, erress, connect, control, filter, internet, network, request, filters, envoy, transparent, connection, mesh

### Resumo baseado na transcript

let's get started hi everyone Welcome to our session on securing outgoing traffic so let's take a deep breathe and just have fun so just a bit of introduction about ourselves my name is Ed I'm a software engineer working on working at Airbnb on the cloud infer team so you might have guessed I am a cat person I love I love cats I have three lovely cats and my hobbies in ler time includes basketball dancing singing and I actually try a lot of different things and here

### Excerpt da transcript

let's get started hi everyone Welcome to our session on securing outgoing traffic so let's take a deep breathe and just have fun so just a bit of introduction about ourselves my name is Ed I'm a software engineer working on working at Airbnb on the cloud infer team so you might have guessed I am a cat person I love I love cats I have three lovely cats and my hobbies in ler time includes basketball dancing singing and I actually try a lot of different things and here together with me is my uh dear teammate a yeah hi everyone my name is akitt and along with Ed I'm a sov engineer at the cloud infrastructure team at Airbnb and U I'm a hiking Enthusiast and almost everything outdoors including biking paddle boarding Etc and you can see the in the photo we have the Mighty mount rer in my back and yeah just like my hike up this mountain the igis Gateway Journey was hard but very rewarding for me and I'm really excited to share it with you today cool so let's jump into the topic we have today so we will go by what is egress why do you need a egress and how in the how section I will firstly talk from a high level perspective on several architectures and then uh choices and then AKA will take a deep dive into one specific solution that we chose using Envoy cool let's just quickly go through what is e Gateway by definition an EG Gateway is a mechanism that manages and outbound traffic to access the comp Network it's a pair of concept with Ingress and then which the Ingress just take the inbound traffic so egress is just the opposite direction of that which taking care of the traffic leaving your network and that Concept in mind internet equ Skateway is basically an e that manages traffic going to inter a public internet that's what we call it internet eway sorry internet e Gateway and so now can you think of any examples of egress in general yeah there are actually many so controlling egress traffic isn't something new or specific to Cloud it's actually quite a fundamental TCH step and there are many technology exist to help with that for example you may have heard of BNS firewall AWS net Gateway or even some open source project like n voice with proy all of these are erress or can be used as an erress but just operating at different level of net Network stack for example some provide lower uh level support like IP based control where others provide more L7 control and htd host and each of them have Pro cons so h a holistic ER solution often combines various of contr
