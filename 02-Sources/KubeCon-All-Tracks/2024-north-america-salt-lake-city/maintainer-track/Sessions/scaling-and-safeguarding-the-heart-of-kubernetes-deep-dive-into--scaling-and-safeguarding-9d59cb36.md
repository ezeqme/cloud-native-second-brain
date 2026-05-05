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
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Wenjia Zhang", "Marek Siarkowicz", "Google", "James Blair", "Red Hat", "Ivan Valdes Castillo", "Independent", "Wei Fu", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1hoxR/scaling-and-safeguarding-the-heart-of-kubernetes-deep-dive-into-etcd-wenjia-zhang-marek-siarkowicz-google-james-blair-red-hat-ivan-valdes-castillo-independent-wei-fu-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+and+Safeguarding+the+Heart+of+Kubernetes%3A+Deep+Dive+Into+etcd+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scaling and Safeguarding the Heart of Kubernetes: Deep Dive Into etcd - Wenjia Zhang & Marek Siarkowicz, Google; James Blair, Red Hat; Ivan Valdes Castillo, Independent; Wei Fu, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Wenjia Zhang, Marek Siarkowicz, Google, James Blair, Red Hat, Ivan Valdes Castillo, Independent, Wei Fu, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1hoxR/scaling-and-safeguarding-the-heart-of-kubernetes-deep-dive-into-etcd-wenjia-zhang-marek-siarkowicz-google-james-blair-red-hat-ivan-valdes-castillo-independent-wei-fu-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+and+Safeguarding+the+Heart+of+Kubernetes%3A+Deep+Dive+Into+etcd+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scaling and Safeguarding the Heart of Kubernetes: Deep Dive Into etcd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxR/scaling-and-safeguarding-the-heart-of-kubernetes-deep-dive-into-etcd-wenjia-zhang-marek-siarkowicz-google-james-blair-red-hat-ivan-valdes-castillo-independent-wei-fu-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Scaling+and+Safeguarding+the+Heart+of+Kubernetes%3A+Deep+Dive+Into+etcd+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q_HZo5Mu8Fk
- YouTube title: Scaling and Safeguarding the Heart of Kubernetes: Deep Dive Into etcd - Panel
- Match score: 1.038
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scaling-and-safeguarding-the-heart-of-kubernetes-deep-dive-into-etcd/q_HZo5Mu8Fk.txt
- Transcript chars: 21968
- Keywords: feature, working, happened, basically, operator, compaction, important, cluster, actually, history, guarantees, together, around, clusters, experimental, information, releases, distributed

### Resumo baseado na transcript

thank you for attending the scaling and safeguarding the Heart of kubernetes a quick question for the audience what's the heart of kubernetes SD thank you that's the only answer I heard thank you very much I just make sure you're still awake and then at the right session um so yes this is a sick s um meeting or track talk uh my name is wja I am one of the um chair of sck SD I I am also the uh engineering manager of Google we work on

### Excerpt da transcript

thank you for attending the scaling and safeguarding the Heart of kubernetes a quick question for the audience what's the heart of kubernetes SD thank you that's the only answer I heard thank you very much I just make sure you're still awake and then at the right session um so yes this is a sick s um meeting or track talk uh my name is wja I am one of the um chair of sck SD I I am also the uh engineering manager of Google we work on GK and open source kubernetes and ND hey team uh my name is James bler I'm a specialist architect at red hat and uh coach here for S City alongside W hello guys uh I'm Ivan Valdez or Ivan um I'm contribut on my free time and basically what I do in ET is I specialize in cicd automation uh releases and um tooling hello I'm Mark shovi I'm Tech lead for S at CD H I work at Google leading the uh gkd Team all right so here's a quick agenda of today's uh topics we'll start with a quick introduction of the sick and then we'll go um into some of the highlight of the project all right uh so um this is the team of SD and then you have seen three of us and we also have another tech lead uh from vmw called uh Benjamin Wong some of you uh have seen him in um Paris all right um the sick SD owns the sdd project and how it how it is used by kubernetes and as the storage of uh kubernetes our goal is very simple we want to provide the best production level data store for cloud native distributed system and it should be reliable simple to maintain and scale all right next is the exciting uh moment um I don't know if you have been to the contributor Summit so if you haven't you have you probably missed this this year uh when we when SD become the sick of kubernetes the first cuon we didn't have any award winners and this year we actually have three of them which is very exciting for us and very proud um um first award winner is even or Ian V this um so um this was not read out at the contributor Summit because there are too many Award winners so I want to read this out here uh uh thank you Ivan you have been extremely active across a number of SD sub projects and help takes the S SD tooling to another level and we deeply appreciate your contribution and and thank you for your hard work all right next winner is suen from Google suen made crucial contribution to some of our most important road maps for at CD and uh both wiing the SED and Coronet sub project related to sedd uh thank you Cen for your help towards making um SD 3.6 a real reality and the
