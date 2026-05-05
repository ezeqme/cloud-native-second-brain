---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Wenbo Qi", "Chenyu Zhang", "Ant Group"]
sched_url: https://kccnceu2026.sched.com/event/2EF79/dragonfly-v240-intro-updates-data-distribution-in-ai-infrastructure-wenbo-qi-chenyu-zhang-ant-group
youtube_search_url: https://www.youtube.com/results?search_query=Dragonfly+V2.4.0+-+Intro%2C+Updates%2C+Data+Distribution+in+AI+Infrastructure+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure - Wenbo Qi & Chenyu Zhang, Ant Group

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Wenbo Qi, Chenyu Zhang, Ant Group
- Schedule: https://kccnceu2026.sched.com/event/2EF79/dragonfly-v240-intro-updates-data-distribution-in-ai-infrastructure-wenbo-qi-chenyu-zhang-ant-group
- Busca YouTube: https://www.youtube.com/results?search_query=Dragonfly+V2.4.0+-+Intro%2C+Updates%2C+Data+Distribution+in+AI+Infrastructure+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF79/dragonfly-v240-intro-updates-data-distribution-in-ai-infrastructure-wenbo-qi-chenyu-zhang-ant-group
- YouTube search: https://www.youtube.com/results?search_query=Dragonfly+V2.4.0+-+Intro%2C+Updates%2C+Data+Distribution+in+AI+Infrastructure+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zjCFSEVvaX4
- YouTube title: Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure - Wenbo Qi & Chenyu Zhang
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/dragonfly-v2-4-0-intro-updates-data-distribution-in-ai-infrastructure/zjCFSEVvaX4.txt
- Transcript chars: 14751
- Keywords: download, solution, container, models, artifact, distribution, dronefly, inference, bandwidth, storage, downloading, management, cluster, reduce, native, registry, distribute, second

### Resumo baseado na transcript

I hope my introduction can let you know about the current status of the dronefly. Dronely delivers efficient, stable and secure date distribution and acceleration powered by the P2P technology. The first solution is to use the drumfly to distribute the image based on the P2P which is suitable for the large scale cluster. The second solution is to use the drumfly and the nidos to distribute the serated image which is suitable for the large scale cluster and the faster container launching. Jump flies post the large scale fail distribution and uh use the P2P to eliminate the impact of the origin bandwidth limitations. It also supports different object storage including the S3, OSS, OBS in the field of the AI infrastructure.

### Excerpt da transcript

Hello everyone, my name is Wimbu. You can call me Gio. I'm the maintainer of the drone fly. I hope my introduction can let you know about the current status of the dronefly. I hope that developers can be interested in the dronefly project. Thank you for join us. Okay. Dronely delivers efficient, stable and secure date distribution and acceleration powered by the P2P technology. It aims to be the best practice and the standard solution in the cloud native architectures. It's designed to improve the performance of the large scale cluster uh delivery across the files container image OC artifacts AI models cache logs. You can see that in the container registry the of the sens landscape there are two graduated project. One is harbor as a artifact registry and the other is dronefly as a image acceleration and fail distribution system. Okay. Next let me introduce the nidos a sub project of the drunkfly. It provides a file system on the based on the RAFS format. The most important feature is to make the container image are downloaded on demand in the trunk and the trunk level dduplication to reduce the storage and memory cost.

It can reduce the end to end code launching of the container image from the minutes to the seconds. Okay. Next, now drone fly focus on the three part uh image acceleration, fail distribution and the AI infa in the field of the image acceleration. Don't flies container clans such as the canodi docker cryo oras. It provides the three solutions for the image acceleration. The first solution is to use the drumfly to distribute the image based on the P2P which is suitable for the large scale cluster. The second solution is to use the drumfly and the nidos to distribute the serated image which is suitable for the large scale cluster and the faster container launching. The third solution is to use the Nidus uh to distribute the accelerated image which is suitable for the faster container launching in the field of the fail distribution. Jump flies post the large scale fail distribution and uh use the P2P to eliminate the impact of the origin bandwidth limitations. It supports protocols including the HTTP, HDFS.

It also supports different object storage including the S3, OSS, OBS in the field of the AI infrastructure. Drone flight post accelerated the data distribution during the AI training and AI inference. In the AI inference, drone flight supports the model pack to distribute the AI model. It also supports downloading models and this side from
