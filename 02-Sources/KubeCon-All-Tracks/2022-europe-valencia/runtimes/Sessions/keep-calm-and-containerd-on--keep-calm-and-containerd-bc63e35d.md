---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Runtimes"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Anusha Ragunathan", "Intuit Inc"]
sched_url: https://kccnceu2022.sched.com/event/ytqI/keep-calm-and-containerd-on-anusha-ragunathan-intuit-inc
youtube_search_url: https://www.youtube.com/results?search_query=Keep+Calm+and+Containerd+On%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Keep Calm and Containerd On! - Anusha Ragunathan, Intuit Inc

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Runtimes]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Spain / Valencia
- Speakers: Anusha Ragunathan, Intuit Inc
- Schedule: https://kccnceu2022.sched.com/event/ytqI/keep-calm-and-containerd-on-anusha-ragunathan-intuit-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Keep+Calm+and+Containerd+On%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Keep Calm and Containerd On!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqI/keep-calm-and-containerd-on-anusha-ragunathan-intuit-inc
- YouTube search: https://www.youtube.com/results?search_query=Keep+Calm+and+Containerd+On%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nQAvkHJ4xak
- YouTube title: Keep Calm and Containerd On! - Anusha Ragunathan, Intuit Inc
- Match score: 0.731
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keep-calm-and-containerd-on/nQAvkHJ4xak.txt
- Transcript chars: 19159
- Keywords: container, docker, actually, cluster, migration, socket, daemon, runtime, running, kubelet, gpu, around, add-ons, management, logs, format, basically, performance

### Resumo baseado na transcript

welcome everyone today i'll be talking about how to keep calm and container deon my name is anusha raghunathan and i'm a principal software engineer at intuit introvid is a fintech company that makes software around tax preparation accounting consumer credit reports and stuff so if you've ever used turbotax mint credit karma or quickbooks then that's us the agenda for today is basically starting off with why why are we even doing this talk what is the background what are cris then we'll do a section on how we

### Excerpt da transcript

welcome everyone today i'll be talking about how to keep calm and container deon my name is anusha raghunathan and i'm a principal software engineer at intuit introvid is a fintech company that makes software around tax preparation accounting consumer credit reports and stuff so if you've ever used turbotax mint credit karma or quickbooks then that's us the agenda for today is basically starting off with why why are we even doing this talk what is the background what are cris then we'll do a section on how we went ahead planning the migration to this new cri what happened during our great migration and some performance analysis that we did with the new cri and finally finish it off with takeaways before we get started i want to give a quick intro introduction about our kubernetes based infrastructure we run about 220 plus clusters and they average about 16 000 nodes and this number of nodes actually goes up pretty high during our tax peak seasons and a number of kubernetes namespaces roughly about 15 000 and odd we run about 2000 production services on this kubernetes-based infrastructure serving about 5000 developers and we have about 17 000 assets that we manage with this and each kubernetes cluster runs about 25 add-ons on top of the vanilla kubernetes cluster we get these are primarily around security and compliance cluster life cycle management i want to call out our keiko proj which is a intuit uh started open source project that manages our cluster add-ons instance management upgrade management and stuff then we have add-ons around observability metrics tracing and logging networking cni and service mesh storage reliability testing around chaos experiments and finally container native workflow engines specifically argo workflows now what's a cri a cri is a container runtime interface and kubernetes has interfaces for running your storage and running your network container networking using cni and csi similar to that for running a container and doing some image management there is a cri interface that the kubelet calls out to and a high level container runtime like docker shim or container d manages of containers and images life cycle of them and in in in turn calls out to a low level container runtime such as run c and a cri is a well established uh interface that the kublet calls over and it's grpc based and examples of container runtimes like i mentioned docker shim cryo and container d now why is it that we're talking about container d and cri an
