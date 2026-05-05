---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Todd Neal", "Amazon", "Sergey Kanzhelev", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2tw/sidecar-containers-are-built-in-to-kubernetes-what-how-and-why-now-todd-neal-amazon-sergey-kanzhelev-google
youtube_search_url: https://www.youtube.com/results?search_query=Sidecar+Containers+Are+Built-in+to+Kubernetes%3A+What%2C+How%2C+and+Why+Now%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Sidecar Containers Are Built-in to Kubernetes: What, How, and Why Now? - Todd Neal, Amazon & Sergey Kanzhelev, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Todd Neal, Amazon, Sergey Kanzhelev, Google
- Schedule: https://kccncna2023.sched.com/event/1R2tw/sidecar-containers-are-built-in-to-kubernetes-what-how-and-why-now-todd-neal-amazon-sergey-kanzhelev-google
- Busca YouTube: https://www.youtube.com/results?search_query=Sidecar+Containers+Are+Built-in+to+Kubernetes%3A+What%2C+How%2C+and+Why+Now%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Sidecar Containers Are Built-in to Kubernetes: What, How, and Why Now?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tw/sidecar-containers-are-built-in-to-kubernetes-what-how-and-why-now-todd-neal-amazon-sergey-kanzhelev-google
- YouTube search: https://www.youtube.com/results?search_query=Sidecar+Containers+Are+Built-in+to+Kubernetes%3A+What%2C+How%2C+and+Why+Now%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_a8fxJDzCJU
- YouTube title: Sidecar Containers Are Built-in to Kubernetes: What, How, and Why Now?- Todd Neal & Sergey Kanzhelev
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/sidecar-containers-are-built-in-to-kubernetes-what-how-and-why-now/_a8fxJDzCJU.txt
- Transcript chars: 29832
- Keywords: containers, container, restart, running, termination, network, terminate, always, sender, little, better, inside, already, wanted, ordering, probably, wouldn, actually

### Resumo baseado na transcript

thank you everybody for coming um glad to see you good turnout um you all probably interested in side cars yeah more people will probably keep coming so I hope it wouldn't uh interrupt you too much um so I'm Serge Kel I'm work for Google and I'm chair of signote hey I'm Todd Neil and I work for AWS and I'm a sign reviewer so side cars you know this construction wouldn't probably steer well when I was a kid uh smallish um I was spending time every summer

### Excerpt da transcript

thank you everybody for coming um glad to see you good turnout um you all probably interested in side cars yeah more people will probably keep coming so I hope it wouldn't uh interrupt you too much um so I'm Serge Kel I'm work for Google and I'm chair of signote hey I'm Todd Neil and I work for AWS and I'm a sign reviewer so side cars you know this construction wouldn't probably steer well when I was a kid uh smallish um I was spending time every summer with my grandparents and my grandfather has a motorcycle with a side car imagine um sitting in a side car there is no belt no nothing nothing wind in your face and so exciting and I was small and imaginative so I was like oh I'm steing a motorcycle oh let's go left let's go right and like uh unfortunately when I need I need to watch my grandfather really carefully where he is going right then I would pretend to turn my wheel and go right as well but I was Imaging that I'm still in the motorcycle so um kubernetes was feeling similarly to me uh side cars were steering the ports it's like yeah it's not right uh we need to fix it so we decided that we need to fix it and now it's fixed we will be so now yeah no imaginative uh steering wheels that actually steers a motorcycle so let's go to the next slide so what is side cars side cars is a special type of container it's a pattern that you will use when you implement your um workload so let's say you have an application you want toize this application uh it may be existing code it may be something that you write specifically for kubernetes but nevertheless it's something that implements a business logic you deployed and you want it to work and uh sometimes you need to to work and you need to communicate with something else like sometimes you need to collect Telemetry out of this container you have different ways to do that uh one of the way is to get a specialized process that will go around and like collect logs when needed and you don't want this process to run inside your container because you may have the different dependency it's much easier to just run a separate container inside your port and you golden uh same concept with networking access you may have different n networking requirements and you want to deploy it as a um some sort of container that it's already existing on a market or you build it yourself other things like security somebody will download certificate and keep it up to date all the time so you don't need to worry about uh about it and um
