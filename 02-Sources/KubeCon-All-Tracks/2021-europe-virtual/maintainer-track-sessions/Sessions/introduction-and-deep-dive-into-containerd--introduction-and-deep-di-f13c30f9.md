---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Kohei Tokunaga", "Akihiro Suda", "NTT Corporation"]
sched_url: https://kccnceu2021.sched.com/event/iE6v/introduction-and-deep-dive-into-containerd-kohei-tokunaga-akihiro-suda-ntt-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Introduction+and+Deep+Dive+Into+Containerd+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Introduction and Deep Dive Into Containerd - Kohei Tokunaga & Akihiro Suda, NTT Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Kohei Tokunaga, Akihiro Suda, NTT Corporation
- Schedule: https://kccnceu2021.sched.com/event/iE6v/introduction-and-deep-dive-into-containerd-kohei-tokunaga-akihiro-suda-ntt-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Introduction+and+Deep+Dive+Into+Containerd+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Introduction and Deep Dive Into Containerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE6v/introduction-and-deep-dive-into-containerd-kohei-tokunaga-akihiro-suda-ntt-corporation
- YouTube search: https://www.youtube.com/results?search_query=Introduction+and+Deep+Dive+Into+Containerd+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LNMPg5n2lf0
- YouTube title: Introduction and Deep Dive Into Containerd - Kohei Tokunaga & Akihiro Suda, NTT Corporation
- Match score: 0.736
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/introduction-and-deep-dive-into-containerd/LNMPg5n2lf0.txt
- Transcript chars: 19270
- Keywords: quantity, client, content, continuity, container, runtime, images, docker, contents, snapshot, several, including, management, runtimes, plugin, containers, provides, library

### Resumo baseado na transcript

hi i'm kohei tokunaga from ntt corporation i'm a reviewer of continuity and the maintenance of non-kwasa project sergeant snapshot in containery i'm joined today by akihiro soda from ntg corporation he is a maintainer of contrary project today we will introduce and div dive into constantly first i'm going to give you a brief introduction to continuity quantity is a consumer runtime project it is the fifth cncf graduated project containing manages resources about containers including container processes images file system metadata and resource dependencies then it provides clean

### Excerpt da transcript

hi i'm kohei tokunaga from ntt corporation i'm a reviewer of continuity and the maintenance of non-kwasa project sergeant snapshot in containery i'm joined today by akihiro soda from ntg corporation he is a maintainer of contrary project today we will introduce and div dive into constantly first i'm going to give you a brief introduction to continuity quantity is a consumer runtime project it is the fifth cncf graduated project containing manages resources about containers including container processes images file system metadata and resource dependencies then it provides clean interface to upper tools i will introduce internal architecture of continuity data as well quantity is tightly scoped but it's highly extensible in community there are many projects that leverage this quantity with extending it extensibility is also one of the major topics in this session i will introduce some examples about how to extend continuity quantity is now widely used by container-based tools in community including kubernetes and docker let's now focus on the adoption status in community from the next slide container is widely used in community including docker's use of continuity continuity is 83 percent of container usage according to the survey in 2021 container is used by managed services as well as open source projects including managed services like gke aws fargate aks ats development tools like docker mobile build kit humanities distributions like k3f kind mini cube cube spray micro ks and k3s and functional service like fasti if you are using either of these tools you are already using continuity so how quantum d is used in community quantity is mainly used in three different ways it's used as a cri runtime on kubernetes as a component of docker and as a general content management tool by various content id based tools let's keep a look at each of them one of the most well-known use cases of quantity is as a cri runtime on kubernetes as shown in the diagram quantum d runs on each node when cubelet on the node detects spots events from cube api server cubelet invokes quantities concern management functionalities the api used by cubelet is called cry as a cri runtime content reports images from registry and manages spots contents and images it pulls and stores images from the registry and executes them as contrast using low level runtimes including run c devices and cata containers etc it is now the default standard cri runtime for kubernetes it's used by various mana
