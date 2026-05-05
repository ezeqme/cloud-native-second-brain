---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Kubernetes Core", "Sustainability"]
speakers: ["Tayebeh Bahreini", "Asser Tantawi", "IBM Research"]
sched_url: https://kccnceu2024.sched.com/event/1YeSb/caspian-a-carbon-optimized-multi-cluster-job-scheduler-tayebeh-bahreini-asser-tantawi-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=CASPIAN%3A+A+Carbon-Optimized+Multi-Cluster+Job+Scheduler+CNCF+KubeCon+2024
slides: []
status: parsed
---

# CASPIAN: A Carbon-Optimized Multi-Cluster Job Scheduler - Tayebeh Bahreini & Asser Tantawi, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]], [[Sustainability]]
- País/cidade: France / Paris
- Speakers: Tayebeh Bahreini, Asser Tantawi, IBM Research
- Schedule: https://kccnceu2024.sched.com/event/1YeSb/caspian-a-carbon-optimized-multi-cluster-job-scheduler-tayebeh-bahreini-asser-tantawi-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=CASPIAN%3A+A+Carbon-Optimized+Multi-Cluster+Job+Scheduler+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre CASPIAN: A Carbon-Optimized Multi-Cluster Job Scheduler.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSb/caspian-a-carbon-optimized-multi-cluster-job-scheduler-tayebeh-bahreini-asser-tantawi-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=CASPIAN%3A+A+Carbon-Optimized+Multi-Cluster+Job+Scheduler+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=h9FotOl8gK4
- YouTube title: CASPIAN: A Carbon-Optimized Multi-Cluster Job Scheduler - Tayebeh Bahreini & Asser Tantawi
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/caspian-a-carbon-optimized-multi-cluster-job-scheduler/h9FotOl8gK4.txt
- Transcript chars: 26406
- Keywords: carbon, cluster, clusters, intensity, caspan, casban, deadline, decision, workloads, running, energy, footprint, location, schedule, optimization, second, resource, scheduling

### Resumo baseado na transcript

hello everyone uh welcome to uh the talk on caspan the carbon aware scheduling and placement talk uh first let me congratulate you on your endurance and tenacity uh that you're coming and attending uh the very last uh s almost last session of the conference let me introduce myself first my name is Asser Tanta I'm with IBM research and my colleague here hello everyone my name is say Ry I'm a post researcher in iar all right so we'll walk you through this uh activity or project that

### Excerpt da transcript

hello everyone uh welcome to uh the talk on caspan the carbon aware scheduling and placement talk uh first let me congratulate you on your endurance and tenacity uh that you're coming and attending uh the very last uh s almost last session of the conference let me introduce myself first my name is Asser Tanta I'm with IBM research and my colleague here hello everyone my name is say Ry I'm a post researcher in iar all right so we'll walk you through this uh activity or project that we started uh it's not in in cncf but we're planning to be there we're going to talk about scheduling we're going to talk about dispatching we're going to talk about jobs uh multic clusters uh queuing coup Stellar but most importantly carbon and energy so what is Caspian uh the motivation for for us getting onto this project is obviously that the world is getting or trying to get greener and Greener and uh we all know that in data centers and in in clusters and kubernetes clusters especially now we have a lot of gpus and we have a lot of training jobs running and they they consume uh obviously a lot of GPU cycles for very long periods of time minutes hours days and and months in some cases so what we're trying to do is schedule jobs so that we can minimize the carbon footprint of running those jobs on those power hungry devices there are many things one could do uh we can make the devices more efficient you can make better cooling better this and that we're going to try with this project something very simple which is schedule jobs at the right time at the right place and I'll go through what do I mean by that and that's what casban is all about so I don't have to remind you of the amount of uh car the carbon footprint due to running these uh llm training and so on and so forth uh you know they're usually uh uh equivalent to I don't know they count how many round trips and how many car trips in a lifetime and so on you all know that the problem is that it's increasing it's getting worse by the day okay the good thing however that we exploiting in this project is that if you look at the generation of electricity that goes into these data centers come from uh various or a mix of of supplies of energy supplies some of them are renewable some of them are not and this this mix you see here on the left depends on the geography of where the data center is some geographies have more renewal percentage of mix than others you can see here this is real data uh from Canada for example in Tor
