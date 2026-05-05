---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Rachel Sheikh", "Cash App"]
sched_url: https://kccncna2024.sched.com/event/1i7lc/cash-apps-journey-into-a-multi-cluster-ecosystem-rachel-sheikh-cash-app
youtube_search_url: https://www.youtube.com/results?search_query=Cash+App%27s+Journey+Into+a+Multi-Cluster+Ecosystem+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cash App's Journey Into a Multi-Cluster Ecosystem - Rachel Sheikh, Cash App

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Rachel Sheikh, Cash App
- Schedule: https://kccncna2024.sched.com/event/1i7lc/cash-apps-journey-into-a-multi-cluster-ecosystem-rachel-sheikh-cash-app
- Busca YouTube: https://www.youtube.com/results?search_query=Cash+App%27s+Journey+Into+a+Multi-Cluster+Ecosystem+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cash App's Journey Into a Multi-Cluster Ecosystem.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lc/cash-apps-journey-into-a-multi-cluster-ecosystem-rachel-sheikh-cash-app
- YouTube search: https://www.youtube.com/results?search_query=Cash+App%27s+Journey+Into+a+Multi-Cluster+Ecosystem+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9TSNOVJ6BEY
- YouTube title: Cash App's Journey Into a Multi-Cluster Ecosystem - Rachel Sheikh, Cash App
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cash-apps-journey-into-a-multi-cluster-ecosystem/9TSNOVJ6BEY.txt
- Transcript chars: 37389
- Keywords: cluster, clusters, traffic, migration, process, making, platform, multicluster, number, looking, environment, resources, secrets, provision, tooling, actually, deploy, getting

### Resumo baseado na transcript

hi everyone my name is Rachel I am from cash app uh and together with my colleagues we own operate and maintain our kubernetes Fleet for cash app services today I'm going to be talking to you about some work we've done over the past year to delve into the multicluster ecosystem with our kubernetes setup um so just to set the ground a little before multicluster we had about six clusters that we were operating um three of these being actual services so we have a prod development and

### Excerpt da transcript

hi everyone my name is Rachel I am from cash app uh and together with my colleagues we own operate and maintain our kubernetes Fleet for cash app services today I'm going to be talking to you about some work we've done over the past year to delve into the multicluster ecosystem with our kubernetes setup um so just to set the ground a little before multicluster we had about six clusters that we were operating um three of these being actual services so we have a prod development and staging cluster and three maintenance utility clusters uh we had about 5,000 nodes we had 500 services on these clusters and um a pretty high number of cores RAM and dis usage after multicluster we can see that same number of services double number of clusters but relatively comparable cores RAM and dis usage and we've actually seen a decrease in node usage thanks to some work we've done around our Carpenter setup so why would you want to use multicluster when you're you when you're running kuiz uh clusters um the big part is removing a single point of failure and improving platform resiliency the case study that we have is when you're doing an in place upgrade or just a cluster fails and you only have one cluster tied to your environment you lose that environment until you spin up another cluster or restore your cluster back to normal um so part of this is building into multicluster spreading out multiple clusters per environment so that we can fail over more easily whenever we need it um and so part of this extension into what we're looking in 2025 and Beyond is looking into new operational opportunities to simplify adding more clusters to our environment and making it easier for us to spin them up tear them down and migrate Services back and forth between them uh the last part is reducing per cluster resource usage uh part of R case study from last year is when we upgraded up uh our kubernetes version we saw that there were just too many API server calls because we have too many services running the same cluster fully scaled up and the API server couldn't keep up with it until we over provisioned it however even if you want to move to multicluster there are some challenges along the way uh first thing you have to consider is resources for services things like Secrets Etc config maps how do you keep them synced across clusters in the same state to make sure you're serving traffic reliably how do you make sure that as you're moving services between clusters that you are making s
