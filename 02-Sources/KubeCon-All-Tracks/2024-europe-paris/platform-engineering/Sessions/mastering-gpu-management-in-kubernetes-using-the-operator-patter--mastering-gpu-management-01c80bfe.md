---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Shiva Krishna Merla", "Kevin Klues", "NVIDIA"]
sched_url: https://kccnceu2024.sched.com/event/1YeQY/mastering-gpu-management-in-kubernetes-using-the-operator-pattern-shiva-krishna-merla-kevin-klues-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Mastering+GPU+Management+in+Kubernetes+Using+the+Operator+Pattern+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Mastering GPU Management in Kubernetes Using the Operator Pattern - Shiva Krishna Merla & Kevin Klues, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Shiva Krishna Merla, Kevin Klues, NVIDIA
- Schedule: https://kccnceu2024.sched.com/event/1YeQY/mastering-gpu-management-in-kubernetes-using-the-operator-pattern-shiva-krishna-merla-kevin-klues-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Mastering+GPU+Management+in+Kubernetes+Using+the+Operator+Pattern+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Mastering GPU Management in Kubernetes Using the Operator Pattern.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQY/mastering-gpu-management-in-kubernetes-using-the-operator-pattern-shiva-krishna-merla-kevin-klues-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Mastering+GPU+Management+in+Kubernetes+Using+the+Operator+Pattern+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jbpIFCkEEng
- YouTube title: Mastering GPU Management in Kubernetes Using the Operator Pattern- Shiva Krishna Merla & Kevin Klues
- Match score: 0.882
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/mastering-gpu-management-in-kubernetes-using-the-operator-pattern/jbpIFCkEEng.txt
- Transcript chars: 44579
- Keywords: gpu, driver, operator, container, support, install, drivers, runtime, itself, configuration, nvidia, device, common, deploy, containers, software, manage, looking

### Resumo baseado na transcript

I'm Shiva merla U I'm from the cloud native engineering team at Nvidia um I've been focusing um on GPU operator for last few years um and mainly work working on orchestration GPU orchestration in kubernetes um so we had a long journey um uh in terms of using operator pattern uh to make it easy to consume gpus in kubernetes um so today we're going to talk about um how we um how we went through this approach and the learnings we had uh through this journey introduce my

### Excerpt da transcript

I'm Shiva merla U I'm from the cloud native engineering team at Nvidia um I've been focusing um on GPU operator for last few years um and mainly work working on orchestration GPU orchestration in kubernetes um so we had a long journey um uh in terms of using operator pattern uh to make it easy to consume gpus in kubernetes um so today we're going to talk about um how we um how we went through this approach and the learnings we had uh through this journey introduce my name is Kevin Clues um I'm on the same team as Shiva at Nvidia um and the the way I always pitch the team that that that we have what we do is we we do everything that's necessary to enable GPU support in kubernetes in in containers in kubernetes um and then we build all the tooling around that to make to make using gpus in this environment easier um and so yeah we're the the operator is our way to pack it all these things together and make it that much easier for you guys to take advantage of of all the of all of these things on kubernetes thanks Kevin um so this is the outline for the talk today um we're going to talk about why gpus um so why GPS have become so ubiquitous and and why um gpus in kubernetes um and also we'll walk through um how the typical GPU software stack looks like um uh what are the main um operational pain points we have when enabling gpus um GPU software snack and then we'll um uh delve into uh operator pattern uh how we have implemented GPU operator and some of the technical details uh of the GPU operator itself then we'll end with a demo and and some of the the lessons that we learn um through this journey um so why gpus um are so popular right um it's no surprise um given the given the massive um computational Power and and given the the way we are um we took a giant leap in terms of computational capacity over the last decade um so they become um so ubiquitous in in kubernetes um to run IML jobs deep learning um even in the scientific research um so become so um common everywhere um and recently we have announced Blackwell um which took a giant leap in terms of computation capability and and kubernetes on the other hand um also over the last few years have become a defacto standard uh to run IML jobs um be it in um IML uh deep learning um in the scientific fields or data processing so everywhere kubernetes have become a defacto standard because of its scalability um easy to scale your applications um because of its resiliency um right and also um uh uh the way to ki
