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
themes: ["Platform Engineering", "Networking"]
speakers: ["Raghav Grover", "Timothy Ehlers", "Expedia"]
sched_url: https://kccncna2023.sched.com/event/1R2uV/under-the-hood-exploring-istios-lock-contention-and-its-impact-on-expedias-compute-platform-raghav-grover-timothy-ehlers-expedia
youtube_search_url: https://www.youtube.com/results?search_query=Under+the+Hood%3A+Exploring+Istio%27s+Lock+Contention+and+Its+Impact+on+Expedia%27s+Compute+Platform+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Under the Hood: Exploring Istio's Lock Contention and Its Impact on Expedia's Compute Platform - Raghav Grover & Timothy Ehlers, Expedia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Platform Engineering]], [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Raghav Grover, Timothy Ehlers, Expedia
- Schedule: https://kccncna2023.sched.com/event/1R2uV/under-the-hood-exploring-istios-lock-contention-and-its-impact-on-expedias-compute-platform-raghav-grover-timothy-ehlers-expedia
- Busca YouTube: https://www.youtube.com/results?search_query=Under+the+Hood%3A+Exploring+Istio%27s+Lock+Contention+and+Its+Impact+on+Expedia%27s+Compute+Platform+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Under the Hood: Exploring Istio's Lock Contention and Its Impact on Expedia's Compute Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uV/under-the-hood-exploring-istios-lock-contention-and-its-impact-on-expedias-compute-platform-raghav-grover-timothy-ehlers-expedia
- YouTube search: https://www.youtube.com/results?search_query=Under+the+Hood%3A+Exploring+Istio%27s+Lock+Contention+and+Its+Impact+on+Expedia%27s+Compute+Platform+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HFduMmPcKqI
- YouTube title: Under the Hood: Exploring Istio's Lock Contention and Its Impact o... Raghav Grover & Timothy Ehlers
- Match score: 0.819
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/under-the-hood-exploring-istios-lock-contention-and-its-impact-on-expe/HFduMmPcKqI.txt
- Transcript chars: 18472
- Keywords: actually, controller, number, events, related, server, endpoint, little, cluster, inside, objects, metrics, processing, happening, everything, internals, particular, contention

### Resumo baseado na transcript

so we're from Expedia group um we're going to go over some of the the problems we had um in our ISO adoption uh we're going to start from the page out all the way to the diagnostic steps and uh how we got to a solution so uh let's do some introductions because the way we diagnose this between different Engineers is is how we got to the solution so I'm Tim uh I started to orbit in 2009 so I've been in the travel industry for forever U

### Excerpt da transcript

so we're from Expedia group um we're going to go over some of the the problems we had um in our ISO adoption uh we're going to start from the page out all the way to the diagnostic steps and uh how we got to a solution so uh let's do some introductions because the way we diagnose this between different Engineers is is how we got to the solution so I'm Tim uh I started to orbit in 2009 so I've been in the travel industry for forever U now orbits is uh Expedia um I like to call myself op stev I know the dev Ops buzzword floated around but I've always taken issue with that I do ops things first and then Dev hi everyone myself rag of grower and I work with Tim at xedia as a senior software engineer and um unlike Tim I'm a Dev first guy and I think that's how we complement each other and I've made some contributions to projects like crossplane Carpenter and stto all right just a brief overview again uh we're going to go over what the actual issue was with thiso when we adopted this and and scaled up uh we'll go over possible bottlenecks we'll dive a little bit into how it works if you're not familiar so we'll cover that and then we'll dive into some of the good stuff remote debugging uh the actual solution and uh some stuff we added to help you out if you might go down this road uh so here's the actual issue you know this is this is where the page out starts we've been paged 500 errors uh oh it's probably our fault we're not sure uh and it's lasting a really long time a pod terminates and for nine minutes users are seeing a 500 air so this is a worst case scenario for us um at some point we determin the cause uh pod turn was causing this to happen so every time a pod was deleted uh we would see these these 500 air codes right um and our pod sets are really big so that's important to the story this cluster had grown dramatically because we're moving to it uh we have 1,200 pods set a 600 a 900 a 300 so they're all like really big and they release very frequently uh so ISO architecture this is where we need to step into a little bit of uh how this was all working so here's the Ingress all your traffic is coming in from the internet to the Ingress it then flows to your pods right in our scenario uh pod gets deleted and then the 500 erors begin so if you're familiar with esto uh what should be happening here is ISO should be getting updates from API server those should go down to everything and tell everything where everything is that didn't seem to be happening and
