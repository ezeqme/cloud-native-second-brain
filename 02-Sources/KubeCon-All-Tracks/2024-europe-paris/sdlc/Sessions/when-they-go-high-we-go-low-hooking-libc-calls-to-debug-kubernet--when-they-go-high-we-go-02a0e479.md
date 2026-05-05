---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["Kubernetes Core"]
speakers: ["Tal Zwick", "MetalBear"]
sched_url: https://kccnceu2024.sched.com/event/1YeN7/when-they-go-high-we-go-low-hooking-libc-calls-to-debug-kubernetes-apps-tal-zwick-metalbear
youtube_search_url: https://www.youtube.com/results?search_query=When+They+Go+High%2C+We+Go+Low+%E2%80%93+Hooking+Libc+Calls+to+Debug+Kubernetes+Apps+CNCF+KubeCon+2024
slides: []
status: parsed
---

# When They Go High, We Go Low – Hooking Libc Calls to Debug Kubernetes Apps - Tal Zwick, MetalBear

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Tal Zwick, MetalBear
- Schedule: https://kccnceu2024.sched.com/event/1YeN7/when-they-go-high-we-go-low-hooking-libc-calls-to-debug-kubernetes-apps-tal-zwick-metalbear
- Busca YouTube: https://www.youtube.com/results?search_query=When+They+Go+High%2C+We+Go+Low+%E2%80%93+Hooking+Libc+Calls+to+Debug+Kubernetes+Apps+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre When They Go High, We Go Low – Hooking Libc Calls to Debug Kubernetes Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeN7/when-they-go-high-we-go-low-hooking-libc-calls-to-debug-kubernetes-apps-tal-zwick-metalbear
- YouTube search: https://www.youtube.com/results?search_query=When+They+Go+High%2C+We+Go+Low+%E2%80%93+Hooking+Libc+Calls+to+Debug+Kubernetes+Apps+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3OSQdiKTNU8
- YouTube title: When They Go High, We Go Low – Hooking Libc Calls to Debug Kubernetes Apps - Tal Zwick, MetalBear
- Match score: 0.957
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/when-they-go-high-we-go-low-hooking-libc-calls-to-debug-kubernetes-app/3OSQdiKTNU8.txt
- Transcript chars: 28293
- Keywords: application, cluster, running, binary, dynamic, function, actually, library, basically, process, environment, support, simple, requests, configuration, native, locally, machine

### Resumo baseado na transcript

hello everybody and welcome to this talk titled when they go high we go low my name is talsik and I'm a developer at mle bear where we develop mird so this talk is about solving a seemingly high level problem using quite low-level techniques specifically the problem of cloud native developer experience and more specifically we will discuss M which is a Dev tool written in Rust um that is for developing Cloud native applications mird enables cluster connected but local execution of cloud native applications and what that

### Excerpt da transcript

hello everybody and welcome to this talk titled when they go high we go low my name is talsik and I'm a developer at mle bear where we develop mird so this talk is about solving a seemingly high level problem using quite low-level techniques specifically the problem of cloud native developer experience and more specifically we will discuss M which is a Dev tool written in Rust um that is for developing Cloud native applications mird enables cluster connected but local execution of cloud native applications and what that means and what it looks like will become clear as we move on so as I said the high level challenge Mir addresses is cloud native developer experience and more specifically just being able to run your code while developing it and the solution Mir deploys is at the operating system process level um first we're going to talk about what M is for once that is out of the way we're going to take a look at some of the lowlevel technical details of the implementation of mird and then to wrap it all up there's going to be a short life demo of Mir and during this talk I hope you'll um understand why we went in this very lowlevel direction for MD and also kind of how it works in general terms so first what M is for running the code you're working on while developing is useful and helpful and with many types of software that is a simple enough task but often when it comes to Cloud native applications that can become not so trivial at all um but I believe that we shouldn't abandon useful development patterns and practices because they're harder to implement with Cloud native applications which is just develop the tool link to make them easy but how do you run your Cloud native application while developing the application if it for example accesses um files that only exist on the cluster or if it uses other services in the cluster over IP or or if you need another service in order to generate requests to your application and besides running your code often is good and you might not want to spend time containerizing and deploying it after every little code change you want to test out um so there are multiple existing approaches to solving that problem they don't offer the same capabilities and they don't all result in the same kind of workflow uh but other tools to for example try to um just enable remote debugging in the cloud or they're uh for running everything locally on the development machine the approach Mir D takes is to enable local development wi
