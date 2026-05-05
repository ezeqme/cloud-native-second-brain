---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["William Wang", "Xuzheng Chang", "Huawei"]
sched_url: https://kccnceu2025.sched.com/event/1td1E/cloud-native-ai-harness-the-power-of-advanced-scheduling-for-high-performance-aiml-training-william-wang-xuzheng-chang-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+AI%3A+Harness+the+Power+of+Advanced+Scheduling+for+High-Performance+AI%2FML+Training+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Cloud Native AI: Harness the Power of Advanced Scheduling for High-Performance AI/ML Training - William Wang & Xuzheng Chang, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: William Wang, Xuzheng Chang, Huawei
- Schedule: https://kccnceu2025.sched.com/event/1td1E/cloud-native-ai-harness-the-power-of-advanced-scheduling-for-high-performance-aiml-training-william-wang-xuzheng-chang-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+AI%3A+Harness+the+Power+of+Advanced+Scheduling+for+High-Performance+AI%2FML+Training+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Cloud Native AI: Harness the Power of Advanced Scheduling for High-Performance AI/ML Training.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td1E/cloud-native-ai-harness-the-power-of-advanced-scheduling-for-high-performance-aiml-training-william-wang-xuzheng-chang-huawei
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+AI%3A+Harness+the+Power+of+Advanced+Scheduling+for+High-Performance+AI%2FML+Training+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yCyezOTVU_Y
- YouTube title: Cloud Native AI: Harness the Power of Advanced Scheduling for High-P... William Wang & Xuzheng Chang
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/cloud-native-ai-harness-the-power-of-advanced-scheduling-for-high-perf/yCyezOTVU_Y.txt
- Transcript chars: 19825
- Keywords: scheduling, network, actually, topology, basically, volcano, gpu, working, perspective, resource, training, workloads, underlying, cluster, performance, little, especially, support

### Resumo baseado na transcript

So uh we are going to share uh the uh uh work we have done in the recent uh times. So we will uh focus more about the uh the new uh features we are working on to uh accelerate the high performance AI uh machine learning trending. Um so we all know that uh in the recent years uh the rapid growth of AI uh workloads become more and more especially uh for the LMS uh you know that uh and from scale efficiency or uh performance perspective and more and more uh advanced setup and the deployment requirements have uh uh ra have been raised. uh before the name of uh this project volcano was used actually we were uh a sub project called the cuba batch in uh uh kubernetes scheduling sik and uh uh during that time we found that that actually you know uh workload awareness of Uh so uh we know that uh especially for their hyperscalers and a lot of uh large end users uh they are kind of uh designing their own AI uh cluster to make more uh powerful uh uh helping the training workloads and also uh more uh like this year for distributed uh inference. So on the left you can see actually uh like Nvidia DJX uh they have the concept called a super pot right basically uh group of nodes that are connected with very high uh performance uh GPU network we call it uh uh MVL link

### Excerpt da transcript

Hello everyone uh thanks for joining our talk. So uh we are going to share uh the uh uh work we have done in the recent uh times. Uh so basically it's uh also a talk about the volcano project. So we will uh focus more about the uh the new uh features we are working on to uh accelerate the high performance AI uh machine learning trending. Uh my name is Kevin Juan. Uh unfortunately uh William didn't make it here so I'm helping uh him to give the this talk. Uh personally uh my background is all about uh scheduling stuff. I started contributing to upstream kubernetes uh back to 2015 and so also a lot of uh sub projects and currently I'm also working on the uh TOC to help uh the uh whole uh community. So today's talk is more uh based on my personal expertise and also as the role of uh maintainer. Hello everyone. My name is Shu Jun and you can also call me Zir and I'm a maintainer of the candle. All right. Uh so basically we we will just uh cover uh the following part uh parts uh of the talk today uh a little bit background and deep dive our uh uh key features especially the new uh new ones for AI workloads.

Yeah. and also uh a little bit more about the uh scheduling stuff and the uh the future plan. Okay. Um so we all know that uh in the recent years uh the rapid growth of AI uh workloads become more and more especially uh for the LMS uh you know that uh and from scale efficiency or uh performance perspective and more and more uh advanced setup and the deployment requirements have uh uh ra have been raised. However, for uh users especially like uh the data scientists uh that they don't have much background about the um uh the infrastructure uh sort of things uh uh we think that simplicity is always very important thing. So it's kind of uh you know uh we need to always consider uh exposing more the like the topology like the underlying hardware thing as well as uh providing a a more simple way for uh the users to use. So uh based on our observation and the research we think that there are uh two key trends very uh closely relevant to the cloud native AI infrastructure especially uh also very relevant to the work we are uh working on.

So um from the resources layer uh uh previously we have done a lot of research and also uh implementation try out in the uh in node topology like new awareness and also like the the feature uh discovery thing and uh uh now and the focus uh and also the kind of attention extends to more inter node topology thing like the network to
