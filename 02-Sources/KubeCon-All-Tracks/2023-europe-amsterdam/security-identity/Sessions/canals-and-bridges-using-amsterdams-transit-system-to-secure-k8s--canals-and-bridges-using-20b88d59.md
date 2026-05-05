---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["AI ML", "Security", "Networking"]
speakers: ["Cailyn Edwards", "Shopify"]
sched_url: https://kccnceu2023.sched.com/event/1HyQ9/canals-and-bridges-using-amsterdams-transit-system-to-secure-k8s-networks-cailyn-edwards-shopify
youtube_search_url: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+Canals+and+Bridges%3A+Using+Amsterdam%E2%80%99s+Transit+System+To+Secure+K8s+Networks+CNCF+KubeCon+2023
slides: []
status: parsed
---

# 🦝 Canals and Bridges: Using Amsterdam’s Transit System To Secure K8s Networks - Cailyn Edwards, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[AI ML]], [[Security]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Cailyn Edwards, Shopify
- Schedule: https://kccnceu2023.sched.com/event/1HyQ9/canals-and-bridges-using-amsterdams-transit-system-to-secure-k8s-networks-cailyn-edwards-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+Canals+and+Bridges%3A+Using+Amsterdam%E2%80%99s+Transit+System+To+Secure+K8s+Networks+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre 🦝 Canals and Bridges: Using Amsterdam’s Transit System To Secure K8s Networks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyQ9/canals-and-bridges-using-amsterdams-transit-system-to-secure-k8s-networks-cailyn-edwards-shopify
- YouTube search: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+Canals+and+Bridges%3A+Using+Amsterdam%E2%80%99s+Transit+System+To+Secure+K8s+Networks+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N1XvgWXnEik
- YouTube title: 🦝 Canals and Bridges: Using Amsterdam’s Transit System To Secure K8s Networks - Cailyn Edwards
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/canals-and-bridges-using-amsterdams-transit-system-to-secure-k8s-netwo/N1XvgWXnEik.txt
- Transcript chars: 32334
- Keywords: network, security, traffic, canals, cluster, amsterdam, access, policy, pretty, single, bridges, infrastructure, policies, defense, issues, likely, important, information

### Resumo baseado na transcript

so thank you so much for coming um I really appreciate it I know the end of the first day is pretty tough probably a lot of folks in this room are still jet lagged so I really really appreciate you making it to be here so um today we're going to use the canals and bridges of Amsterdam to map out uh kubernetes networks and use it to form a security strategy and I have a clicker um so who am I uh you just heard a little bit

### Excerpt da transcript

so thank you so much for coming um I really appreciate it I know the end of the first day is pretty tough probably a lot of folks in this room are still jet lagged so I really really appreciate you making it to be here so um today we're going to use the canals and bridges of Amsterdam to map out uh kubernetes networks and use it to form a security strategy and I have a clicker um so who am I uh you just heard a little bit about it but I'm Kalyn I've been at Shopify for almost five years I contribute to six CLI and Sig security I'm also a cncf Ambassador this is my first year and when I'm not doing this I um used to be a farmer I am still a squash player I sew I make a lot of my clothing not today because I want it to look nice but sometimes and like a whole bunch of people thanks to the pandemic I am a reluctant Runner uh oh gosh one second this is the my speaker note for this is easy peasy okay sweet oh gosh this is my really great diagram to show why this talk is super awesome obviously you can see that kubernetes was meant to be their coupon was meant to be in Amsterdam um I chose this analogy because I think it's really fun I've always enjoyed talks that focus on the host cities I think it's a great way to learn about the city because often this conference takes all the time and you have all the fun parties in the evening so you don't really get to explore and enjoy the city so hopefully this talk you could leave knowing some things about Amsterdam that maybe you wouldn't have known otherwise and then the technical topic is as kubernetes Security Professionals or new to kubernetes folks or people who are just interested in learning about kubernetes it's very likely that many times in our careers we're going to be presented with a new network and we're going to have to get to know this network and get up to speed with it so that we can see if there are any security vulnerabilities or concerns I think that um what we're going to do in this talk which is Going Back to Basics is really useful and it's really important so that we can get knowledge about a system and often we're so excited to learn the really deep technical stuff that we skip out on some of those basics so let's walk through the process and hopefully each of you will learn something along the way sweet okay so here's our agenda we're going to start off by working that metaphor pretty close to death and then we're going to get to know kubernetes Network so I'm going to go over I did was not b
