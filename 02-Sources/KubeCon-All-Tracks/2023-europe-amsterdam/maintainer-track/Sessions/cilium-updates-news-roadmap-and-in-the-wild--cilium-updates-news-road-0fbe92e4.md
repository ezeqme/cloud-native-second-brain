---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Liz Rice", "Isovalent", "Andy Allred", "EfiCode", "Richard Hartmann", "Grafana Labs"]
sched_url: https://kccnceu2023.sched.com/event/1HyTU/cilium-updates-news-roadmap-and-in-the-wild-liz-rice-isovalent-andy-allred-eficode-richard-hartmann-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Cilium+Updates%2C+News%2C+Roadmap%2C+and+in+the+Wild+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cilium Updates, News, Roadmap, and in the Wild - Liz Rice, Isovalent; Andy Allred, EfiCode; Richard Hartmann, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Liz Rice, Isovalent, Andy Allred, EfiCode, Richard Hartmann, Grafana Labs
- Schedule: https://kccnceu2023.sched.com/event/1HyTU/cilium-updates-news-roadmap-and-in-the-wild-liz-rice-isovalent-andy-allred-eficode-richard-hartmann-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Cilium+Updates%2C+News%2C+Roadmap%2C+and+in+the+Wild+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cilium Updates, News, Roadmap, and in the Wild.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyTU/cilium-updates-news-roadmap-and-in-the-wild-liz-rice-isovalent-andy-allred-eficode-richard-hartmann-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Cilium+Updates%2C+News%2C+Roadmap%2C+and+in+the+Wild+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RdAO_Kxe6tE
- YouTube title: Cilium Updates, News, Roadmap, and in the Wild - Liz Rice, Andy Allred, Richard Hartmann
- Match score: 0.774
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cilium-updates-news-roadmap-and-in-the-wild/RdAO_Kxe6tE.txt
- Transcript chars: 36211
- Keywords: psyllium, mesh, actually, network, running, grafana, hubble, essentially, little, networking, observability, security, istio, traffic, policy, cluster, virtual, authentication

### Resumo baseado na transcript

so uh welcome to the psyllium update session where any of you at psylliumcon yesterday yes awesome right it was good say first section today is just a little welcome to psyllium session how many of you are already using psyllium most of you good so you probably mostly know what psyllium is very quickly you most of you probably use it as a cni so providing networking in kubernetes psyllium service mesh which is extending that to service mesh capabilities using ebpf and and highlighting the capabilities of psyllium

### Excerpt da transcript

so uh welcome to the psyllium update session where any of you at psylliumcon yesterday yes awesome right it was good say first section today is just a little welcome to psyllium session how many of you are already using psyllium most of you good so you probably mostly know what psyllium is very quickly you most of you probably use it as a cni so providing networking in kubernetes psyllium service mesh which is extending that to service mesh capabilities using ebpf and and highlighting the capabilities of psyllium as a networking platform Hubble for observability and we're going to hear a little bit more about Hubble and observability and grafana integration later in this session and of course tetragon so let's get another show of hands how many of you have tried tetragon or been interested in tetragon okay so tetragon is the security observability subproject in psyllium I highly recommend you check it out really very briefly psyllium you know covers kubernetes networking in a really performant fashion because it's based on ebpf really high performance load balancing we have users who are using it outside of kubernetes as a load balancing platform security aspects around Network policy and transparent encryption and of course the ability to integrate multiple kubernetes clusters and external workloads that is another thing that you will hear more about from Thomas shortly Hubble is the observability platform that gives us visibility into individual Network flows aggregated metrics service maps and the ability to export all this metric information to whatever you want to export it to whether it's fluent D or Prometheus or grafana elastic whatever Sim you're using we can use as a destination for Hubble information and tetragon which uses the evpf knowledge that we have to instrument the kernel and give us insight into security relevant events foreign is being used by a lot of people and we have a lot of um use case studies videos blog posts and people describing how they're using psyllium that you can find on the psyllium website we've already got over a hundred end users documented publicly in the users file is there anybody here who is using psyllium but hasn't added themselves to the users file nobody wants to confess to that there's somebody who's confessed right so you need to go to the users.md file and submit a pull request to add your organization and uh you know we're seeing that number explode brilliant you can use eppf in basically any Cloud enviro
