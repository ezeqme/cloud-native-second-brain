---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability"]
speakers: ["Simon Pasquier", "Vanessa Martini", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HyaD/it-is-more-than-just-correlation-a-debug-journey-simon-pasquier-vanessa-martini-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=It+Is+More+Than+Just+Correlation+-+A+Debug+Journey+CNCF+KubeCon+2023
slides: []
status: parsed
---

# It Is More Than Just Correlation - A Debug Journey - Simon Pasquier & Vanessa Martini, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Simon Pasquier, Vanessa Martini, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HyaD/it-is-more-than-just-correlation-a-debug-journey-simon-pasquier-vanessa-martini-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=It+Is+More+Than+Just+Correlation+-+A+Debug+Journey+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre It Is More Than Just Correlation - A Debug Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyaD/it-is-more-than-just-correlation-a-debug-journey-simon-pasquier-vanessa-martini-red-hat
- YouTube search: https://www.youtube.com/results?search_query=It+Is+More+Than+Just+Correlation+-+A+Debug+Journey+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hovktXU5ojE
- YouTube title: It Is More Than Just Correlation - A Debug Journey - Simon Pasquier & Vanessa Martini, Red Hat
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/it-is-more-than-just-correlation-a-debug-journey/hovktXU5ojE.txt
- Transcript chars: 21608
- Keywords: signals, logs, starting, correlator, events, deployment, observability, openshift, troubleshooting, metrics, information, engineers, clusters, alerts, objects, domain, correlation, journey

### Resumo baseado na transcript

hello everyone welcome to the session it is more than just correlation at the back Journey so while several kubernetes users are already have access to metrics logs to some extent traces there is still no established open source tool out there that Aggregates all these different information and helps users understanding how their systems behave and most importantly why those systems break so contributing to soviety's issue is actually the driving motive of today's session at kubecon so thank you for joining but before deep diving into the topic

### Excerpt da transcript

hello everyone welcome to the session it is more than just correlation at the back Journey so while several kubernetes users are already have access to metrics logs to some extent traces there is still no established open source tool out there that Aggregates all these different information and helps users understanding how their systems behave and most importantly why those systems break so contributing to soviety's issue is actually the driving motive of today's session at kubecon so thank you for joining but before deep diving into the topic a few words about us my name is Vanessa I am an observability product manager at redette working in openshift and this is my colleague hello I'm Simon so I'm working on openshift monitoring as an engineer great so let's take a look at the agenda for today first we will talk about the problems that Engineers mainly site reliability Engineers have to face when troubleshooting issues in kubernetes mainly when troubleshooting clusters after that we will take a look at our solution at least the proposed solution to this problem correlator which is an open source project founded within Reddit with the goal of making correlation across observability signals accessible to everyone after that we will have a demo led by Simon and then we will recap on the functionalities of correlators so stay tuned for that and lastly we will wrap up the presentation with a sneak peek overview of our roadmap Vision next steps we have around it so let's get started with Section number one what is the problem that we're actually trying to solve here everything started a few months ago we were wondering how we could facilitate the troubleshooting process of site reliability Engineers when dealing with openshift clusters so what we knew back then was that they need to access relevant information to keep the system up and running secured and stable and avoiding any disruptions to the end customers and in this troubleshooting journey is where observability signals come into play observability signals represent the relevant information set reliability Engineers need to troubleshoot for the ones of you were not familiar with the term observability what do we Define with it so observability is about correlating various sources so that you can answer any questions you might have about your running system assisting you when you're resolving issues within your system and also when not optimizing it so with this information in mind let's take a look at w
