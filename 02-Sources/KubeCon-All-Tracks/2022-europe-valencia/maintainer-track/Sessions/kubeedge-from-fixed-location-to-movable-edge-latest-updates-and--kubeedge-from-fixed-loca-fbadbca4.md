---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Kevin Wang (Zefeng)", "Huawei", "Yin Ding", "Google"]
sched_url: https://kccnceu2022.sched.com/event/ytnF/kubeedge-from-fixed-location-to-movable-edge-latest-updates-and-future-kevin-wang-zefeng-huawei-yin-ding-google
youtube_search_url: https://www.youtube.com/results?search_query=KubeEdge%3A+From+Fixed+Location+to+Movable+Edge%2C+Latest+Updates+and+Future+CNCF+KubeCon+2022
slides: []
status: parsed
---

# KubeEdge: From Fixed Location to Movable Edge, Latest Updates and Future - Kevin Wang (Zefeng), Huawei & Yin Ding, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Kevin Wang (Zefeng), Huawei, Yin Ding, Google
- Schedule: https://kccnceu2022.sched.com/event/ytnF/kubeedge-from-fixed-location-to-movable-edge-latest-updates-and-future-kevin-wang-zefeng-huawei-yin-ding-google
- Busca YouTube: https://www.youtube.com/results?search_query=KubeEdge%3A+From+Fixed+Location+to+Movable+Edge%2C+Latest+Updates+and+Future+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre KubeEdge: From Fixed Location to Movable Edge, Latest Updates and Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytnF/kubeedge-from-fixed-location-to-movable-edge-latest-updates-and-future-kevin-wang-zefeng-huawei-yin-ding-google
- YouTube search: https://www.youtube.com/results?search_query=KubeEdge%3A+From+Fixed+Location+to+Movable+Edge%2C+Latest+Updates+and+Future+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vN1KOC6wiB4
- YouTube title: KubeEdge: From Fixed Location to Movable Edge, Latest Updates and... Kevin Wang (Zefeng) & Yin Ding
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubeedge-from-fixed-location-to-movable-edge-latest-updates-and-future/vN1KOC6wiB4.txt
- Transcript chars: 21264
- Keywords: deployment, running, deploy, connection, device, control, application, broken, actually, communication, cannot, network, support, desired, another, basically, multiple, security

### Resumo baseado na transcript

so today we are talking about a coupe edge so kubernetes is currently a cncf incubation project so mainly i will talk about the latest update so my name is indian so kevin cannot make it due to the code so both of us are the maintainers and the founder of this project for today i'm going to talk about project history key features and architecture and deployment cases and user cases and mainly i will we'll talk about this performance and scalability test to show how impressive the project

### Excerpt da transcript

so today we are talking about a coupe edge so kubernetes is currently a cncf incubation project so mainly i will talk about the latest update so my name is indian so kevin cannot make it due to the code so both of us are the maintainers and the founder of this project for today i'm going to talk about project history key features and architecture and deployment cases and user cases and mainly i will we'll talk about this performance and scalability test to show how impressive the project is so at last i will talk about a little bit about our future roadmap so our journey so this project we founded in 2018 so we donated to cncf on that year and in 2019 march we entered the sincere sandbox and in 2020 september we become a incubation project in cncf so currently we have more than 5000 stars on github github and more than 1300 folks and more than uh 800 contributors and they are two for 240 more than uh code submitters and from 60 plus organizations so it's a well accepted project and we really appreciate our contributors so uh we fought sorry about that so for this project we mainly try to solve the cloud and edge connection issues so uh people all know uh the latency is one issue and also the autonomy when the network is broken there's a interesting topic is here the broken so edge needs to run autonomously and also because in the edge a lot of iot devices are connected that will have a lot of data generated we don't want to pass all this data back to the cloud so the massive data is another issue and also data privacy so we generate a lot of data in the ad side however however we don't want pass all them back to the cloud especially public cloud so we need ad computing the kube edge is built for this features so key features so we the kubernetes project support the native combination apis so when you deploy an app to the edge so you can use a kubernetes directly so that's a native kubernetes apis as a developer when you do the deployment you won't see any different you deploy an app to azure node or you deploy to a node into a node in data center and is transparent to the uh developers and also uh we can allow mix edge node and the node in the edge side and the node in data center you can have this mixed deployment another important thing is that we have a seamless ad and ad cloud coordination so it's transparent to the developers so the framework itself will handle all the communications between ad and cloud is transparent to the developers another thing
