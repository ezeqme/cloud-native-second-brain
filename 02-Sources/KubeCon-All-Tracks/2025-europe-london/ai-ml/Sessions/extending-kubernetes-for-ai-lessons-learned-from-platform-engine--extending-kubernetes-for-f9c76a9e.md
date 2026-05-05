---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Susan Wu", "Google", "Lucy Sweet", "Uber", "Andrea Giardini", "Overstory", "Etienne Dilocker", "Weaviate.io", "Tim Wickberg", "SchedMD"]
sched_url: https://kccnceu2025.sched.com/event/1tx9e/extending-kubernetes-for-ai-lessons-learned-from-platform-engineering-susan-wu-google-lucy-sweet-uber-andrea-giardini-overstory-etienne-dilocker-weaviateio-tim-wickberg-schedmd
youtube_search_url: https://www.youtube.com/results?search_query=Extending+Kubernetes+for+AI+%7C+Lessons+Learned+From+Platform+Engineering+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Extending Kubernetes for AI | Lessons Learned From Platform Engineering - Susan Wu, Google; Lucy Sweet, Uber; Andrea Giardini, Overstory; Etienne Dilocker, Weaviate.io; Tim Wickberg, SchedMD

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Susan Wu, Google, Lucy Sweet, Uber, Andrea Giardini, Overstory, Etienne Dilocker, Weaviate.io, Tim Wickberg, SchedMD
- Schedule: https://kccnceu2025.sched.com/event/1tx9e/extending-kubernetes-for-ai-lessons-learned-from-platform-engineering-susan-wu-google-lucy-sweet-uber-andrea-giardini-overstory-etienne-dilocker-weaviateio-tim-wickberg-schedmd
- Busca YouTube: https://www.youtube.com/results?search_query=Extending+Kubernetes+for+AI+%7C+Lessons+Learned+From+Platform+Engineering+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Extending Kubernetes for AI | Lessons Learned From Platform Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9e/extending-kubernetes-for-ai-lessons-learned-from-platform-engineering-susan-wu-google-lucy-sweet-uber-andrea-giardini-overstory-etienne-dilocker-weaviateio-tim-wickberg-schedmd
- YouTube search: https://www.youtube.com/results?search_query=Extending+Kubernetes+for+AI+%7C+Lessons+Learned+From+Platform+Engineering+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=d9K5PSsHtDg
- YouTube title: Extending Kubernetes for AI | Lessons Learned From Platform... - Susan, Lucy, Andrea, Etienne, Tim
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/extending-kubernetes-for-ai-lessons-learned-from-platform-engineering/d9K5PSsHtDg.txt
- Transcript chars: 24848
- Keywords: platform, actually, workloads, database, company, questions, resources, vector, essentially, workload, course, training, satellite, images, especially, google, across, provider

### Resumo baseado na transcript

Uh Weeb8 is a vector database company, or actually it's more of a of an AI data platform these days, but it started out as a as a vector database company. We're one of the biggest end user deployments in the world which uh I'm sure we can get into later. What kind of customizations have you seen uh you know that people have been doing and if you have any adjacent projects that you've seen people bring in to Kubernetes? I have a session dedicated to how we do and that we try to handle these problems at over story. So in case you're interested, I have a talk later today right after lunch uh at level zero room J um where I will talk specifically on how we tackle these problems. So that's very high resolution, high imagery and the flexibility that we get with Kubernetes and having the possibility of having workloads that use one CPU and 2 gigs of memory or 72 CPUs and 450 gigs of memory.

### Excerpt da transcript

Hi, my name is Susan Woo. Thanks for staying back on Friday to hear from us. Um, I'm Susan Woo. I'm out in the pro I'm a product manager in Google Cloud. I focus on cloud networking, GKE networking, network security. We all wear a lot of hats here at Google. Thank you. So, with me, I have my panel, a steam panel. Uh, we're talking about extending Kubernetes for AI. So, come on up. Thank you very much. We have no uh walk-on music. Thank you. So, with that, I'm going to let the panelists introduce themselves. They're all miked up and ready. Cool. Thank you. Um yeah, hi, my name is co-founder and CTO of Weeb8. Uh Weeb8 is a vector database company, or actually it's more of a of an AI data platform these days, but it started out as a as a vector database company. And of course, we run a lot of AI workloads. uh on Kubernetes. Hi. Uh I'm the only one who wasn't miked up. We ran out of packs. Uh but my name's Lucy. I'm a engineer at Uber where I work on our platforms. Uh we have a quite substantial presence on Kubernetes.

We're one of the biggest end user deployments in the world which uh I'm sure we can get into later. And then we run a mix of a IML workloads both for training and for inference uh across non-critical stuff but also in the core trip flow of Uber. Good morning everyone. My name is Andrea. I work for a company called Overstory. We do vegetation management using satellite images. Basically, we use satellite images to prevent wildfires. And uh yeah, I'm here today to talk about how we use Kubernetes in the cloud in Google Cloud to yeah, make sure all our clients get their risk assessment on time using our platform. Um I'm Tim Wickberg. I'm the chief technical officer for Skidmd. uh were the principal slurm developers um also now the developers of slinky which is meant to be our set of integrations for bringing slurm scheduling wherewithal into the kubernetes stack. Okay. Uh I got a couple of prepared questions but I at some point I'll I'll have folks come on to the microphone and you can ask your questions directly.

Uh so starting with Lucy you know for platform engineers or infrastructure engineers do do you typically provide Kubernetes clusters for sort of conventional uh microservices orchestration or do you have dedicated teams for a IML workloads so um our approach is that we don't bad time for a cough our approach is that we don't uh directly offer what I would call maybe Kubernetes as a service uh our worry is that it's very expansive and it
