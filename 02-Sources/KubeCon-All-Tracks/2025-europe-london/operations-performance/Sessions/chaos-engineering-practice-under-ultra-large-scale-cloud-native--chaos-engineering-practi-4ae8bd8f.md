---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Yue Bao", "Huawei", "yue li", "DaoCloud"]
sched_url: https://kccnceu2025.sched.com/event/1tx9Y/chaos-engineering-practice-under-ultra-large-scale-cloud-native-edge-computing-yue-bao-huawei-yue-li-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=Chaos+Engineering+Practice+Under+Ultra-large-scale+Cloud+Native+Edge+Computing+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Chaos Engineering Practice Under Ultra-large-scale Cloud Native Edge Computing - Yue Bao, Huawei & yue li, DaoCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Yue Bao, Huawei, yue li, DaoCloud
- Schedule: https://kccnceu2025.sched.com/event/1tx9Y/chaos-engineering-practice-under-ultra-large-scale-cloud-native-edge-computing-yue-bao-huawei-yue-li-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=Chaos+Engineering+Practice+Under+Ultra-large-scale+Cloud+Native+Edge+Computing+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Chaos Engineering Practice Under Ultra-large-scale Cloud Native Edge Computing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9Y/chaos-engineering-practice-under-ultra-large-scale-cloud-native-edge-computing-yue-bao-huawei-yue-li-daocloud
- YouTube search: https://www.youtube.com/results?search_query=Chaos+Engineering+Practice+Under+Ultra-large-scale+Cloud+Native+Edge+Computing+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CK7Il4ZiqTA
- YouTube title: Chaos Engineering Practice Under Ultra-large-scale Cloud Native Edge Computing - Yue Bao & yue li
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/chaos-engineering-practice-under-ultra-large-scale-cloud-native-edge-c/CK7Il4ZiqTA.txt
- Transcript chars: 12745
- Keywords: kubage, cluster, testing, latency, devices, computing, scenarios, management, native, defined, resources, collaboration, results, message, channel, various, clusters, master

### Resumo baseado na transcript

It's my pleasure to uh have this opportunity to share the testing of large scale edge computing using KU edge as well as the work we have done to ensure the stability at a scale. Uh before starting the presentation let me briefly introduce Yani and uh myself. Uh at the same time users of the Kubage community have also impressed demands for managing niscale edge computing edge nodes and edge applications. As the project involves the scale of edge nodes and applications will continue to grow. The vehicle cloud collaborative collaborative management platform built using Kubage is the first cloud edge and integrated architecture in the automotive industry enabling rapid software upgrade and integration integration for software defined vehicles. In this platform, each car is treated as an edge nodes and the scale of edge nodes is expected to reach millions.

### Excerpt da transcript

Okay, time is almost up and let's start. Uh, good afternoon everyone. Welcome to be here. It's my pleasure to uh have this opportunity to share the testing of large scale edge computing using KU edge as well as the work we have done to ensure the stability at a scale. Uh before starting the presentation let me briefly introduce Yani and uh myself. Yani is the uh software quality engineer of doc and she is also the chair of sik testing of kubage community. Uh my name is Ba uh and I worked at Huawei now and uh I'm currently also a maintainer of Kubage community. Um uh is a beauty due to the scheduling conflicts. Yi is unable to attend this conference in person. So she interested in me to share this topic. Okay. uh let's talk let's talk about some uh background uh with the rapid development of 5G networks uh industrial IoT AI and other fields edge computing has become a trade leading the digital transformation uh future scenarios such as smart cities smart transportation smart health care and intelligent manufacturing ing are become more familiar to people.

Uh and edge computing has garnered much attention. Uh Gartner has said uh pointed out in that in 2023 the number of the uh smart devices at edge is more than 20 times the that of traditional IT devices. and uh uh by 2028 the integration of sensors, storage, computing and advanced AI cap capabilities in edge devices will grow steadily. uh due to the diverse types and largest numbers of IoT devices, the increase in the scale of IoT device uh connections brings significant challenges to unified management and operation and maintainers. Uh at the same time users of the Kubage community have also impressed demands for managing niscale edge computing edge nodes and edge applications. For example, in the high-speed tour station project based on Kubage, nearly 100,000 uh 100,000 edge nodes and over 500,000 edge applications are connected at highway tour stations across the country. As the project involves the scale of edge nodes and applications will continue to grow. The vehicle cloud collaborative collaborative management platform built using Kubage is the first cloud edge and integrated architecture in the automotive industry enabling rapid software upgrade and integration integration for software defined vehicles.

In this platform, each car is treated as an edge nodes and the scale of edge nodes is expected to reach millions. Uh before dive into how Kubage achieves large scale management and testing. We let
