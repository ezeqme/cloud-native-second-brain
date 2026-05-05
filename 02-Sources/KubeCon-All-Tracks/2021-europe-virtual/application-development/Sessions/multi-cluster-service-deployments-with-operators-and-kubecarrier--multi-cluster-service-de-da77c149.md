---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Application + Development"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Rastislav Szabó", "Kubermatic"]
sched_url: https://kccnceu2021.sched.com/event/iE5Q/multi-cluster-service-deployments-with-operators-and-kubecarrier-rastislav-szabo-kubermatic
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Cluster+Service+Deployments+with+Operators+and+KubeCarrier+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Multi-Cluster Service Deployments with Operators and KubeCarrier - Rastislav Szabó, Kubermatic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Application + Development]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Rastislav Szabó, Kubermatic
- Schedule: https://kccnceu2021.sched.com/event/iE5Q/multi-cluster-service-deployments-with-operators-and-kubecarrier-rastislav-szabo-kubermatic
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Cluster+Service+Deployments+with+Operators+and+KubeCarrier+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Multi-Cluster Service Deployments with Operators and KubeCarrier.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5Q/multi-cluster-service-deployments-with-operators-and-kubecarrier-rastislav-szabo-kubermatic
- YouTube search: https://www.youtube.com/results?search_query=Multi-Cluster+Service+Deployments+with+Operators+and+KubeCarrier+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aTQeeS9cv98
- YouTube title: Multi-Cluster Service Deployments with Operators and KubeCarrier
- Match score: 1.0
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/multi-cluster-service-deployments-with-operators-and-kubecarrier/aTQeeS9cv98.txt
- Transcript chars: 14212
- Keywords: cluster, clusters, multi-cluster, instance, custom, management, resource, application, tenant, running, operators, export, multiple, provider, instances, cubecarrier, across, resources

### Resumo baseado na transcript

hello and welcome to my talk my name is rastisal and today i'll be speaking about multi-cluster service deployments with operators and keep carrier so before we start let me introduce myself i am a software engineer at cobramatik where i am working on cobramatic kubernetes platform and cubecarrier open source projects i am specialized on multi-cluster application management and multi-cluster networking and in the past i also contributed to several other other open source projects such as regatta i o fdi opp contv ppp cni or 6 repo so

### Excerpt da transcript

hello and welcome to my talk my name is rastisal and today i'll be speaking about multi-cluster service deployments with operators and keep carrier so before we start let me introduce myself i am a software engineer at cobramatik where i am working on cobramatic kubernetes platform and cubecarrier open source projects i am specialized on multi-cluster application management and multi-cluster networking and in the past i also contributed to several other other open source projects such as regatta i o fdi opp contv ppp cni or 6 repo so as the title of the talk suggests it will be about multi-cluster service deployments today during the talk i will go through different aspects of multi-cluster service deployments and i will also mention some community driven open source projects related to them we'll go through multi-cluster infrastructure management then multi-cluster application management and finally multi-cluster networking at the end of the talk i will also show a quick demo of multi-cluster application deployment with cubecarrier and multi-cluster networking with submariner so before we go into any details let me talk about use cases for deploying applications across multiple clusters one of the reasons for doing that may be close user proximity for example we would like to serve users from different parts of the world without high latency another reason may be regional high availability where we may want to minimize the impact of regional outages another reason may be security and organizational separation for instance we may have to use dedicated clusters for each organization or organization you didn't the next one may be data locality for example databases with sensitive data may be only available on in on premises clusters and last but not least one of the biggest use cases is edge computing where we usually run many smaller clusters distributed across multiple locations uh because of flow latency requirements so let's start our multi-cluster service deployment story with the necessary infrastructure for running and managing multiple clusters for that each cloud provider usually provides their own solution but if you wanted to automate operation of many clusters across multiple regions and different cloud providers including on-premises infrastructure and do that all by a single pane of glass or a single api endpoint i really recommend you to take a look at the open source kubernetes kubernetes platform which can easily do it for you okay let's ass
