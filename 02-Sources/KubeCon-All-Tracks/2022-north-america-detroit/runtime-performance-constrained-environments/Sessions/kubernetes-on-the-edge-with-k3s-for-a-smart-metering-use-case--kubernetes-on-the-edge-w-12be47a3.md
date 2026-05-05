---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Harry Lee", "Melio AI"]
sched_url: https://kccncna2022.sched.com/event/182GQ/kubernetes-on-the-edge-with-k3s-for-a-smart-metering-use-case-harry-lee-melio-ai
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+On+the+Edge+With+K3s+For+a+Smart+Metering+Use+Case+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes On the Edge With K3s For a Smart Metering Use Case - Harry Lee, Melio AI

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Harry Lee, Melio AI
- Schedule: https://kccncna2022.sched.com/event/182GQ/kubernetes-on-the-edge-with-k3s-for-a-smart-metering-use-case-harry-lee-melio-ai
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+On+the+Edge+With+K3s+For+a+Smart+Metering+Use+Case+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes On the Edge With K3s For a Smart Metering Use Case.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GQ/kubernetes-on-the-edge-with-k3s-for-a-smart-metering-use-case-harry-lee-melio-ai
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+On+the+Edge+With+K3s+For+a+Smart+Metering+Use+Case+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rj4FFf1gZ0g
- YouTube title: Kubernetes On the Edge With K3s For a Smart Metering Use Case - Harry Lee, Melio AI
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-on-the-edge-with-k3s-for-a-smart-metering-use-case/rj4FFf1gZ0g.txt
- Transcript chars: 33999
- Keywords: actually, cluster, devices, platform, server, solution, manager, aggregation, address, customers, installed, gateway, energy, network, install, reason, on-premise, storage

### Resumo baseado na transcript

um yeah morning everyone my name is Harry Lee and today I'll be talking about kubernetes on the edge with k3s for a smart metering use case so just a quick introduction about myself I'm the co-founder and CTO at media AI I've been a devops Enthusiast since I can remember nowadays I help organizations adopt devops practices and Implement Cloud native Technologies by helping them navigate the cloud native landscape I've been working with kubernetes for more than five years now I'm also a certified kubernetes administrator as well fails right because metal lb is actually installed as a demon sets on all of the nodes it see that no one has failed and then it will actually move that IP address to node two so now we're still going to stick with that

### Excerpt da transcript

um yeah morning everyone my name is Harry Lee and today I'll be talking about kubernetes on the edge with k3s for a smart metering use case so just a quick introduction about myself I'm the co-founder and CTO at media AI I've been a devops Enthusiast since I can remember nowadays I help organizations adopt devops practices and Implement Cloud native Technologies by helping them navigate the cloud native landscape I've been working with kubernetes for more than five years now I'm also a certified kubernetes administrator as well as certified kubernetes security specialist I've been on the cncf Ambassador based in South Africa for three years now I've also founded the cloud native Computing Meetup in Johannesburg South Africa since four years ago I currently we're 980 members strong still growing you can find us on the cncf community group I love connecting with Cloud native enthusiasts so yeah if you would like to connect with me yeah follow me on Twitter as well as LinkedIn so quick two words on Miele Ai and what we do we are an mlops consultancy we specialize in ml and devops practices helping data science teams build and deploy machine learning Solutions reliably and efficiently effectively helping them deliver business value as fast as possible and of course we do everything in a cloud native way if you're interested in finding out more about us check us out at milner.ai and we do regular posts on our LinkedIn page so if you want to know more about email Ops please follow us on LinkedIn cool so for this talk I would like to take you on a journey on how we have helped one of our clients build out a smart metering solution so I'll be focusing on three crucial aspects the product that we're trying to build the challenges that we faced while we're building this product and the design that ultimately results in our final delivered solution I'll start off by giving you some context and provide some background into what our client is trying to build and then I'll go into some of the considerations and limitations with what they're trying to build and this that becomes requirements of course and naturally requirements always have a way to become challenges so I'll highlight the four main challenges that we faced while we're building this product provisioning networking High availability certificate management these may seem trivial in the cloud environment but on an on-premise edge setting it's actually proved to be a little bit more involved the design aspect
