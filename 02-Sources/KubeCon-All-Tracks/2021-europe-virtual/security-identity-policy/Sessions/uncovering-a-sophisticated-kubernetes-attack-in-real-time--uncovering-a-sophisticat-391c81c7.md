---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jed Salazar", "Natália Réka Ivánkó", "Isovalent"]
sched_url: https://kccnceu2021.sched.com/event/iE2u/uncovering-a-sophisticated-kubernetes-attack-in-real-time-jed-salazar-natalia-reka-ivanko-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Uncovering+a+Sophisticated+Kubernetes+Attack+in+Real-Time+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Uncovering a Sophisticated Kubernetes Attack in Real-Time - Jed Salazar & Natália Réka Ivánkó, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Jed Salazar, Natália Réka Ivánkó, Isovalent
- Schedule: https://kccnceu2021.sched.com/event/iE2u/uncovering-a-sophisticated-kubernetes-attack-in-real-time-jed-salazar-natalia-reka-ivanko-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Uncovering+a+Sophisticated+Kubernetes+Attack+in+Real-Time+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Uncovering a Sophisticated Kubernetes Attack in Real-Time.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2u/uncovering-a-sophisticated-kubernetes-attack-in-real-time-jed-salazar-natalia-reka-ivanko-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Uncovering+a+Sophisticated+Kubernetes+Attack+in+Real-Time+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bohnofE_dvw
- YouTube title: Uncovering a Sophisticated Kubernetes Attack in Real-Time - Jed Salazar & Natália Réka Ivánkó
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/uncovering-a-sophisticated-kubernetes-attack-in-real-time/bohnofE_dvw.txt
- Transcript chars: 17680
- Keywords: security, container, environment, observability, actually, ebpf, program, attack, detect, detection, protections, access, inside, within, network, behavior, attacks, kernel

### Resumo baseado na transcript

welcome to uncovering the sophisticated kubernetes attack in real time kubernetes has become the de facto cloud operating system and every day more and more critical applications are containerized and moved to kubernetes this means kubernetes is quickly becoming a crucial component to secure today we as defenders are in the dark because we lack the observability needed to detect and respond to attacks on our workloads today we'll show you how we can build out a detection program to uncover a sophisticated attack against a kubernetes cluster hi i'm

### Excerpt da transcript

welcome to uncovering the sophisticated kubernetes attack in real time kubernetes has become the de facto cloud operating system and every day more and more critical applications are containerized and moved to kubernetes this means kubernetes is quickly becoming a crucial component to secure today we as defenders are in the dark because we lack the observability needed to detect and respond to attacks on our workloads today we'll show you how we can build out a detection program to uncover a sophisticated attack against a kubernetes cluster hi i'm jed salazar platform security at tesla i like mountains and distributed systems hey my name is natalia and i'm a security engineer and i surveillance i really like traveling and flying on planes observability in distributed systems is a crucial element in detecting issues and making changes to improve the stability and security of the system so for sre we use things like prometheus to actually come up with metrics to define how we can actually improve the reliability of a service what we're advocating for is that security takes the same approach being data driven and using data to drive forward security improvements within our system so a lot of security today practices they really focus on the pre-fail and post-fail approach to security pre-fail tries to predict the necessary protections that a system is going to require based on threat modeling or an assumption of risk post fail ensures that you have the necessary logs for intrusion detection to be notified if you get compromised despite those protections what we're advocating for is that we actually change that paragon and we move from a pre-fail and post-fail to a pre-data and post data paradigm data allows us to continually measure that our hardening and security configurations are suitable to protect against real world threats that are attacked that are detected by observability within our environment with observability we will open your eyes to the reality of the threats in your environment so how do we secure this this is the cncf landscape basically the set of tools and systems that make up the kubernetes ecosystem i like to call this the cncf threat landscape if you're tasked with securing kubernetes you might look at this landscape and become overwhelmed it takes a lot of resources and time to successfully build and operate a cloud-native environment let alone secure it however different components of your stack have different levels of risk and priori
