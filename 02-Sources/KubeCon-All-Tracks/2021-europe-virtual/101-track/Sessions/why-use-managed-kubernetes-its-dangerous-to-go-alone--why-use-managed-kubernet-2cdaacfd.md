---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Seth McCombs", "Workday"]
sched_url: https://kccnceu2021.sched.com/event/iE5Z/why-use-managed-kubernetes-its-dangerous-to-go-alone-seth-mccombs-workday
youtube_search_url: https://www.youtube.com/results?search_query=Why+Use+Managed+Kubernetes%3F%3A+It%27s+Dangerous+to+Go+Alone%21+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Why Use Managed Kubernetes?: It's Dangerous to Go Alone! - Seth McCombs, Workday

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Seth McCombs, Workday
- Schedule: https://kccnceu2021.sched.com/event/iE5Z/why-use-managed-kubernetes-its-dangerous-to-go-alone-seth-mccombs-workday
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Use+Managed+Kubernetes%3F%3A+It%27s+Dangerous+to+Go+Alone%21+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Why Use Managed Kubernetes?: It's Dangerous to Go Alone!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5Z/why-use-managed-kubernetes-its-dangerous-to-go-alone-seth-mccombs-workday
- YouTube search: https://www.youtube.com/results?search_query=Why+Use+Managed+Kubernetes%3F%3A+It%27s+Dangerous+to+Go+Alone%21+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RyjXYYMacBc
- YouTube title: Why Use Managed Kubernetes?: It's Dangerous to Go Alone! - Seth McCombs, Workday
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/why-use-managed-kubernetes-its-dangerous-to-go-alone/RyjXYYMacBc.txt
- Transcript chars: 27322
- Keywords: managed, clusters, cluster, provider, running, deploy, providers, around, platform, looking, probably, cost, working, options, environments, offering, deploying, yourself

### Resumo baseado na transcript

hi everyone thank you for being here my name is seth mccombs i am a software engineer focusing on cloud orchestration and kubernetes things at workday uh and in the upstream kubernetes project i've also spent some time on the release teams as well as working as parts of sig docs and sig release in the past today i'd like to cover a topic uh some people may have avoided or have some some preconceptions about i'm going to be talking today about managed kubernetes services uh and and by say hey here's why we need this so with most things around cost and money it's multi-faceted you know what's the cost of running your own versus uh managed service what is the time your engineers spend on these upgrading recovering uh you know what

### Excerpt da transcript

hi everyone thank you for being here my name is seth mccombs i am a software engineer focusing on cloud orchestration and kubernetes things at workday uh and in the upstream kubernetes project i've also spent some time on the release teams as well as working as parts of sig docs and sig release in the past today i'd like to cover a topic uh some people may have avoided or have some some preconceptions about i'm going to be talking today about managed kubernetes services uh and and by managed i mean using a cloud providers kind of kubernetes as a service offering um now i won't be diving into specifics around any one cloud provider's offering we're not going to get that technical i'm just covering the overall idea of using a kubernetes managed kubernetes service why you may want to consider doing so um and in in the case of some cloud providers they may only have you know one sort of kubernetes offering some may have different levels of kind of abstraction around their their kubernetes offering so you know depending on where you may find your infrastructure running you may have some choices there so the original title for this talk was a little more aggressive than the one i ended up going with it was something along the lines of using a managed kubernetes service doesn't make you a bad engineer and while i still believe that statement wholeheartedly i thought it was best to lighten up a little bit uh before my current role in in past various infor related roles i found that even though i wanted kubernetes to be the only thing i was working on you know to be the focus of my day today uh that wasn't you know that wasn't the case uh kubernetes was the platform i was deploying on and what really mattered were the services i provided to my end users whether they were the developers the actual you know consumers of the product or service the company made the executives that used some sort of service um you know the kubernetes clusters i ran were just a means to an end and it was in one of these roles that i came to terms with using a managed kubernetes service um and it was a service provided by a cloud provider and i found that by offloading uh much of the day-to-day overhead operational stuff i needed to do to keep clusters running uh it freed me up to work on some other cool stuff toil less and it was it was definitely something that worked for me so that's it right i found using a managed kubernetes service worked for me the story has a happy ending and we'r
