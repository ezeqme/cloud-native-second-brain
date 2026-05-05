---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security", "Networking", "Kubernetes Core"]
speakers: ["Hillai Ben-Sasson", "Nir Ohfeld", "Wiz"]
sched_url: https://kccncna2024.sched.com/event/1i7ow/mish-mesh-abusing-the-service-mesh-to-compromise-kubernetes-environments-hillai-ben-sasson-nir-ohfeld-wiz
youtube_search_url: https://www.youtube.com/results?search_query=Mish-Mesh%3A+Abusing+the+Service+Mesh+to+Compromise+Kubernetes+Environments+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Mish-Mesh: Abusing the Service Mesh to Compromise Kubernetes Environments - Hillai Ben-Sasson & Nir Ohfeld, Wiz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Hillai Ben-Sasson, Nir Ohfeld, Wiz
- Schedule: https://kccncna2024.sched.com/event/1i7ow/mish-mesh-abusing-the-service-mesh-to-compromise-kubernetes-environments-hillai-ben-sasson-nir-ohfeld-wiz
- Busca YouTube: https://www.youtube.com/results?search_query=Mish-Mesh%3A+Abusing+the+Service+Mesh+to+Compromise+Kubernetes+Environments+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Mish-Mesh: Abusing the Service Mesh to Compromise Kubernetes Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ow/mish-mesh-abusing-the-service-mesh-to-compromise-kubernetes-environments-hillai-ben-sasson-nir-ohfeld-wiz
- YouTube search: https://www.youtube.com/results?search_query=Mish-Mesh%3A+Abusing+the+Service+Mesh+to+Compromise+Kubernetes+Environments+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iMQR_l0ZvWU
- YouTube title: Mish-Mesh: Abusing the Service Mesh to Compromise Kubernetes Environments - H. Ben-Sasson, N. Ohfeld
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/mish-mesh-abusing-the-service-mesh-to-compromise-kubernetes-environmen/iMQR_l0ZvWU.txt
- Transcript chars: 31183
- Keywords: network, container, access, internal, request, linkerd, environment, server, inside, security, basically, admission, environments, traffic, running, actually, cluster, control

### Resumo baseado na transcript

hello everyone and Welcome to our talk Mish mes I'll be using the service Mash to compromise kubernetes environments my name is neld and here with me on stage is Eli bason we are both security researchers from Israel and we work for wiiz the cloud security company now you might be familiar with some of our previous findings notable Cloud incidents like Kos DB oh my God bing bang and some AI Services which we're going to talk about later on in this talk in this talk we're also

### Excerpt da transcript

hello everyone and Welcome to our talk Mish mes I'll be using the service Mash to compromise kubernetes environments my name is neld and here with me on stage is Eli bason we are both security researchers from Israel and we work for wiiz the cloud security company now you might be familiar with some of our previous findings notable Cloud incidents like Kos DB oh my God bing bang and some AI Services which we're going to talk about later on in this talk in this talk we're also going to talk about a quick introduction to what is service MH and our attackers might abuse service MH solutions to map internal networks and how we did just that in NL we're also going to talk about how attackers might bypass the security rules imposed by service M Solutions and how we did exactly that to accept sap Ai and we'll finish things off with some summary and takeaways it's important to note that we're not going to show you vulnerabilities in service M Solutions rather we're going to show you legitimate features that attackers might abuse to escalate low severity vulnerabilities to high or even critical and with that let's begin a service Mash is essentially a dedicated infrastructure layer that manages the traffic between the different microservices within your cluster some examples include EO linkerd selum and console there are many more service M Solutions on the market but these are just like honorable mentions and these Solutions are the network backbone of many production kubernetes environments and quite frankly a critical component in many of our engagement so we figure that if we see them so often we need to find a way to take them to our own Advantage now getting a bit more technical this is like a general blueprint of how a service mesh might be implemented essentially each part has some kind of a networking middleware and the entire post trffic is redirected to that Network in middleware into the mesh once the traffic is in the mesh the user is benefited from like a few improvements like enhance observability enhan Security in the form of mutual TLS and other features and quite frankly more in in our experience this network in Middle is usually implemented using a networking cite container each part spins up with another cite container that shares the network name space with all of the other containers running on the Pod and using IP tables the entire pod traffic is redirected to that container and from there into the mesh so now that we have like a general unde
