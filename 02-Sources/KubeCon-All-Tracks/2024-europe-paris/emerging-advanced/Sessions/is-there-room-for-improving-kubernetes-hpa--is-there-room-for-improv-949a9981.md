---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Berta Serracanta Pujol", "UPC Barcelona Tech", "Gabor Retvari", "L7mp Technologies", "Alberto Rodriguez-Natal", "Cisco"]
sched_url: https://kccnceu2024.sched.com/event/1YeOo/is-there-room-for-improving-kubernetes-hpa-berta-serracanta-pujol-upc-barcelona-tech-gabor-retvari-l7mp-technologies-alberto-rodriguez-natal-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Is+There+Room+for+Improving+Kubernetes%E2%80%99+HPA%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Is There Room for Improving Kubernetes’ HPA? - Berta Serracanta Pujol, UPC Barcelona Tech; Gabor Retvari, L7mp Technologies; Alberto Rodriguez-Natal, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Berta Serracanta Pujol, UPC Barcelona Tech, Gabor Retvari, L7mp Technologies, Alberto Rodriguez-Natal, Cisco
- Schedule: https://kccnceu2024.sched.com/event/1YeOo/is-there-room-for-improving-kubernetes-hpa-berta-serracanta-pujol-upc-barcelona-tech-gabor-retvari-l7mp-technologies-alberto-rodriguez-natal-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Is+There+Room+for+Improving+Kubernetes%E2%80%99+HPA%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Is There Room for Improving Kubernetes’ HPA?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOo/is-there-room-for-improving-kubernetes-hpa-berta-serracanta-pujol-upc-barcelona-tech-gabor-retvari-l7mp-technologies-alberto-rodriguez-natal-cisco
- YouTube search: https://www.youtube.com/results?search_query=Is+There+Room+for+Improving+Kubernetes%E2%80%99+HPA%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZG8WIiCl5m4
- YouTube title: Is There Room for Improving Kubernetes’ HPA?
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/is-there-room-for-improving-kubernetes-hpa/ZG8WIiCl5m4.txt
- Transcript chars: 25713
- Keywords: microservice, scaling, actually, request, control, requests, microservices, resources, traffic, replicas, application, situation, number, micros, presentation, course, second, basically

### Resumo baseado na transcript

uh welcome welcome to this session we are very happy to have you here um we are not sure why you have picked this out of the many good presentations that are going on but anyways we are we are happy to to see you so we have titled this presentation um is there room for improving kubernetes spa and you may notice there's a question mark at the end and the reason for that question mark is because we we don't know so basically um we we are not

### Excerpt da transcript

uh welcome welcome to this session we are very happy to have you here um we are not sure why you have picked this out of the many good presentations that are going on but anyways we are we are happy to to see you so we have titled this presentation um is there room for improving kubernetes spa and you may notice there's a question mark at the end and the reason for that question mark is because we we don't know so basically um we we are not experts on on HPA okay we we are people the three of us uh we have an academic background uh so basically we have been you know thinking about this PA thinkering with it uh doing some experiments and the the goal here is hopefully to to spark some some discussion and and have some conversation with you with you after the the session so a bit more a bit more about the the three of us um today the stage you have uh Berta she's a PhD student at at Barcelona Tech you have H Gabor there he's the the CTO for uh L7 mp. and he's also a professor at BM University and I'm Alberto I'm a tech L Cisco and I work at the Enterprise C team there so before we go into the you know the core of the presentation we thought it could be interesting to to describe you know where we are coming from which work we have done in the past what has motivated us to do this presentation so that we are all in the same page of you know why we are all here together today so let's start slow outo scaling AOS scaling the the idea is is simple enough to have some some load that goes up some some replicas that that goes up as well and and the three of us and together with some people from you know our our institutions we were thinking on on out scaling and and we have been thinking out scaling for for some time and one of the things that we were thinking about is okay what really means that you out to scale things so one implication of that is that you are consuming some resources on your system and typically people tend to think of the resources in terms of CPU and memory but one thing that we realize on Sago is that another resource that is typically consum and sometimes goes un notice is is the network so we ask ourselves the question is there any between autoscaling and the network of course there's some some relationship right so the the idea again is is still simple you have more replicas you have more traffic you have more traffic you have more replicas so as the you know request went into your system you have to scale up the the micros Service uh scal
