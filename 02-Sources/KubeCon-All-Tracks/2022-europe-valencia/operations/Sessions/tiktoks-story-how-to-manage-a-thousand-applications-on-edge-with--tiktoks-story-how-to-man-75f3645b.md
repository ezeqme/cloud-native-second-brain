---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Operations"
themes: ["GitOps Delivery"]
speakers: ["Qingkun Li", "TikTok/Bytedance Inc.", "Jesse Suen", "Akuity", "Inc."]
sched_url: https://kccnceu2022.sched.com/event/ytrb/tiktoks-story-how-to-manage-a-thousand-applications-on-edge-with-argo-cd-qingkun-li-tiktokbytedance-inc-jesse-suen-akuity-inc
youtube_search_url: https://www.youtube.com/results?search_query=TikTok%E2%80%99s+Story%3A+How+To+Manage+a+Thousand+Applications+on+Edge+With+Argo+CD+CNCF+KubeCon+2022
slides: []
status: parsed
---

# TikTok’s Story: How To Manage a Thousand Applications on Edge With Argo CD - Qingkun Li, TikTok/Bytedance Inc. & Jesse Suen, Akuity, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Operations]]
- Temas: [[GitOps Delivery]]
- País/cidade: Spain / Valencia
- Speakers: Qingkun Li, TikTok/Bytedance Inc., Jesse Suen, Akuity, Inc.
- Schedule: https://kccnceu2022.sched.com/event/ytrb/tiktoks-story-how-to-manage-a-thousand-applications-on-edge-with-argo-cd-qingkun-li-tiktokbytedance-inc-jesse-suen-akuity-inc
- Busca YouTube: https://www.youtube.com/results?search_query=TikTok%E2%80%99s+Story%3A+How+To+Manage+a+Thousand+Applications+on+Edge+With+Argo+CD+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre TikTok’s Story: How To Manage a Thousand Applications on Edge With Argo CD.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrb/tiktoks-story-how-to-manage-a-thousand-applications-on-edge-with-argo-cd-qingkun-li-tiktokbytedance-inc-jesse-suen-akuity-inc
- YouTube search: https://www.youtube.com/results?search_query=TikTok%E2%80%99s+Story%3A+How+To+Manage+a+Thousand+Applications+on+Edge+With+Argo+CD+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ftz5_lIepNA
- YouTube title: TikTok’s Story: How To Manage a Thousand Applications on Edge With Argo CD - Qingkun Li & Jesse Suen
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tiktoks-story-how-to-manage-a-thousand-applications-on-edge-with-argo/Ftz5_lIepNA.txt
- Transcript chars: 18883
- Keywords: argo, cluster, application, clusters, applications, configuration, directory, deployment, instance, manage, deploy, controller, parent, repository, configurations, create, distributed, common

### Resumo baseado na transcript

hi everyone thank you for attending our talk tick tock story how to manage a thousand applications on edge with argo cd in today's talk we'll do a case study on how tiktok is managing 3000 applications across 100 global edge clusters with argo cd and we'll discuss some considerations tips and techniques for using argo cd to manage cluster applications on the edge so before we start some quick introductions my name is jesse suen and i am a argo project lead and co-founder and cto of acuity.io which

### Excerpt da transcript

hi everyone thank you for attending our talk tick tock story how to manage a thousand applications on edge with argo cd in today's talk we'll do a case study on how tiktok is managing 3000 applications across 100 global edge clusters with argo cd and we'll discuss some considerations tips and techniques for using argo cd to manage cluster applications on the edge so before we start some quick introductions my name is jesse suen and i am a argo project lead and co-founder and cto of acuity.io which provides application delivery solutions powered by argo speaking with me today is chinkun li and i'll let him introduce himself thank you jessie my name is ching kun lee tech beat manager of edge platform team at tiktok we use kubernetes and cloud native technologies to manage teapots on-prem at clusters and help developers deploy and manage applications on the edge this is the overview of tick-tock's edge cluster we have around 100 edge clusters distributed around the world serving tick-tock as services such as video saving cash live streaming gaming and so on the size of our edge cluster varies from 10 to 60 nodes on each edge those are powerful server node with currently 96 cpu cores and the 256 giga memory for each node we also have the data center that can talk to all of those edge clusters the data center functions as both the management control plane as well as the service data plane for those edge clusters and edge services for example we have the argo cd that runs in the data center to deploy ad services to those edge clusters talking about edge cluster deployment this is the high level overview and architecture of our deployment infrastructure so each of our edge cluster is a step along kubernetes cluster they talk to the data center where we have argos id and the git ripple to manage the deployment for the edge services using githubs so our developers will put their kubernetes configuration for the ad services to the git repository and the central argo cd controller will pull those configuration from the git repository to sync and deploy them to the specified edge clusters for the deployment of all edge services they actually all follow the same pattern usually at service is deployed to many edge clusters and the service functionality and behavior of this edge service on all edge clusters are very similar or the same for example for the video setting cache service when deployed to all the edge clusters they all serve the same exciting functionality for
