---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["Kubernetes Core"]
speakers: ["Jago Macleod", "Engineering Director", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2HgNv/sponsored-keynote-from-cloud-native-to-accelerator-native-kubernetes-as-the-distributed-os-for-accelerated-workloads-and-frameworks-jago-macleod-engineering-director-google
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Cloud+Native+to+Accelerator+Native%3A+Kubernetes+as+the+Distributed+OS+for+Accelerated+Workloads+and+Frameworks+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sponsored Keynote: From Cloud Native to Accelerator Native: Kubernetes as the Distributed OS for Accelerated Workloads and Frameworks - Jago Macleod, Engineering Director, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jago Macleod, Engineering Director, Google
- Schedule: https://kccnceu2026.sched.com/event/2HgNv/sponsored-keynote-from-cloud-native-to-accelerator-native-kubernetes-as-the-distributed-os-for-accelerated-workloads-and-frameworks-jago-macleod-engineering-director-google
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Cloud+Native+to+Accelerator+Native%3A+Kubernetes+as+the+Distributed+OS+for+Accelerated+Workloads+and+Frameworks+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: From Cloud Native to Accelerator Native: Kubernetes as the Distributed OS for Accelerated Workloads and Frameworks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgNv/sponsored-keynote-from-cloud-native-to-accelerator-native-kubernetes-as-the-distributed-os-for-accelerated-workloads-and-frameworks-jago-macleod-engineering-director-google
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+From+Cloud+Native+to+Accelerator+Native%3A+Kubernetes+as+the+Distributed+OS+for+Accelerated+Workloads+and+Frameworks+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4jP9lSZslSQ
- YouTube title: Sponsored Keynote: From Cloud Native to Accelerator Native: Kubernetes as the Distri... Jago Macleod
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sponsored-keynote-from-cloud-native-to-accelerator-native-kubernetes-a/4jP9lSZslSQ.txt
- Transcript chars: 6140
- Keywords: hardware, google, platform, talked, ecosystem, infrastructure, innovation, workloads, working, stability, velocity, developers, pretty, applications, operating, underlying, topology, workload

### Resumo baseado na transcript

I lead Kubernetes at Google and it's never been more fun than it is right now. As the creators and the most active maintainers of Kubernetes, I wanted to share some of what the community is working on and why and how it'll help you make some stability in the chaos. And if you're a hardware provider and you integrate with Kubernetes, you are available to the entire ecosystem essentially for free. Step one was about uh re-imagining the Kubernetes relationship with the underlying hardware. So right now in Kubernetes 136, the workload API is emerging as this place where we're pulling in uh support for gang scheduling to schedule an entire job together, workload aware preeemption and the topology that we talked about. So some of our core investments, we talked about topology and workload awareness, we talked about DRRA, and then the agent sandbox we announced last in November has really taken off to provide the safety you need to run agentic workloads at scale and safely.

### Excerpt da transcript

Hi, I'm JGO Mloud and I have the greatest job in the world. I lead Kubernetes at Google and it's never been more fun than it is right now. It's also never moved faster. As the creators and the most active maintainers of Kubernetes, I wanted to share some of what the community is working on and why and how it'll help you make some stability in the chaos. At Google, we often write down a vision statement to help focus the team. Right now, our focus is on velocity and utilization. And I'll share why those two ideas are helping us shape the future. Kubernetes has this amazing flywheel effect that starts with developers, gets amplified by the platform team, and then gets accelerated by the ecosystem. And we'll talk a little bit about each of those. For developers, it's all about velocity. And Kubernetes gives developers a platform that provides velocity, flexibility, and scalability without a lot of work for them. The platform team, it's about efficiency. And so you have to have operational speed, but also reliability and of course scaling.

But the ecosystem is where the magic really happens. I talk about Kubernetes as the narrow waste of the hourglass of infrastructure, but it's not a bottleneck. It's actually a birectional megaphone. And it's really interesting. If you work on a framework like Ray or Slurm at the top and you write to the Kubernetes APIs, you get access to all of the infrastructure providers and emerging hardware. And if you're a hardware provider and you integrate with Kubernetes, you are available to the entire ecosystem essentially for free. It's super powerful and this becomes this distribution engine in both directions. It's really pretty awesome. Kubernetes emerged in a few phases. Phase one of course was about container orchestration and this was the big breakthrough. We started with stateless applications and then moved on to stateful and batch and more. And phase two is the ecosystem explosion that you see the 200 plus projects in the CNCF today. And that's that magic we just talked about. And phase three we think of as the distributed operating system for AI.

What does that mean? Operating systems really shift the focus to resource management and the extensible frameworks that let you run different kinds of workloads on the same uh underlying infrastructure. And then heterogeneous hardware is a place where hardware is really fun and moving fast right now. So we've been working harder than ever. Step one was about uh re-imagining th
