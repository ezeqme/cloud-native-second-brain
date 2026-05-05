---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Felix Hoffmann", "iteratec"]
sched_url: https://kccnceu2023.sched.com/event/1HyWp/how-to-blow-up-a-kubernetes-cluster-felix-hoffmann-iteratec
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Blow+up+a+Kubernetes+Cluster+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How to Blow up a Kubernetes Cluster - Felix Hoffmann, iteratec

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Felix Hoffmann, iteratec
- Schedule: https://kccnceu2023.sched.com/event/1HyWp/how-to-blow-up-a-kubernetes-cluster-felix-hoffmann-iteratec
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Blow+up+a+Kubernetes+Cluster+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How to Blow up a Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWp/how-to-blow-up-a-kubernetes-cluster-felix-hoffmann-iteratec
- YouTube search: https://www.youtube.com/results?search_query=How+to+Blow+up+a+Kubernetes+Cluster+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rjSWVeAvb24
- YouTube title: How to Blow up a Kubernetes Cluster - Felix Hoffmann, iteratec
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-to-blow-up-a-kubernetes-cluster/rjSWVeAvb24.txt
- Transcript chars: 16543
- Keywords: memory, limits, request, resources, requests, actually, always, quality, resource, guaranteed, cluster, application, course, schedule, second, documentation, exceed, terminated

### Resumo baseado na transcript

welcome um welcome to my talk how to blow up a kubernetes cluster sorry about the clickbait but judging by how crowd the rumors I guess it kind of worked um I hope some of you have read the talks description because if you haven't you'll be disappointed to learn that this is actually about resource management and it's about Resource Management from the point of view of an application developer because that's who I am I'm an application developer my name is Felix I'm a software engineer at italatech

### Excerpt da transcript

welcome um welcome to my talk how to blow up a kubernetes cluster sorry about the clickbait but judging by how crowd the rumors I guess it kind of worked um I hope some of you have read the talks description because if you haven't you'll be disappointed to learn that this is actually about resource management and it's about Resource Management from the point of view of an application developer because that's who I am I'm an application developer my name is Felix I'm a software engineer at italatech we are a consultancy slash agency based in Germany and the reason why I'm giving this talk is because last year I was I gained access to a kubernetes cluster and I didn't really have a clue on how kubernetes works and I was told there were some parts that need limits and they need requests set and I read about it in the documentation and I thought I was doing good things but it turned out the entire thing blew up and this is why I'm giving this talk and since this is the one-on-one track I'll start from the top so let's look at what the documentation has to say about resources now when we talk about resources obviously we're talking about compute resources and there's CPU there's memory these are the obvious ones there's tons more like ephemeral storage there's PID limiting and many more but for the purpose of this talk I'll concentrate on CPU and memory now the documentation tells us how we can set requests and limits and it defines requests as the amounts of memory and CPU that is guaranteed for our containers and limits is the amount of CPU or memory that we cannot exceed with our containers and there are different units we can use to set these um settings so for CPU we have one CPU unit which is one core either physical or virtual and we can use different fractions for this core and we can Define these fractions using Milli CPU or milli core whereas 1000 Milli core equals to one CPU unit and for memory the base unit is byte and we can use all kinds of um kilobyte up to exabyte and the binary equivalent Cube byte up to XP byte of course now when we look at a plot definition file when we Define those requests and limits they look like this for this part or for this container rather they're always on a container basis we have defined a request of 64 maybe byte and a CPU request of 250 Milli core and the limit is two times our request so we have 128 megabytes and 500 millicore now what does happen with our part when we exceed our memory limit and that's kind of
