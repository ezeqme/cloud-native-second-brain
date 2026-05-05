---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Observability", "SRE Reliability"]
speakers: ["Ganeshkumar Ashokavardhanan", "Microsoft", "Yifan Yuan", "AlibabaCloud"]
sched_url: https://kccnceu2024.sched.com/event/1YeRU/scaling-up-without-slowing-down-accelerating-pod-start-time-ganeshkumar-ashokavardhanan-microsoft-yifan-yuan-alibabacloud
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+up+Without+Slowing+Down%3A+Accelerating+Pod+Start+Time+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scaling up Without Slowing Down: Accelerating Pod Start Time - Ganeshkumar Ashokavardhanan, Microsoft & Yifan Yuan, AlibabaCloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Ganeshkumar Ashokavardhanan, Microsoft, Yifan Yuan, AlibabaCloud
- Schedule: https://kccnceu2024.sched.com/event/1YeRU/scaling-up-without-slowing-down-accelerating-pod-start-time-ganeshkumar-ashokavardhanan-microsoft-yifan-yuan-alibabacloud
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+up+Without+Slowing+Down%3A+Accelerating+Pod+Start+Time+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scaling up Without Slowing Down: Accelerating Pod Start Time.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRU/scaling-up-without-slowing-down-accelerating-pod-start-time-ganeshkumar-ashokavardhanan-microsoft-yifan-yuan-alibabacloud
- YouTube search: https://www.youtube.com/results?search_query=Scaling+up+Without+Slowing+Down%3A+Accelerating+Pod+Start+Time+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RJ6Lt9bVNTw
- YouTube title: Scaling up Without Slowing Down: Accelerating Pod Start Time
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scaling-up-without-slowing-down-accelerating-pod-start-time/RJ6Lt9bVNTw.txt
- Transcript chars: 22047
- Keywords: container, registry, overlay, streaming, download, source, needed, storage, artifact, experience, reduce, projects, minutes, loading, gpu, workloads, network, already

### Resumo baseado na transcript

hi everyone and welcome to the session on scaling up without slowing down accelerating part start times we're so excited to see so many of you here today on this Friday afternoon and seeing this overflowing room is really thrilling thank you so much for joining us I'm Ganesh Kumar Ashok Karin a software engineer at Microsoft on the Azure kuet service team I work on node life cycle and GPU workloads I also developed this feature called artifact streaming which speeds up part start times on AKs in close

### Excerpt da transcript

hi everyone and welcome to the session on scaling up without slowing down accelerating part start times we're so excited to see so many of you here today on this Friday afternoon and seeing this overflowing room is really thrilling thank you so much for joining us I'm Ganesh Kumar Ashok Karin a software engineer at Microsoft on the Azure kuet service team I work on node life cycle and GPU workloads I also developed this feature called artifact streaming which speeds up part start times on AKs in close collaboration with the Azure container registry team with me today is Yan Yuan from Alibaba cloud storage team and he's a major maintainer of the overlay BD open source project which we use for AKs and many other companies use as well have you ever had the situation where you're waiting to book tickets for your favorite concert or sports event May maybe it was a Taylor Swift concert and you go to the website and you're trying to book the ticket but the server crashes or you're not able to log in and make progress that's often H the case when you're trying to suddenly have many people book uh on a website or the load increases a lot and that could be because of many reasons such as Network congestion storage throttling or issues with containers being able to make progress and crash Loof back cops it could also be due to slow note scaleup that leads to a poor user experience and a developer experience so in this presentation we're going to talk about the common approaches you can use to speed up pod starts explain why pod start takes so long and we'll also share high level approaches to reduce pod start time and talk about the challenges that happen at scale when you're trying to scale up quickly we'll also show a demo with a challenging llm based workload and also talk about our experience integrating this in production and the various trade-offs that we'd have to consider so what are the common approaches to address this problem most container run times like container D already have a feature called layer sharing as you know a container image is made up of many layers and these layers need to be pulled and decompressed if the the layers are already present on the host node then container run times like container D don't need to pull it again there's another option through kubernetes from K 127 and there's a flag called serialized image pull and if you turn that flag to off or false then you can paralyze the pulls on your node this is especially useful in case
