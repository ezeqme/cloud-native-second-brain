---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Matteo Bunino", "CERN", "Diego Ciangottini", "INFN"]
sched_url: https://kccnceu2025.sched.com/event/1tx7o/testing-ai-containers-for-digital-twins-in-science-a-cloud-hpc-workflow-matteo-bunino-cern-diego-ciangottini-infn
youtube_search_url: https://www.youtube.com/results?search_query=Testing+AI+Containers+for+Digital+Twins+in+Science%3A+A+Cloud-HPC+Workflow+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Testing AI Containers for Digital Twins in Science: A Cloud-HPC Workflow - Matteo Bunino, CERN & Diego Ciangottini, INFN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Matteo Bunino, CERN, Diego Ciangottini, INFN
- Schedule: https://kccnceu2025.sched.com/event/1tx7o/testing-ai-containers-for-digital-twins-in-science-a-cloud-hpc-workflow-matteo-bunino-cern-diego-ciangottini-infn
- Busca YouTube: https://www.youtube.com/results?search_query=Testing+AI+Containers+for+Digital+Twins+in+Science%3A+A+Cloud-HPC+Workflow+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Testing AI Containers for Digital Twins in Science: A Cloud-HPC Workflow.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7o/testing-ai-containers-for-digital-twins-in-science-a-cloud-hpc-workflow-matteo-bunino-cern-diego-ciangottini-infn
- YouTube search: https://www.youtube.com/results?search_query=Testing+AI+Containers+for+Digital+Twins+in+Science%3A+A+Cloud-HPC+Workflow+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bIxw1uK0QRQ
- YouTube title: Testing AI Containers for Digital Twins in Science: A Cloud-HPC... Matteo Bunino & Diego Ciangottini
- Match score: 0.868
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/testing-ai-containers-for-digital-twins-in-science-a-cloud-hpc-workflo/bIxw1uK0QRQ.txt
- Transcript chars: 23915
- Keywords: actually, distributed, pipeline, machine, digital, dagger, course, github, instance, learning, container, training, create, frameworks, pretty, singularity, containers, docker

### Resumo baseado na transcript

Uh how we managed to develop and to create a platform to develop digital twins in a hybrid cloud plus HPC scenario. I'm Diego Changotini from INF that is the National Institute for Nuclear Physics in Italy. So the challenge in a nutshell, we have a distributed hogenous resources good and then we need to put on top a common interface. So we left out just with a uh a question how we can merge a Kubernetes API access to different kind of resources and we listen before for quantum computing is kind of the same challenge. So there is a demo for the solution that I'm going to briefly introd introduce here. And the idea is to create a plugable system where we put adapters on top of the remote resources that we want to control through the Kubernetes cluster and we try very hard to keep the requirements for the providers the uh less inbases possible.

### Excerpt da transcript

Good morning everyone. Uh today we are going to talk about something very peculiar. Uh how we managed to develop and to create a platform to develop digital twins in a hybrid cloud plus HPC scenario. Right. So first of all presentations. I'm Diego Changotini from INF that is the National Institute for Nuclear Physics in Italy. And here with me on the stage there is Matabunino that is from the CERN open lab. So you might have heard CERN inafan it's on the same kind of of track. We are doing physics with particles and so why we are here talking about um digital twins. Well there are several reasons uh and several institute and projects that are working into whatever we are presenting today. I give you here just the links so you can check later if you're interested. What are digital twins then? I love this uh sentence that summarize very well uh what should be uh a digital twin. So it's a digital representation of a real world system and yeah it it's not working like that but kind of you know so you have projecting wildfire and you want to uh forecast whatever will happen in in case of this disaster or in this kind of other disaster you want to understand the impact of floating on your um landscape.

And then there are other digital twins that can be very useful. And for instance, one that was just uh mentioned before uh in the nice panel that was mentioned before uh is particle detection. So we have this big camera that are uh trained and projected to create photos detailed pictures of what happens between particles. Why not creating a digital team of these big cameras and facilitate our life? And same for noise. We have to do precise measurement. We can simulate noise or teach a machine to simulate the real world noise we have in our environments. From all these use cases that share very similar uh needs, we started investigating possibility to create an engine for digital twins. to something that will serve multiple communities and make them adopt and use resources that are shared across different providers. So you see intertwin is the project European project uh where we are working this out and on one end we have the providers so that can span from cloud providers to supercomputers euro HPC supercomputers and on the other side you have frameworks that users use to uh do their digital twins.

What are the challenges there? So you have to provide a platform that is capable to support all different use cases, all different frameworks, but also you have to m
