---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Mofi Rahman", "Kaslin Fields", "Google", "Rob Koch", "Slalom"]
sched_url: https://kccnceu2024.sched.com/event/1YeNn/navigating-the-processing-unit-landscape-in-kubernetes-for-ai-use-cases-mofi-rahman-kaslin-fields-google-rob-koch-slalom
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+the+Processing+Unit+Landscape+in+Kubernetes+for+AI+Use+Cases+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Navigating the Processing Unit Landscape in Kubernetes for AI Use Cases - Mofi Rahman & Kaslin Fields, Google & Rob Koch, Slalom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Mofi Rahman, Kaslin Fields, Google, Rob Koch, Slalom
- Schedule: https://kccnceu2024.sched.com/event/1YeNn/navigating-the-processing-unit-landscape-in-kubernetes-for-ai-use-cases-mofi-rahman-kaslin-fields-google-rob-koch-slalom
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+the+Processing+Unit+Landscape+in+Kubernetes+for+AI+Use+Cases+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Navigating the Processing Unit Landscape in Kubernetes for AI Use Cases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNn/navigating-the-processing-unit-landscape-in-kubernetes-for-ai-use-cases-mofi-rahman-kaslin-fields-google-rob-koch-slalom
- YouTube search: https://www.youtube.com/results?search_query=Navigating+the+Processing+Unit+Landscape+in+Kubernetes+for+AI+Use+Cases+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=195X1yItSLc
- YouTube title: Navigating the Processing Unit Landscape in Kubernetes for AI Use Cases
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/navigating-the-processing-unit-landscape-in-kubernetes-for-ai-use-case/195X1yItSLc.txt
- Transcript chars: 33769
- Keywords: memory, workload, gpu, running, processing, process, hardware, faster, particular, talking, containers, probably, basically, cluster, called, machine, parallel, scheduler

### Resumo baseado na transcript

all right welcome everyone to what is the name of our talk really navigating the processing unit landscape in kubernetes for AI use cases um so today we're going to be talking about processing units we'll go over the basics of what they are and then we're going to talk about how they're used in kubernetes especially in Ai and ml workloads I'm casyn Fields I'm a developer Advocate at Google Cloud where I focus on gke and open source kubernetes I'm also a co-chair of the speci interest group

### Excerpt da transcript

all right welcome everyone to what is the name of our talk really navigating the processing unit landscape in kubernetes for AI use cases um so today we're going to be talking about processing units we'll go over the basics of what they are and then we're going to talk about how they're used in kubernetes especially in Ai and ml workloads I'm casyn Fields I'm a developer Advocate at Google Cloud where I focus on gke and open source kubernetes I'm also a co-chair of the speci interest group for contributor experience in open source kubernetes so if you have any questions about contributing feel free to let me know um I'm also a cncf Ambassador and a co-host of the kuber podcast from Google and my name is Mofi I am also developed Advocate at Google focusing on gke and these days my focus mostly is around running AI workload on kubernetes and hello everyone I'm Rob cot I'm a principal at slom Bill I'm also an data hero so sorry in between amongst two gers here but uh I also work um in the uh cncf uh DEA and heart of hearing working group I am the co-chair here and I'd like to welcome uh the rest of the group here that's uh supporting me today all right folks we're going to start off with some heavy stuff going to tell you the truth about containers did you know that you write containers in like a 100 lines of bash containers really are primarily made up of a couple of core Linux kernel components called cgroups and namespaces cgroups allow you to do resource sharing so you've got so much CPU you've got so much memory on your machine using a cgroup you can say this process gets this much of the processor and gets this much of the memory the other core component is nam spaces and name spaces are a logical environmental isolation mechanism so they're a way of separating processes from one another and aside from that a container is basically just a process and that's going to come into play a lot as we go through our content today so let's start talking about processing units there are a whole bunch of different types of processing units actually not sure if you're aware but there are a whole bunch of them they all in in pu because they're processing units but today we're going to be talking about them in the context of kubernetes so for a processing unit to be uh compatible or supported by kubernetes it basically needs to be supported by uh the Linux kernel it needs to have a device driver that's compatible with kubernetes and the hardware that kubernetes works
