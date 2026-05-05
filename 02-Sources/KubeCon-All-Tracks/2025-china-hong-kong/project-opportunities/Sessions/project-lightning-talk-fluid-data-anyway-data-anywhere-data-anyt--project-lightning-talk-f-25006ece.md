---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Tongyu Guo", "Maintainer"]
sched_url: https://kccncchn2025.sched.com/event/1xjz8/project-lightning-talk-fluid-data-anyway-data-anywhere-data-anytime-tongyu-guo-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluid+Data+Anyway%2C+Data+Anywhere%2C+Data+Anytime+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Fluid Data Anyway, Data Anywhere, Data Anytime - Tongyu Guo, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: China / Hong Kong
- Speakers: Tongyu Guo, Maintainer
- Schedule: https://kccncchn2025.sched.com/event/1xjz8/project-lightning-talk-fluid-data-anyway-data-anywhere-data-anytime-tongyu-guo-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluid+Data+Anyway%2C+Data+Anywhere%2C+Data+Anytime+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Fluid Data Anyway, Data Anywhere, Data Anytime.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1xjz8/project-lightning-talk-fluid-data-anyway-data-anywhere-data-anytime-tongyu-guo-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluid+Data+Anyway%2C+Data+Anywhere%2C+Data+Anytime+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MlIcDRadcA0
- YouTube title: Project Lightning Talk: Fluid Data Anyway, Data Anywhere, Data Anytime - Tongyu Guo, Maintainer
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-fluid-data-anyway-data-anywhere-data-anytime/MlIcDRadcA0.txt
- Transcript chars: 3504
- Keywords: provide, achieve, container, client, anywhere, however, integration, hybrid, abstraction, plug-in, definitions, volume, interface, address, workloads, cost, resources, deploy

### Resumo baseado na transcript

I'm Tingo the maintainer from the CNSF center project fluid and today I will introduce our project fluid for you and uh the most important is what is fluid and why our slogan is use data in any way use data anywhere and any time as everybody knows you're using process volume with the container storage interface address the data excise in general screeners. We provide a unified plug-in based fuse client integration map approach for multiple cache engines and allow cache engine vendors to achieve a low cost integration with zero code for CSS plug-in for it use a unified container resource definitions to provide a consistence objection As absolute in the diagram you can see user can deploy and scale the cache systems in hybrid cloud by creating and updating the fleet container custom resource runtimes. This exper experience is easily to achieved in traditional VM environments but is also wish to have the same simulated data usage experience in Kubernetes. By the way, Fleet has stood out in the latest incept technology radar reports which it received wise rec recognitions in the fields of bash processing, AI and machine learning and has been extensively deployed in so many users production environments and currently freed has more than 500 contributors and 40 adopters.

### Excerpt da transcript

Hello everyone. I'm Tingo the maintainer from the CNSF center project fluid and today I will introduce our project fluid for you and uh the most important is what is fluid and why our slogan is use data in any way use data anywhere and any time as everybody knows you're using process volume with the container storage interface address the data excise in general screeners. However, it's for shorts of the meeting the uni code features of AI workloads. Firstly, because of the expensive cost of resources combining the service and the server resources as a common choice for user to deploy the AI workloaded. However, it require a smart fuse client integration for environment adaptions and the second air workloads in variable from the high performance data sizing in hybrid cloud. But there is no native abstraction for distributed data cache layers. And secondly, during the AI application development, uh the it necessary to has a ability to dynamically mount the data size in a running port. However, the imunitability uh of the persist volumes due to the uh when the data set changes, it leads to the post reconstructions.

So to address several uh issues, fluid was initiated. A fluid used to build container data distribute cache interface in kubernetes. There are two key concepts in the fluid. The first one is data site. It is a mutable data abstraction layer and you can define a logical grouping of data source. You can define just like S3, HDFS and NAS in here and the second one the runtime. It is a pluggo distribute care system as such as electro and juice. The data operation allows you to achieve data proactive data warning and migration processings. As mentioned about fleet provide a smart containerizing fuse client at support two modes. The first mode is the CSI driver mode. It achieve native persistent volume attachments and we also provide a set card mode. It's designed for the service environment. It help user to use data in any way. The benefit for the cache engine vendor we provide a plug-in based fuse client integrations. We provide a unified plug-in based fuse client integration map approach for multiple cache engines and allow cache engine vendors to achieve a low cost integration with zero code for CSS plug-in for it use a unified container resource definitions to provide a consistence objection of distributed C systems in hybrid clouds.

As absolute in the diagram you can see user can deploy and scale the cache systems in hybrid cloud by creating and
