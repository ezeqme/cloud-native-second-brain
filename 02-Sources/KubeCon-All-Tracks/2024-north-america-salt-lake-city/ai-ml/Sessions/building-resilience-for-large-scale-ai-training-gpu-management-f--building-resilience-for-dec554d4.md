---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Ganeshkumar Ashokavardhanan", "Microsoft", "Ace Eldeib", "Cohere"]
sched_url: https://kccncna2024.sched.com/event/1i7mf/building-resilience-for-large-scale-ai-training-gpu-management-failure-detection-and-beyond-ganeshkumar-ashokavardhanan-microsoft-ace-eldeib-cohere
youtube_search_url: https://www.youtube.com/results?search_query=Building+Resilience+for+Large-Scale+AI+Training%3A+GPU+Management%2C+Failure+Detection%2C+and+Beyond+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building Resilience for Large-Scale AI Training: GPU Management, Failure Detection, and Beyond - Ganeshkumar Ashokavardhanan, Microsoft & Ace Eldeib, Cohere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Ganeshkumar Ashokavardhanan, Microsoft, Ace Eldeib, Cohere
- Schedule: https://kccncna2024.sched.com/event/1i7mf/building-resilience-for-large-scale-ai-training-gpu-management-failure-detection-and-beyond-ganeshkumar-ashokavardhanan-microsoft-ace-eldeib-cohere
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Resilience+for+Large-Scale+AI+Training%3A+GPU+Management%2C+Failure+Detection%2C+and+Beyond+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building Resilience for Large-Scale AI Training: GPU Management, Failure Detection, and Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mf/building-resilience-for-large-scale-ai-training-gpu-management-failure-detection-and-beyond-ganeshkumar-ashokavardhanan-microsoft-ace-eldeib-cohere
- YouTube search: https://www.youtube.com/results?search_query=Building+Resilience+for+Large-Scale+AI+Training%3A+GPU+Management%2C+Failure+Detection%2C+and+Beyond+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iam7A5peA5U
- YouTube title: Building Resilience for Large-Scale AI Training: GPU Management, Fa... G. Ashokavardhanan, A. Eldeib
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-resilience-for-large-scale-ai-training-gpu-management-failure/iam7A5peA5U.txt
- Transcript chars: 33569
- Keywords: gpu, checks, training, issues, workload, running, checkpoint, components, failures, health, errors, little, nvidia, hardware, across, actually, workloads, detector

### Resumo baseado na transcript

welcome everyone it's great seeing so many of you this evening uh training today's large language models and other deep learning workloads often involves several thousand gpus and can take multiple million GPU hours of time the coordinated nature of training also makes resilience in the system not just a nice to have but an essential quality today we'll share how to detect manage and mitigate GPU network issues for building resilience and while these techniques are critical at large scales they also bring many valuable aspects to running a

### Excerpt da transcript

welcome everyone it's great seeing so many of you this evening uh training today's large language models and other deep learning workloads often involves several thousand gpus and can take multiple million GPU hours of time the coordinated nature of training also makes resilience in the system not just a nice to have but an essential quality today we'll share how to detect manage and mitigate GPU network issues for building resilience and while these techniques are critical at large scales they also bring many valuable aspects to running a wide range of smaller workloads I'm Ganesh and I'm a software engineer in the azja kubernetes service team at Microsoft I primarily work on GPU workload management and also pod startup time as part of the node life cycle team we make it easy to run AI training and INF workload along with many other types of workloads on kubernetes I'm Ace I'm a software engineer at cooh here we build large language models uh I work on both our training and serving infrastructure one yeah in today's talk we'll start with a brief background on running AIML workloads on kubernetes talk about why job communication between different nodes and gpus is very critical then discuss about the various types of errors that can happen and show you a demo on how failure can be managed as well uh when this happens at the application layer then from the infr provider perspective we'll talk about how you can both proactively detect and manage errors through uh components like node problem detector and remedy controllers and we'll show a demo of this in action finally we'll touch upon brief briefly about Advanced scenarios and developments in the field around how you can make this more uh native to kubernetes and better from the end user perspective uh so a little bit of backgrounds if you're here you probably know something about llms you probably heard about chat GPT let's go back um so models are getting bigger they're hungrier for more data more compute to train them uh and we use kubernetes to run these jobs uh and these are jobs that span multiple pods multiple nodes likees mentioned it could be thousands of gpus um but these are one unit of work so we want them scheduled as a unit uh we don't want any Deadlocks where where our job is partially scheduled uh you might hear about things like volcano or q that support this kind of behavior today um you'll also hear about framework specific abstractions so if you've heard of cube flow you might hear abou
