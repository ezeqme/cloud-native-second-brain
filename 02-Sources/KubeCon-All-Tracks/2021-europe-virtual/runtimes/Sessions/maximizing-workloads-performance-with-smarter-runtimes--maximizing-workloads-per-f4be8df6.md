---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Runtimes"
themes: ["Runtime Containers", "SRE Reliability"]
speakers: ["Krisztian Litkey", "Alexander Kanevskiy", "Intel"]
sched_url: https://kccnceu2021.sched.com/event/iE1Y/maximizing-workloads-performance-with-smarter-runtimes-krisztian-litkey-alexander-kanevskiy-intel
youtube_search_url: https://www.youtube.com/results?search_query=Maximizing+Workload%27s+Performance+With+Smarter+Runtimes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Maximizing Workload's Performance With Smarter Runtimes - Krisztian Litkey & Alexander Kanevskiy, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Runtimes]]
- Temas: [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Krisztian Litkey, Alexander Kanevskiy, Intel
- Schedule: https://kccnceu2021.sched.com/event/iE1Y/maximizing-workloads-performance-with-smarter-runtimes-krisztian-litkey-alexander-kanevskiy-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Maximizing+Workload%27s+Performance+With+Smarter+Runtimes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Maximizing Workload's Performance With Smarter Runtimes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1Y/maximizing-workloads-performance-with-smarter-runtimes-krisztian-litkey-alexander-kanevskiy-intel
- YouTube search: https://www.youtube.com/results?search_query=Maximizing+Workload%27s+Performance+With+Smarter+Runtimes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BwQmjunIsFI
- YouTube title: Maximizing Workload's Performance With Smarter Runtimes - Krisztian Litkey & Alexander Kanevskiy
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/maximizing-workloads-performance-with-smarter-runtimes/BwQmjunIsFI.txt
- Transcript chars: 18177
- Keywords: memory, resource, resources, container, runtimes, hardware, multiple, workloads, runtime, algorithms, containers, performance, cubelet, caches, control, requirements, smarter, understand

### Resumo baseado na transcript

hello kubecon welcome to our session i'm alexander kaninsky i'm cloud software architect working for intel and today with my colleague we are going to talk about something interesting in the run times track hello cubecon my name is christian litke i work for intel finland as a linux and cloud software engineer maximizing workloads performance with smarter runtimes we will take a look at performance optimization how kubernetes models hardware detour into hardware domains and then talk about smart runtimes so let me first start with achieving my performance we share common interest with nri it aims improving node resource management with a structured api and plug-in design for containers we would like to do pretty much the same it wants additional interfaces to customize and con a container's runtime environment we also would

### Excerpt da transcript

hello kubecon welcome to our session i'm alexander kaninsky i'm cloud software architect working for intel and today with my colleague we are going to talk about something interesting in the run times track hello cubecon my name is christian litke i work for intel finland as a linux and cloud software engineer maximizing workloads performance with smarter runtimes we will take a look at performance optimization how kubernetes models hardware detour into hardware domains and then talk about smart runtimes so let me first start with achieving my performance optimization comes down to a very known problem of noisy neighbors we all have dozens of hundreds of workloads running now and and all of those workloads they have a different characteristics different life cycles and so on so one thing which i want to say in the very beginning the silver moon doesn't exist even though if you have some good algorithms to optimize one set of workloads most probably for ourselves it will have differences and the reason for that is what like we all have differences in the cpus caches memory and our hardware resources when usage of patterns of those resources also differs what is important is what you need to understand how those resources are used how you can measure them and how you can react in those events of the life cycle of those workloads today in our scope is just a container runtimes dryer container b and some interfaces waters connecting roads pieces together and even though here i'm talking about theory of things we we have a project which is called cri resource manager where we validated most of our materials theories and we have practical examples of what can be achieved by extending the runtimes but let's talk about how the resources are recognized how we can look at them in our kubernetes world where pristine and vanilla installation of kubernetes you have a very simplified model of resources everything is one big share pool every cpu is record every memory region is again one big shared set of resources and obviously in this setup you are not able to provide too much of your controls you have some priorities but that's it to fully embrace our control we need to start dividing those resources into a smaller challenge so we can when you can measure and control one and when people are thinking about the divisions of standard computer resources where you immediately came to the idea of no one and this current implementation of aluminum kubernetes you still have o
