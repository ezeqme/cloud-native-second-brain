---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Antonio Ojea", "Benjamin Elder", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YhhY/keep-calm-and-load-balance-on-kind-antonio-ojea-benjamin-elder-google
youtube_search_url: https://www.youtube.com/results?search_query=Keep+Calm+and+Load+Balance+on+KIND+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keep Calm and Load Balance on KIND - Antonio Ojea & Benjamin Elder, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Antonio Ojea, Benjamin Elder, Google
- Schedule: https://kccnceu2024.sched.com/event/1YhhY/keep-calm-and-load-balance-on-kind-antonio-ojea-benjamin-elder-google
- Busca YouTube: https://www.youtube.com/results?search_query=Keep+Calm+and+Load+Balance+on+KIND+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keep Calm and Load Balance on KIND.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhhY/keep-calm-and-load-balance-on-kind-antonio-ojea-benjamin-elder-google
- YouTube search: https://www.youtube.com/results?search_query=Keep+Calm+and+Load+Balance+on+KIND+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=U6_-y24rJnI
- YouTube title: Keep Calm and Load Balance on KIND - Antonio Ojea & Benjamin Elder, Google
- Match score: 0.74
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keep-calm-and-load-balance-on-kind/U6_-y24rJnI.txt
- Transcript chars: 25679
- Keywords: balancer, cluster, docker, traffic, terminating, container, running, application, network, balance, important, provider, create, another, everything, implementation, deployment, support

### Resumo baseado na transcript

hello everyone thanks for coming uh my name is Benjamin Elder and this is Antonio hea we're both senior software engineers at Google and our talk is on keep calm and load balance with kind so what is kind kind is kubernetes and Docker um it's a tool that we built for testing the kubernetes project initially um it uses Docker containers to simulate nodes so you can run them locally and it can build and run kubernetes from sour as long as as well as some pre-built images it

### Excerpt da transcript

hello everyone thanks for coming uh my name is Benjamin Elder and this is Antonio hea we're both senior software engineers at Google and our talk is on keep calm and load balance with kind so what is kind kind is kubernetes and Docker um it's a tool that we built for testing the kubernetes project initially um it uses Docker containers to simulate nodes so you can run them locally and it can build and run kubernetes from sour as long as as well as some pre-built images it boots a cluster in 30 seconds because everything is packed into the container and running locally um this was really important for us for the kubernetes project to have very cheap fast local testing because we need to test changes of kubernetes constantly it's minimal but fully conformant want something is simple and streamlined uh and flexible it has multi- Noe support which is required to actually run all of the conformance tests properly because there's some tests around rolling node behavior and it has persistent volume support everything else comes from kubernetes core itself and the rest is just getting those to run we have a very very minimal lightweight networking agent called KET D it just ensures that pods are ratable between nodes with the minimal simplest cni there's no load balancer and no Ingress we have bring your own and some docks for that so that's where the project is coming from it looks a little bit like this so you've got Docker running on your host within each Docker container for the node we have system D because we need an anit process for kubernetes uh we're running container D and we have a bunch of images for all the kubernetes project and the binaries we run cubet and our KET depod and everything else is standard kubernetes so you have some cord Paws Cube proxy Cube controller manager etcd Cube API server and your user workloads and these are in nested containers um if you're familiar with Docker and Docker it's the same idea in kubernetes CI we actually run on kubernetes so we wind up with um container D and Docker in container D it's it's it works I I I don't recommend it but it it solved our problems so as I said it supports multi Noe which looks something like this spread across if you have a single node we'll just untaint the node and you can run your workloads there and for most application testing that's what's appropriate but for testing kubernetes we really need to test Behavior across nodes so it looks like a pretty standard Cub adom cluster it's pow
