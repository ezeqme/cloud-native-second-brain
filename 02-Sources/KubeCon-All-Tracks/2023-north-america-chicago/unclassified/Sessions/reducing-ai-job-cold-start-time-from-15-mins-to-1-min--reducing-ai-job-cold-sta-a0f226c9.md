---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML"]
speakers: ["Tao He", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2nV/reducing-ai-job-cold-start-time-from-15-mins-to-1-min-tao-he-google
youtube_search_url: https://www.youtube.com/results?search_query=Reducing+AI+Job+Cold+Start+Time+from+15+Mins+to+1+Min+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Reducing AI Job Cold Start Time from 15 Mins to 1 Min - Tao He, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]]
- País/cidade: United States / Chicago
- Speakers: Tao He, Google
- Schedule: https://kccncna2023.sched.com/event/1R2nV/reducing-ai-job-cold-start-time-from-15-mins-to-1-min-tao-he-google
- Busca YouTube: https://www.youtube.com/results?search_query=Reducing+AI+Job+Cold+Start+Time+from+15+Mins+to+1+Min+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Reducing AI Job Cold Start Time from 15 Mins to 1 Min.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nV/reducing-ai-job-cold-start-time-from-15-mins-to-1-min-tao-he-google
- YouTube search: https://www.youtube.com/results?search_query=Reducing+AI+Job+Cold+Start+Time+from+15+Mins+to+1+Min+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=e6Oo2aoZPnA
- YouTube title: Reducing AI Job Cold Start Time from 15 Mins to 1 Min - Tao He, Google
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/reducing-ai-job-cold-start-time-from-15-mins-to-1-min/e6Oo2aoZPnA.txt
- Transcript chars: 24313
- Keywords: container, question, layers, containers, solution, approach, cost, storage, inside, create, unpacking, change, latency, reduce, benefit, machine, process, actually

### Resumo baseado na transcript

all right let's get started and um my name is toi I'm a software in software engineer in Google I need teams to improve the start of latency for machine learning workloads I also need team to provide the GPU round time in gke and today we're going to talk about the reducing AI job code start time from 15 minutes to 1 minute and first we'll talk about the code start problem the definition is here a code start is when you SC schedule a port and to a

### Excerpt da transcript

all right let's get started and um my name is toi I'm a software in software engineer in Google I need teams to improve the start of latency for machine learning workloads I also need team to provide the GPU round time in gke and today we're going to talk about the reducing AI job code start time from 15 minutes to 1 minute and first we'll talk about the code start problem the definition is here a code start is when you SC schedule a port and to a node and when the node doesn't have that container image during this process the container will the container on time will prove and will pull the image from a remote container registry and download and pack that uh container image to the local disk which will consume some CPU and networking and storage which also take time to finish and this graph is a high level like when you schedu port and each step it requires some resource for example in the infra side you may need a no pool in jke you may need a instance group in ads and when you don't have enough node for the same machine type it will check like Auto scaling and to get enough like CP U GPU or memory and when it comes to the container run time the workload part and if the content image does not exist there it will trigger the image pool and it will pull the image to the local and pack it and then the container can start from that container image and in the end you need the AI model to present and to start the machine learning workout in this talk we will focus on the container image pool because that is a most time consuming part and when you have like 30 gigabyte container image the image pool can take up to 15 minutes and it's a super long time to start a application and the problem get uh get even worse when you running a training job because if you hit some error you need to do error recovery from the N check point at that point you also need to schedule a group of ports onto a new nodes and then it will delay further due to the code start latency first we'll uh go to a deep dive into why the image pool is so snow for AI workloads because AI container image are very large they uh username for lar uh larger than 4 gab and why are those AI container image so large because those base layers are very large and why are those base layers are so large because AI Mach in GPU libraries inside those layers they are very large and then comes the next question why not placing the libraries onto the host and put it as part of the disk image it is because the applic
