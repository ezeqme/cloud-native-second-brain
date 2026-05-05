---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Matthias Bertschy", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwF/project-lightning-talk-transforming-your-application-behavior-to-kubernetes-objects-matthias-bertschy-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Transforming+your+Application+Behavior+to+Kubernetes+Objects+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Transforming your Application Behavior to Kubernetes Objects - Matthias Bertschy, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Matthias Bertschy, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwF/project-lightning-talk-transforming-your-application-behavior-to-kubernetes-objects-matthias-bertschy-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Transforming+your+Application+Behavior+to+Kubernetes+Objects+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Transforming your Application Behavior to Kubernetes Objects.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwF/project-lightning-talk-transforming-your-application-behavior-to-kubernetes-objects-matthias-bertschy-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Transforming+your+Application+Behavior+to+Kubernetes+Objects+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fok2apYcVdE
- YouTube title: Project Lightning Talk: Transforming your Application Behavior to Kubernetes Ob... Matthias Bertschy
- Match score: 0.985
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-transforming-your-application-behavior-to-kuber/fok2apYcVdE.txt
- Transcript chars: 3561
- Keywords: started, ebpf, instead, containers, application, memory, simple, server, objects, cubscape, cluster, scanning, incubation, thought, kernel, storage, separate, however

### Resumo baseado na transcript

So Cubscape started in 2021 as a static scanner for uh your communities cluster. Uh we were scanning your resources uh against some security frameworks and um I have some good news. Then we instead of sending full objects back and forth between the agents and the storage, we started to only send diffs which has the two benefits.

### Excerpt da transcript

So my name is Matias. I'm a co-maintainer of Cubscape. So Cubscape started in 2021 as a static scanner for uh your communities cluster. Uh we were scanning your resources uh against some security frameworks and um I have some good news. So this year we reached uh incubation. We started as a sandbox and now we are an incubation project. So uh when I joined uh the project it was like two and a half years ago more or less and there was something new at that time not new but like it was hot it was ebpf. So we thought how can we evolve from just scanning a cluster to include some ebpf uh goodies. So we said let's make uh let's start recording how application behave and then we can check if it's good or not if there are some deviations. So it seems simple. Uh so we wrote an agent using ebpf which would like monitor the containers through the Linux kernel and then just store all these uh behaviors as a CRD into the through the Kubernetes API. We even thought about writing our own storage component uh which allows to have a separate uh separate place to store them uh not in the TCD.

So seems simple. However, at the very beginning, one of the CR that we created was called application profile and it was very simple. We would track only one container. We would only record execs and opens. However, when developers have a game, they start playing a lot. So then we started tracking not only one container but all the containers of of a workload. So in it containers, FML containers, all the containers and instead of just the execs, we added the second profiles uh the endpoints that the application is talking to. So the different images, the call stacks, uh, policies, as a result, our CRD instead of being 100K became 100 megs. So as you can imagine, it caused some issues. So I'm going to tell a little bit of them. So you have the whole story on how we developed uh this feature. So first about the EBPF library. So we started using the falco liibs uh which were good because they were compatible with older Linux kernels. Unfortunately uh since it's old ebpf technology we were using a lot of CPU and a lot of memory.

So we moved to the inspector gadget libs which are like much better because you using newer ebpf libraries. We as I told you we were implementing our own API server but instead of using the sample API server we modified it heavily. Uh first modification obviously to store 100 megs you cannot really store them in etc. So instead of using etc we started to use file
