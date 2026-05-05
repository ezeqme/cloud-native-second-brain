---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Stefan Schimanski", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182Hm/towards-something-better-than-crds-in-a-post-operator-world-stefan-schimanski-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Towards+Something+Better+Than+CRDs+In+a+Post-Operator+World+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Towards Something Better Than CRDs In a Post-Operator World - Stefan Schimanski, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Stefan Schimanski, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182Hm/towards-something-better-than-crds-in-a-post-operator-world-stefan-schimanski-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Towards+Something+Better+Than+CRDs+In+a+Post-Operator+World+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Towards Something Better Than CRDs In a Post-Operator World.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Hm/towards-something-better-than-crds-in-a-post-operator-world-stefan-schimanski-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Towards+Something+Better+Than+CRDs+In+a+Post-Operator+World+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Uv0ivz5xej4
- YouTube title: Towards Something Better Than CRDs In a Post-Operator World - Stefan Schimanski, Red Hat
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/towards-something-better-than-crds-in-a-post-operator-world/Uv0ivz5xej4.txt
- Transcript chars: 29281
- Keywords: mongodb, cluster, provider, basically, running, everything, create, secret, access, binding, operators, objects, status, permission, resources, operator, software, course

### Resumo baseado na transcript

all right so welcome to the last talk I think before lunch about cids everything is I guess was about crds those who have seen Joe before it was about cids this as well I'm Stefan schumanski I'm one of the initial authors heavily involved in cids so lots of the things you see today defaulting structural schemas blame me for that I was all in there um today we want to talk about something which is CID based but could be a next step for the ecosystem to use

### Excerpt da transcript

all right so welcome to the last talk I think before lunch about cids everything is I guess was about crds those who have seen Joe before it was about cids this as well I'm Stefan schumanski I'm one of the initial authors heavily involved in cids so lots of the things you see today defaulting structural schemas blame me for that I was all in there um today we want to talk about something which is CID based but could be a next step for the ecosystem to use them so this is how it started a few weeks ago I realized that so it's so hard still to get something like a my secret claim API into my cluster there are so many providers providing MySQL but if I want to have one I have to go to some websites or some cloud provider UI to create databases it's still not native right I cannot say cue cattle create MySQL without installing anything into my cluster so what I want to have and that's a submission that's basically the the doing where we want to go to as an ecosystem I don't want operators to do that like I want to consume a MySQL from anybody who offers it in some service I want to have it native CID based in my kubernetes but I don't want to run anything I don't want to run an operator just to get a software as a service MySQL and for eight years we have built systems like operators or for eight years but in kubernetes basically we don't support software as a service this is basically is a rent here this started as a Twitter tweet um very I talk at the time and many people answered I guess some of them are here there is no such support in kubernetes while the whole ecosystem around us builds software as a service so can we change that and six years we have spent in building operators and I'm focusing here on operators which don't operate like operators which don't run local pots this last class is totally um it's a good use case like if you run pods and you want to run your on-premise in your cluster database that's fine but if it's a software as a service I don't want operators I think we as an ecosystem do something which is not really helpful basically creates so much complexity when I have to maintain operators for software as a service basically we we have building or we are building that right everybody knows those pictures many adapters between different worlds different standards different [Music] um API variants and but we are in Cube here so we're in kubecon and we love Cube apis so we need something else and that was basically the result of this Tw
