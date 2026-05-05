---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Research + Academia + HPC + Advanced Concepts"
themes: ["Kubernetes Core"]
speakers: ["Paul Schweigert", "Michael Maximilien", "IBM"]
sched_url: https://kccnceu2023.sched.com/event/1HyYN/cloud-native-quantum-running-quantum-serverless-workloads-on-kubernetes-paul-schweigert-michael-maximilien-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Native+Quantum%3A+Running+Quantum+Serverless+Workloads+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cloud-Native Quantum: Running Quantum Serverless Workloads on Kubernetes - Paul Schweigert & Michael Maximilien, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Research + Academia + HPC + Advanced Concepts]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Paul Schweigert, Michael Maximilien, IBM
- Schedule: https://kccnceu2023.sched.com/event/1HyYN/cloud-native-quantum-running-quantum-serverless-workloads-on-kubernetes-paul-schweigert-michael-maximilien-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Native+Quantum%3A+Running+Quantum+Serverless+Workloads+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cloud-Native Quantum: Running Quantum Serverless Workloads on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYN/cloud-native-quantum-running-quantum-serverless-workloads-on-kubernetes-paul-schweigert-michael-maximilien-ibm
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Native+Quantum%3A+Running+Quantum+Serverless+Workloads+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kvD-Y70DOno
- YouTube title: Cloud-Native Quantum: Running Quantum Serverless Workloads on Kubernetes - Schweigert & Maximilien
- Match score: 0.946
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cloud-native-quantum-running-quantum-serverless-workloads-on-kubernete/kvD-Y70DOno.txt
- Transcript chars: 32872
- Keywords: quantum, circuit, computers, actually, problems, algorithm, qubits, number, little, results, running, computer, basically, serverless, workloads, classical, program, numbers

### Resumo baseado na transcript

well thank you for coming this talk is going to be the first time we do it um so hopefully you cut us some slack but you know feel free to ask questions I mean you know so don't make it easy um so I'll introduce us quickly so this is my colleague Paul he's a senior engineer at IBM and does all kinds of things if you go to the k-native booth you will see him because he's a committer and has contributed tons to k-native but now is technology is improving much faster and the qubits are better and better meaning that they're more perfect meaning that you don't have to do error correction so the number of operations is getting close to what you would expect intros algorithm so for some problems and that's the key thing quantum computers will make solving those problems extremely extremely fast just as a last thing I know we'll go to Paul around November of last year there was a group of Chinese researchers that claimed that they were able to a lot of quantum machine learning we have algorithms for that that people can use in chemistry and things like that as Max was saying you know some of these chemical reactions there are applications out there that you can use that you can pull in we're going to demo one of those a little later Finance is big in Quantum optimizations you know the traveling sales person that Max mentioned there's algorithms out there for that that you can use...

### Excerpt da transcript

well thank you for coming this talk is going to be the first time we do it um so hopefully you cut us some slack but you know feel free to ask questions I mean you know so don't make it easy um so I'll introduce us quickly so this is my colleague Paul he's a senior engineer at IBM and does all kinds of things if you go to the k-native booth you will see him because he's a committer and has contributed tons to k-native but now is working with me on open quantum at IBM so max some people call me Dr Max but Max is fine yes I do have a PhD but it's not in quantum physics so so this is New Territory for me and I'm a distinguished engineer at IBM and I also used to do open serverless so I did contribute to K native as well pioneering the CLI so you know we can talk about that and the quantum effort came because as you'll see there's a little bit of overlap but not too much so that's that okay so the talk is divided into three parts I'm gonna do the first part and um Paul is actually gonna go over how so I'm gonna try to give you my best intuition of quantum Computing or quantum computers and more importantly why are they important why why should you care and Paul is gonna get into a little bit more details by going over how you actually program or come to a computer at least using some of the tools that we have at IBM and then how kubernetes can actually play into this uh emerging field and there's going to be some live demos as well so hopefully it works okay so what is quantum Computing I mean obviously everybody here probably have some notion of regular computers and just giving myself some time so I don't speak too much and of course you know the you know we all have you know supercomputers in our pockets right and quantum computers are actually very different but fundamentally there's some some similarities as well right so we're going to try to at least give you the intuition uh behind them so first is you know thinking of yeah problems right so if you've taken a complexity Theory class you know that computers are are a great at solving problems but believe it or not there's a lot of problem that you cannot solve or at least it would take you so much time to solve them that the best computers we have right now are even super computer is much bigger than the ones you have in your pocket uh would not be able to solve them and part of the reason is because the best algorithms that we know tend to require a lot of operations and computers are pretty straightfo
