---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Cong Gu", "Ankit Goyal", "LinkedIn"]
sched_url: https://kccncna2025.sched.com/event/27FcH/prepare-for-disruptions-how-we-upgrade-the-whole-ml-training-fleet-bi-weekly-cong-gu-ankit-goyal-linkedin
youtube_search_url: https://www.youtube.com/results?search_query=Prepare+for+Disruptions%3A+How+We+Upgrade+the+Whole+ML+Training+Fleet+Bi-weekly+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Prepare for Disruptions: How We Upgrade the Whole ML Training Fleet Bi-weekly - Cong Gu & Ankit Goyal, LinkedIn

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Cong Gu, Ankit Goyal, LinkedIn
- Schedule: https://kccncna2025.sched.com/event/27FcH/prepare-for-disruptions-how-we-upgrade-the-whole-ml-training-fleet-bi-weekly-cong-gu-ankit-goyal-linkedin
- Busca YouTube: https://www.youtube.com/results?search_query=Prepare+for+Disruptions%3A+How+We+Upgrade+the+Whole+ML+Training+Fleet+Bi-weekly+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Prepare for Disruptions: How We Upgrade the Whole ML Training Fleet Bi-weekly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcH/prepare-for-disruptions-how-we-upgrade-the-whole-ml-training-fleet-bi-weekly-cong-gu-ankit-goyal-linkedin
- YouTube search: https://www.youtube.com/results?search_query=Prepare+for+Disruptions%3A+How+We+Upgrade+the+Whole+ML+Training+Fleet+Bi-weekly+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qY46j--UrZk
- YouTube title: Prepare for Disruptions: How We Upgrade the Whole ML Training Fleet Bi-week... Cong Gu & Ankit Goyal
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/prepare-for-disruptions-how-we-upgrade-the-whole-ml-training-fleet-bi/qY46j--UrZk.txt
- Transcript chars: 31646
- Keywords: maintenance, checkpoint, training, cluster, disruption, multiple, checkpointing, disruptions, running, disrupted, basically, priority, process, workers, platform, capacity, mentioned, question

### Resumo baseado na transcript

I'm an engineer at LinkedIn in the AI platforms team and I have Frank my colleague with me who's the manager in the same team. Uh in this talk uh we'll give an overview of our training platform and our training clusters. we have we add initate containers or we annotate the parts to do kota management or provision storage. So this is regular OS fleet upgrades where we upgrade OS security patches or kernel upgrades. Uh so we have this uh hierarchical checkpoint where the primary checkpoint gets written to the in-memory local storage and the secondary checkpoint is uploaded to the remote storage or synchronously. Um this is the general life cycle or general set of events that Kubernetes port goes through uh during an eviction process.

### Excerpt da transcript

Thanks everyone for joining us. Uh I'm Monkit. I'm an engineer at LinkedIn in the AI platforms team and I have Frank my colleague with me who's the manager in the same team. Uh in this talk uh we'll give an overview of our training platform and our training clusters. Uh we'll also talk about what are disruptions and what different kind of disruptions we see in our cluster. uh and then we'll dive into different strategies we use to handle these disruptions for our large language jobs and uh we'll discuss other optimizations we do in our cluster to reduce the impact of these disruptions on the jobs. Uh finally we'll uh share some tangible results that we have seen and the impact from all the improvements we have made. LinkedIn is on prem. So we have multiple regions and these regions have heterogeneous capacity uh of GPUs and CPUs uh different numbers different SKUs uh and we are able to dynamically route our jobs based on data and resource uh availability. So our platform runs over 1 million execution of tasks per month.

Uh yeah this is a highle diagram of our training stack. So we at the very bottom we have fleet management or cluster management which is responsible for uh managing our GPU resources different kind of networking technologies and then we have incluster scheduling where we do multiple optimizations to effectively utilize our GPUs and uh effectively allocate resources to the jobs. And then we have kota management where we support hierarchical quotas for different verticals like ads, feeds, talent marketplace uh to ensure fair fair resource usage. Uh and then we also deploy multiple operators uh to to orchestrate different kind of training jobs depending on uh what users are trying to run. Uh some of these are open source, some of these are custom in-house operators. And then we have multi multi-reionuler at the very top which uh routes the jobs depending on data and compute availability to different regions. Uh observability is very well integrated throughout our stack. Uh and each of these components uh in some way is is aware of disruptions happening in the cluster and they participate in uh in us effectively handling them.

So let's take a look at what a job life cycle looks like uh uh in in our cluster. Uh so flight is the primary orchestrator and user interface for our users. This is what they use to author their uh training workflows. Uh which effectively uh when user requests let's say a tensorflow job it effectively creates a TF job r
