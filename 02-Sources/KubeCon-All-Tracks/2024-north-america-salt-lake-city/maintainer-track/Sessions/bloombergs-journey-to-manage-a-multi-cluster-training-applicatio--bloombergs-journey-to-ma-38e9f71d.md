---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Yifan Zhang", "Wei-Cheng Lai", "Bloomberg"]
sched_url: https://kccncna2024.sched.com/event/1hoyD/bloombergs-journey-to-manage-a-multi-cluster-training-application-with-karmada-yifan-zhang-wei-cheng-lai-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Bloomberg%27s+Journey+to+Manage+a+Multi-Cluster+Training+Application+with+Karmada+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Bloomberg's Journey to Manage a Multi-Cluster Training Application with Karmada - Yifan Zhang & Wei-Cheng Lai, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Yifan Zhang, Wei-Cheng Lai, Bloomberg
- Schedule: https://kccncna2024.sched.com/event/1hoyD/bloombergs-journey-to-manage-a-multi-cluster-training-application-with-karmada-yifan-zhang-wei-cheng-lai-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Bloomberg%27s+Journey+to+Manage+a+Multi-Cluster+Training+Application+with+Karmada+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Bloomberg's Journey to Manage a Multi-Cluster Training Application with Karmada.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoyD/bloombergs-journey-to-manage-a-multi-cluster-training-application-with-karmada-yifan-zhang-wei-cheng-lai-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Bloomberg%27s+Journey+to+Manage+a+Multi-Cluster+Training+Application+with+Karmada+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PmaiEKpM1-Q
- YouTube title: Bloomberg's Journey to Manage a Multi-Cluster Training Application with Karmada - Y. Zhang, W. Lai
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/bloombergs-journey-to-manage-a-multi-cluster-training-application-with/PmaiEKpM1-Q.txt
- Transcript chars: 23241
- Keywords: cluster, resource, clusters, carada, resources, deployment, scheduling, propagation, bloomberg, policy, training, member, replica, running, policies, platform, create, finally

### Resumo baseado na transcript

hello everyone um welcome to today's talk so um today we'll be talking about Bloomberg's journey to manage a multicluster training application with kada uh my name is Ean I am a software engineer on the data science platform team at Bloomberg my name is way Li I'm in the same team with Ean also in the data science platform engineering at Bloomberg so here is the agenda for today so we'll be talking about what is data science platform in short DSP at Bloomberg and we'll be talking about

### Excerpt da transcript

hello everyone um welcome to today's talk so um today we'll be talking about Bloomberg's journey to manage a multicluster training application with kada uh my name is Ean I am a software engineer on the data science platform team at Bloomberg my name is way Li I'm in the same team with Ean also in the data science platform engineering at Bloomberg so here is the agenda for today so we'll be talking about what is data science platform in short DSP at Bloomberg and we'll be talking about what is kada and how we use carada in Bloomberg and finally we'll be closing this talk with a future road map of carada and also a Q&A session so uh let's begin with a brief introduction to the data science platform so DSP at at Bloomberg provides an on Prem bare metal-based kubernetes infrastructure for the entire machine learning life cycle from data experimenting based on jbit Notebook to model training which is built upon the C flow project uh especially training operator and also to uh model inferencing using kerve so today we'll be mainly focusing on the model training part so uh here is a very high level simplified architecture of DSP so DSP is divided into multiple tiers uh according to the network Z Network Zone where the cluster lives so for example we have Dev tier and PR tier so each tier has multiple clusters in it uh the the different clusters are located in different data centers in different GE geographical places to ensure disaster recovery and DSP supports multi-tenancy for different AI teams at Bloomberg by using kubet native namespace and we also managed a quota that uh each name each team is allowed to use um using kubernetes uh resource quota so the quota is duplicated across different clusters within the same tier so that whenever one data center goes down users can submit their jobs to the other dat data center the other cluster uh without facing any quota related issue and finally configurations such as config maps and secrets are managed separately so basically we are allowing users to have different configurations to run their model job training jobs on different clusters and also using different credentials to connect to external services so the uh the uh setup we just talked about has actually brought us a few challenges so the first problem is uh the separate configuration and credential management so because uh we're allowing users to have different credentials configurations on different clusters it is very likely that that uh a certain config
