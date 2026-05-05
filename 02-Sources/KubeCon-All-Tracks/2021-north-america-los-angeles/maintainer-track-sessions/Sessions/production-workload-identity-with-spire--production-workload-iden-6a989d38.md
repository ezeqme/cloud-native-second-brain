---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Ryan Turner", "Uber"]
sched_url: https://kccncna2021.sched.com/event/lV9Y/production-workload-identity-with-spire-ryan-turner-uber
youtube_search_url: https://www.youtube.com/results?search_query=Production+Workload+Identity+with+SPIRE+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Production Workload Identity with SPIRE - Ryan Turner, Uber

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Ryan Turner, Uber
- Schedule: https://kccncna2021.sched.com/event/lV9Y/production-workload-identity-with-spire-ryan-turner-uber
- Busca YouTube: https://www.youtube.com/results?search_query=Production+Workload+Identity+with+SPIRE+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Production Workload Identity with SPIRE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9Y/production-workload-identity-with-spire-ryan-turner-uber
- YouTube search: https://www.youtube.com/results?search_query=Production+Workload+Identity+with+SPIRE+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nlelaa1En0g
- YouTube title: Production Workload Identity with SPIRE - Ryan Turner, Uber
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/production-workload-identity-with-spire/nlelaa1En0g.txt
- Transcript chars: 26602
- Keywords: workload, identity, spiffy, called, workloads, actually, running, account, orders, identities, server, subnet, deployment, authentication, production, security, trying, secure

### Resumo baseado na transcript

hello everyone my name is ryan turner and i'm a software engineer at uber and today i'm going to talk to you about something called production workload identity and explain what that means and how we can use it to improve security posture and how we can achieve that with something called spire so to start i want to talk about a fictional services organization which i've invented for the purposes of this talk it's called starboard games and they want to get into the business of selling board games

### Excerpt da transcript

hello everyone my name is ryan turner and i'm a software engineer at uber and today i'm going to talk to you about something called production workload identity and explain what that means and how we can use it to improve security posture and how we can achieve that with something called spire so to start i want to talk about a fictional services organization which i've invented for the purposes of this talk it's called starboard games and they want to get into the business of selling board games as an online retailer so let's take a look at how they might initially build this system so first they come up with a three-tier architecture to represent different layers of the application so this is composed of three different layers one is the storage layer which is a persistent stateful layer and that contains data that is represented in the system then there is an application layer which interacts with that stateful storage and creates reads updates deletes that data and then there's a web presentation layer which is accessible to users and that's how they interact with the platform and that web layer talks to the app layer to do different operations in the system so this is all in this example running in an aws vpc and as an online retailer this company wants to provide some level of security so that not everything in their production deployment is accessible over the internet so they do this naturally through vpc at goals and they basically set up three different echo policies one says that only things from the internet can access the web subnet only things from the web subnet can talk to the app subnet and only things from the app subnet can talk to the storage subnet so pretty simple and but over time they grow and they decide they want to try to decompose some of the functionality in this app subnet into several different microservices so they move more towards a microservice architecture and suddenly their deployment has gotten much more complicated so you'll see in the middle and bottom layers where there was only one subnet there now that's tripled where the service in the app subnet has now been decomposed into three different services the account service and order service which talks to the account service to get information about an account and then a recommendation service which talks to both the account service and the order service to provide customized recommendations to users and each of these services has its own database so all of a sudden
