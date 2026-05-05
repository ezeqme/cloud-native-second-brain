---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Hochuen Wong", "DoorDash"]
sched_url: https://kccncna2023.sched.com/event/1R2u7/service-mesh-journey-at-doordash-the-good-the-bad-and-the-ugly-hochuen-wong-doordash
youtube_search_url: https://www.youtube.com/results?search_query=Service+Mesh+Journey+at+DoorDash%3A+The+Good%2C+the+Bad%2C+and+the+Ugly+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Service Mesh Journey at DoorDash: The Good, the Bad, and the Ugly - Hochuen Wong, DoorDash

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Hochuen Wong, DoorDash
- Schedule: https://kccncna2023.sched.com/event/1R2u7/service-mesh-journey-at-doordash-the-good-the-bad-and-the-ugly-hochuen-wong-doordash
- Busca YouTube: https://www.youtube.com/results?search_query=Service+Mesh+Journey+at+DoorDash%3A+The+Good%2C+the+Bad%2C+and+the+Ugly+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Service Mesh Journey at DoorDash: The Good, the Bad, and the Ugly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2u7/service-mesh-journey-at-doordash-the-good-the-bad-and-the-ugly-hochuen-wong-doordash
- YouTube search: https://www.youtube.com/results?search_query=Service+Mesh+Journey+at+DoorDash%3A+The+Good%2C+the+Bad%2C+and+the+Ugly+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I6E_7f40YP0
- YouTube title: Service Mesh Journey at DoorDash: The Good, the Bad, and the Ugly - Hochuen Wong, DoorDash
- Match score: 0.929
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/service-mesh-journey-at-doordash-the-good-the-bad-and-the-ugly/I6E_7f40YP0.txt
- Transcript chars: 30703
- Keywords: traffic, features, actually, payment, configurations, started, solution, probably, around, basically, eventually, onboarding, outage, matrix, solutions, support, control, architecture

### Resumo baseado na transcript

I guess let's get started so uh hello everyone welcome thanks for uh coming so today I'm going to talk about the service match Journey at door Dash over the last two years uh we will discuss what's been uh good what's been bad and yes even some a little bit some ugly stuff uh my name is H I have been a software engineer at D cor infrastructure team since 2020 U mainly focusing on uh computer and traffic infrastructure and before that I was working on buildings and

### Excerpt da transcript

I guess let's get started so uh hello everyone welcome thanks for uh coming so today I'm going to talk about the service match Journey at door Dash over the last two years uh we will discuss what's been uh good what's been bad and yes even some a little bit some ugly stuff uh my name is H I have been a software engineer at D cor infrastructure team since 2020 U mainly focusing on uh computer and traffic infrastructure and before that I was working on buildings and distribu system for machine learning uh at several startups until I realized uh that's just probably too hard for me U all right so let's get started whyer smash for door Dash so in 2019 uh door Dash started their effort to extract microservices from a single monistic application and fast forward to the end of q1 2021 we found ourselves with over 50 microservices and you know with this growth came with those you know classic microservice challenges uh observability has been challenging debuging was much harder our service topology became a mze of complexity and no one really knows who is talking to whom and who ons what or microservices could talk to each other in so many different ways they could use service IP they could use uh Headly service with client side Lo balancing or they could just use load balancing Lo Baner and there was no standard way to do authentication and authorization and bes that developers were just implementing so many Sim similar things in the application code using so many different ways so uh in Q2 2021 we started exploring service match which we believed has the potential to address the above challenges we believe that you know by implementing so many features as the platform layer in a more standard way is far more efficient than addressing them individually at the application layer so we started searching for Solutions and we did explore various open source projects and probably you know before we look at the initial deis uh let's take a quick overview of our requirements at the time so uh first thing first scalability uh our microservices actually were around the time were all deployed on one single big cuties clusters with more than 2,000 notes and typically uh we felt uncomfortable whenever a cluster has more than 1,000 notes because a lot of Open Source tools we used were basically tested with at most with a thousand notes and in reality we did U you know observe some random scalability and reliability issues whenever we had a Custer more than a, no and obviously
